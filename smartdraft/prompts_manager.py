from typing import List
import openai
import time
import tiktoken
from loguru import logger

from .dtypes import PROJECT_DOMAIN_TYPE, STRUCTURE_TYPE, ReleaseNoteEntry, OpenAIConfig
from .config import settings

# Prompt engineering tactics based on documentation from OpenAI
# "Use delimiters to clearly indicate distinct parts of the input" https://platform.openai.com/docs/guides/prompt-engineering/tactic-use-delimiters-to-clearly-indicate-distinct-parts-of-the-input
# "Chain of Thought Prompting: Split complex tasks into simpler subtasks" https://platform.openai.com/docs/guides/prompt-engineering/strategy-split-complex-tasks-into-simpler-subtasks
# "One Shot Prompting: Provide examples" https://platform.openai.com/docs/guides/prompt-engineering/tactic-provide-examples
# "Use intent classification to identify the most relevant instructions for a user query" https://platform.openai.com/docs/guides/prompt-engineering/tactic-use-intent-classification-to-identify-the-most-relevant-instructions-for-a-user-query
# "Specify the desired length of the output" https://platform.openai.com/docs/guides/prompt-engineering/tactic-specify-the-desired-length-of-the-output

# Domain descriptions and content (ref: Characterize Software Release Notes of GitHub Projects: Structure, Writing Style, and Content)
DOMAIN_DESCRIPTION: dict[PROJECT_DOMAIN_TYPE, str] = {
    "System": "Software that offers basic services and infrastructure to other software, e.g., operating systems, servers, and databases",
    "Tool": "Software that facilitates developers with universal software development tasks, like IDEs and compilers",
    "Library": "Software that provides a collection of reusable functionalities to facilitate software development in specific domains such as Web and machine learning",
    "Application": "Software that offers end-users with functionality, such as browsers and text editors",
}

DOMAIN_HINT: dict[PROJECT_DOMAIN_TYPE, str] = {
    "System": "prioritize breaking changes and security changes but provide a more comprehensive introduction of various categories to serve a variety of audiences",
    "Tool": "prioritize performance, breaking changes, enhancements, and security to strengthen developers' confidence when they develop software with it",
    "Library": "prioritize breaking changes and document changes to facilitate the usage of downstream projects",
    "Application": "prioritize performance, document changes, and dependency/environment information for ease of installation and upgrade for end users",
}

def _limit_str_len(s: str):
    if not isinstance(s, str):
        s = str(s)
    if len(s) >= 1000:
        return s[:500] + f"...[truncated {len(s)-1000} chars]..." + s[-500:]
    return s

class PromptsManager:
    def __init__(self, openai_config: OpenAIConfig):
        # create an OpenAI client
        self.openai_client = openai.Client(
            api_key=openai_config.api_key,
            base_url=openai_config.base_url,
        )
        self._oai_conf = openai_config
        self.tokenizer = tiktoken.encoding_for_model(openai_config.model)
    
    def tokenize(self, tcr: str):
        return self.tokenizer.encode(tcr, disallowed_special=())
    
    def count_tokens(self, tcr: str):
        return len(self.tokenize(tcr))
    
    def count_tokens_approx(self, tcr: str):
        """Approximate token count for ASCII characters"""
        return len(tcr) / 4
    
    def get_openai_config(self):
        return self._oai_conf

    def send_request(
        self, chat_messages: list[dict[str, str]]
    ) -> openai.ChatCompletion:
        completion = None

        logger.debug(f"<OpenAI> request: {_limit_str_len(chat_messages[-2:])}")
        try:
            completion = self.openai_client.chat.completions.create(
                messages=chat_messages,
                temperature=self._oai_conf.temperature,
                top_p=self._oai_conf.top_p,
                model=self._oai_conf.model,
            )
        except openai.RateLimitError:
            logger.info("Rate limit reached, waiting 1 minute before proceeding... ")
            time.sleep(60)
            completion = self.send_request(chat_messages)
        except openai.OpenAIError as e:
            logger.error(f"OpenAI Error: {e}")
            raise e
        logger.debug(f"<OpenAI> response: {_limit_str_len(completion.choices[0].message.content)}")

        return completion
    
    def get_first_completion(self, chat_messages: list[dict[str, str]]) -> str:
        completion = self.send_request(chat_messages)
        return completion.choices[0].message.content

    def summarize_commit(
        self, tcr: str, provide_technical_detail: bool
    ) -> str:
        logger.debug(f"Summarizing commit: {tcr[:40]}...")
        technical_detail_prompt = ""
        if provide_technical_detail:
            technical_detail_prompt = "Keep in mind most users of the project are developers, "
            "who benefit from technical details, therefore it would be beneficial to include technical details.\n\n"

        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with commit details (delimited with XML tags) and file changes "
                    "(delimited with XML tags) outlining the changes of a commit. "
                    + technical_detail_prompt
                    + "Use the following step-by-step instructions to respond to user input. Prefix each summary with the step number.\n\n"
                    "Step 1 - Summarize the changes into a short paragraph (about 50-100 words) so that it can seamlessly be included in a release note document.\n"
                    "Step 2 - Rewrite the summary from Step 1, removing any prefixes.\n"
                    "Step 3 - Rewrite the summary from Step 2 so that it is not a list.\n"
                    "Step 4 - Rewrite the summary from Step 3, removing references to affected files.\n"
                    "Step 5 - Rewrite the summary from Step 4, removing references to dependency updates.\n"
                    "Step 6 - Rewrite the summary from Step 5, removing references to version changes and updates.\n"
                    "\n\nOnly output the summary from Step 6."
                ),
            },
            {"role": "user", "content": tcr},
        ]
        return self.get_first_completion(prompt)

    def summarize_pr(
        self,
        entries: List[ReleaseNoteEntry],
        commit_dt: str,
        pr_title: str,
        pr_body: str,
        provide_technical_detail: bool,
    ) -> str:
        logger.debug(f"Summarizing PR: {pr_title[:40]}...")
        combined_entries = ""
        for entry in entries:
            combined_entries += f"""- [{entry.significance:.2f}] <{commit_dt}> {entry.summary.strip()}\n"""

        technical_detail_prompt = ""
        if provide_technical_detail:
            technical_detail_prompt = "Keep in mind most users of the project are developers, who benefit from technical details, therefore it would be beneficial to include technical details. "

        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with pull request details (delimited with XML tags) and "
                    "a list of summarized commits (delimited with XML tags) outlining the changes made in a pull request. "
                    + technical_detail_prompt
                    + "Each commit summary is prefixed with a number (prefixed with a dash and delimited with square brackets) between 0 and 1 which indicate the significance of the commit. The closer the number is to 1, the more important the commit. "
                    'For example, "- [0.5] Added a new feature." 0.5 in this case signifies that the entry is moderately significant.\n\n'
                    "Use the following step-by-step instructions to respond to user input. Prefix each summary with the step number.\n\n"
                    "Step 1 - Summarize the details and list of summarized commits into a short paragraph (about 100-200 words) so that it can seamlessly be included in a release note document.\n"
                    "Step 2 - Rewrite the summary from Step 1, removing insignificant commits.\n"
                    "Step 3 - Rewrite the summary from Step 2 so that it is not a list.\n"
                    "Step 4 - Rewrite the summary from Step 3, removing references to affected files.\n"
                    "Step 5 - Rewrite the summary from Step 4, removing references to dependency updates.\n"
                    "Step 6 - Rewrite the summary from Step 5, removing references to version changes and updates.\n"
                    "Step 7 - Rewrite the summary from Step 6, removing any prefixes.\n"
                    "\n\nOnly output the summary from Step 7."
                ),
            },
            {
                "role": "user",
                "content": f"<pull_request_details>Title: {pr_title}\n\nBody: {pr_body}\n\n</pull_request_details><summarized_commits>{combined_entries}</summarized_commits>",
            },
        ]

        return self.get_first_completion(prompt)

    def rewrite_to_suit_pd(
        self, 
        release_note: str, 
        project_domain: PROJECT_DOMAIN_TYPE,
        structure_type: STRUCTURE_TYPE
    ) -> str:
        logger.debug(f"Rewriting release note for project domain: {project_domain}...")
        categories: str = "-" + "\n-".join(settings.categories.conventional_commits) + "\n"
        category_prompt: str = ""
        if structure_type == "Change Type":
            category_prompt = f"You can categorize the each list item into the following categories:\n{categories}"
        else:
            category_prompt = "Do not add any prefixes."

        prompt = [
            {
                "role": "system",
                "content": str(
                    f"You will be provided with a release note document (formatted in markdown) outlining the changes in a {project_domain} project ({DOMAIN_DESCRIPTION[project_domain]}).\n\n"
                    f"Rewrite and reorder each list item so as to {DOMAIN_HINT[project_domain]}. "
                    "You can summarize and combine long list entries for conciseness but do not change the formatting of the document or add a prefix. For example, do not change or add new headings. "
                    "Most importantly, do not remove any links.\n\n"
                    + category_prompt
                ),
            },
            {"role": "user", "content": f"{release_note}"},
        ]
        return self.get_first_completion(prompt)

    def rewrite_for_conciseness(
        self, release_note: str
    ) -> str:
        logger.debug("Rewriting release note for conciseness...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with an entry in a release note document (formatted in markdown). "
                    "Analyze the change and rewrite it for conciseness. For example, remove sentence openers and vague or irrelevant statement.\n\n"
                    "Do not change the formatting of or add a prefix."
                    "Most importantly, do not remove any links."
                ),
            },
            {"role": "user", "content": f"{release_note}"},
        ]
        return self.get_first_completion(prompt)

    def combine_similar_entries(
        self, release_note: str
    ) -> str:
        logger.debug("Combining similar entries in release note...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with a release note document (formatted in markdown). "
                    "Combine similar points into a single list item to improve conciseness but do not combine them if it makes the list item dramatically longer.\n\n"
                    "Do not change or add new headings, the formatting of the document or add a prefix."
                    "Most importantly, do not remove any links."
                ),
            },
            {"role": "user", "content": f"{release_note}"},
        ]
        return self.get_first_completion(prompt)

    def rewrite_name_refs(
        self, release_note: str
    ) -> str:
        logger.debug("Rewriting release note to use new names...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with a release note document (formatted in markdown). "
                    "Analyze the change and rewrite it, making sure that all references to names are using the new name. "
                    "For example, if a function or variable was added and later renamed, the new name should be used and there should be no mention of it being renamed. \n\n"
                    "Do not change the formatting of the document or add a prefix. For example, do not change or add new headings."
                    "Most importantly, do not remove any links."
                ),
            },
            {"role": "user", "content": f"{release_note}"},
        ]
        return self.get_first_completion(prompt)

    def rewrite_func_info(
        self, release_note: str
    ) -> str:
        logger.debug("Rewriting release note to include function information...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with a release note document (formatted in markdown). "
                    "Analyze the change and rewrite it, removing references to changes of changes. "
                    "For example, if a function or variable was added and then later removed in the same commit or PR then it shouldn't be mentioned. "
                    "Similarly, if a function or variable was added in the same commit or PR and later changed, only information relevant to the latest state should be retained..\n\n"
                    "Do not change the formatting of the document or add a prefix. For example, do not change or add new headings."
                    "Most importantly, do not remove any links."
                ),
            },
            {"role": "user", "content": f"{release_note}"},
        ]
        return self.get_first_completion(prompt)

    def determine_commit_module(
        self, sha_combined_tcr: str
    ) -> str:
        logger.debug("Determining the most significantly affected module...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with commit details (delimited with XML tags) and file changes (delimited with XML tags) outlining the changes of a commit. "
                    "From the provided data, determine the most significantly affected module."
                    "\n\nYour response must be the identified module but rewritten so that it can be included as a header in documentation."
                    "\n\nDo not format your response in anyway."
                    "Most importantly, do not remove any links."
                ),
            },
            {"role": "user", "content": f"{sha_combined_tcr}"},
        ]
        return self.get_first_completion(prompt)

    def refine_module_categories(
        self, release_note: str
    ) -> str:
        logger.debug("Refining module categories in release note...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with a release note document (formatted in markdown). "
                    "Reduce the number of categories (headings) by combining them into an existing category.  "
                    "If they cannot be combined or the category does not contain many changes, categorize the changes under a misc category."
                    "\n\nOther than the misc category, do not add new category."
                ),
            },
            {"role": "user", "content": f"{release_note}"},
        ]
        return self.get_first_completion(prompt)
    
    def are_commit_messages_good(
        self, commit_messages: List[str]
    ) -> bool:
        """
        Guide GPT to determine whether commit messages are 'good' based on Yuxia's taxonomy
        of good commit messages (https://arxiv.org/pdf/2202.02974). In short, a commit message
        is considered good if it describes 'what' and 'why'.
        """
        logger.debug("Determining if commit messages are good and relevant...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with a list of commit messages."
                    "From the provided data, determine if the commit messages are of high quality and relevant to the project."
                    "A good commit message usually describes 'what' (summarize the change and the design decisions) "
                    "and 'why' (what is the problem, what is the goal of the change, and why the change is necessary). "
                    "\nExamples of good commit messages: "
                    "\n- Remove outdated key. `aggregate-key-pattern` is no longer defined but was still referenced in the documentation."
                    "\n- Fix concurrent problem of zookeeper configcenter, wait to start until cache being fully populated."
                    "\n- Polish pom.xml. Apply consistent formatting, drop JDK 8 support and cleanup repo."
                    "\nExamples of bad commit messages: "
                    "\n- Update README.md"
                    "\n- Fix bug"
                    "\n- A lot of changes"
                    "\n\nYour response must be a 'yes' or 'no' answer."
                    "\n\nDo not format your response in anyway."
                ),
            },
            {"role": "user", "content": '\n'.join(commit_messages)},
        ]
        _response = self.get_first_completion(prompt)
        if _response.strip().lower() == "no":
            return False
        if _response.strip().lower() == "yes":
            return True
        logger.warning(f"Unexpected response from GPT binary classification: {_response}")
        return False
    
    def reorder_rn_categories(
        self, release_note: str
    ) -> str:
        logger.debug("Reordering release note categories...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with a release note document (formatted in markdown). "
                    "Reorder the categories so that the most important categories are at the top and the least important are at the bottom."
                    "Normally, breaking changes and new features, bug fixes, and enhancements are considered the most important. "
                    "Document changes, dependency updates, and version changes are considered less important."
                    "\n\nDo not format the response in any way. "
                    "Do not add new categories. Do not remove any links. "
                    "Do not change the formatting of the document or add a prefix. "
                ),
            },
            {"role": "user", "content": f"{release_note}"},
        ]
        return self.get_first_completion(prompt)
    
    def determine_project_domain(
        self, project_description: str, readme_content: str
    ) -> PROJECT_DOMAIN_TYPE:
        """
        Guide GPT to classify a GitHub project into one of four categories:
        System Software, Libraries & Frameworks, Software Tools, or Application Software.
        """
        logger.debug("Classifying GitHub project...")
        prompt = [
            {
                "role": "system",
                "content": str(
                    "You will be provided with a project description and README content for a GitHub project. "
                    "Classify the project into one of the following categories:\n"
                    "System: software that offers basic services and infrastructure to other software, e.g., operating systems, servers, and databases.\n"
                    "Library: software that provides a collection of reusable functionalities to facilitate software development in specific domains such as Web and machine learning.\n"
                    "Tool: software that facilitates developers with universal software development tasks, like IDEs and compilers.\n"
                    "Application: software that offers end-users with functionality, such as browsers and text editors.\n\n"
                    "Your response must be one of these four categories exactly as written above.\n"
                    "Do not format your response in any way or provide any additional explanation."
                ),
            },
            {
                "role": "user", 
                "content": f"Project Description:\n{project_description}\n\nREADME Content:\n{readme_content}"
            },
        ]
        _response = self.get_first_completion(prompt)
        _response = _response.strip()

        if _response in settings.categories.project_domains:
            return _response
        else:
            logger.warning(f"Unexpected response from GPT classification: {_response}")
            return "Unclassified"
