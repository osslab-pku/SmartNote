from github import Github, Repository
from tqdm.auto import tqdm
from datetime import datetime
from openai import OpenAI
import os
import csv
import tiktoken

# Initialize GitHub instance
g = Github("ghp_I...")
g.per_page = 100
api_key = "sk-proj-i..."
max_token = 127000
llm_model="gpt-4o"

def shorten_to_token_limit(input_string, max_tokens, model="gpt-4"):
    """
    Shortens a string to fit within the specified token limit.

    :param input_string: The string to shorten.
    :param max_tokens: The maximum number of tokens allowed.
    :param model: The OpenAI model (e.g., 'gpt-3.5-turbo' or 'gpt-4').
    :return: A shortened string fitting within the token limit.
    """
    # Load tokenizer for the specified model
    encoding = tiktoken.encoding_for_model(model)
    
    # Tokenize the string
    tokens = encoding.encode(input_string, disallowed_special=())
    
    # Trim the tokens if they exceed the limit
    if len(tokens) > max_tokens:
        tokens = tokens[:max_tokens]
    
    # Decode the tokens back to a string
    shortened_string = encoding.decode(tokens)
    return shortened_string

def get_commit_data(repo, start_tag, end_tag):
    # # Get the commits between two tags
    # start_commit = repo.get_git_ref(f'tags/{start_tag}').object.sha
    # end_commit = repo.get_git_ref(f'tags/{end_tag}').object.sha
    
    # Get the comparison between the two commits
    comparison = repo.compare(start_tag, end_tag)
    
    return comparison

def get_prs_from_commit(comparison):
    print("Getting PRs")
    relevant_prs = []
    print(comparison.commits.totalCount)
    for commit in comparison.commits:
        pulls = commit.get_pulls()
        print(pulls.totalCount)
        for pr in pulls:
            if pr not in relevant_prs:
                relevant_prs.append(pr)

    return relevant_prs

def get_prs_between_dates(repo: Repository, start_date, end_date):
    # Get PRs that were merged between the two dates
    pulls = repo.get_pulls(state='closed', sort='updated', direction='desc')

    relevant_prs = []

    for pr in tqdm(pulls, desc="Filtering PRs", total=pulls.totalCount):
        # If we use "pr.merged" it will make an api call for every single pr, causing significant delay.
        # Instead make sure the merged_at var is not null to ensure the pr was merged.
        #if pr.merged and start_date <= pr.merged_at <= end_date:
        if pr.merged_at and start_date <= pr.merged_at <= end_date:
            relevant_prs.append(pr)
        if pr.updated_at < start_date:
            break
    
    return relevant_prs

def get_commit_from_tag(repo, tag_name):
    """
    Get the commit SHA associated with a tag.
    Handles both lightweight and annotated tags.
    
    :param repo: PyGitHub repository object.
    :param tag_name: The name of the tag (e.g., 'v1.0.0').
    :return: The commit object associated with the tag.
    """
    tag_ref = repo.get_git_ref(f'tags/{tag_name}')
    tag_object = tag_ref.object

    if tag_object.type == 'commit':  # Lightweight tag
        return repo.get_commit(tag_object.sha)
    elif tag_object.type == 'tag':  # Annotated tag
        annotated_tag = repo.get_git_tag(tag_object.sha)
        return repo.get_commit(annotated_tag.object.sha)
    else:
        raise ValueError(f"Unexpected tag object type: {tag_object.type}")

def write_commit_data(name_with_owner: str, start_version: str, end_version: str, output_folder: str) -> str:
    # Get repository
    repo = g.get_repo(name_with_owner)

    # Get commit data
    comparison = get_commit_data(repo, start_version, end_version)

    # Get the dates of the tags for PR filtering
    start_commit = get_commit_from_tag(repo, start_version)
    end_commit = get_commit_from_tag(repo, end_version)

    start_date = start_commit.commit.author.date
    end_date = end_commit.commit.author.date

    # Get relevant PRs
    prs = get_prs_between_dates(repo, start_date, end_date)
    #prs = get_prs_from_commit(comparison)

    # Create output file
    output_file = f"{name_with_owner.split('/')[-1]}_changes_{start_version}_to_{end_version}.txt"
    if (output_folder != ""):
        output_file = f"{output_folder}/{output_file}"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header
        f.write(f"Changes between {start_version} and {end_version}\n")
        f.write("=" * 80 + "\n\n")

        # Write commit information
        f.write("COMMITS\n")
        f.write("-" * 80 + "\n\n")

        for commit in tqdm(comparison.commits, desc="Writing commits"):
            try:
                f.write(f"Commit: {commit.sha}\n")
                f.write(f"Author: {commit.commit.author.name}\n")
                f.write(f"Date: {commit.commit.author.date}\n")
                f.write(f"Message: {commit.commit.message}\n")
                f.write("-" * 40 + "\n\n")
            except:
                print(f"Error writing commit {commit.sha}")

        # Write PR information
        f.write("\nPULL REQUESTS\n")
        f.write("-" * 80 + "\n\n")

        for pr in tqdm(prs, desc="Writing PRs"):
            try:
                f.write(f"PR #{pr.number}: {pr.title}\n")
                f.write(f"Author: {pr.user.login}\n")
                f.write(f"Merged at: {pr.merged_at}\n")
                f.write(f"URL: {pr.html_url}\n")
                f.write(f"Description:\n{pr.body}\n")
                f.write("-" * 40 + "\n\n")
            except:
                print(f"Error writing PR {pr.number}")

        # Write file changes
        f.write("\nFILE CHANGES\n")
        f.write("-" * 80 + "\n\n")

        for file in tqdm(comparison.files, desc="Writing files"):
            try:
                f.write(f"File: {file.filename}\n")
                f.write(f"Status: {file.status}\n")
                f.write(f"Changes: +{file.additions} -{file.deletions}\n")
                if file.patch:
                    f.write("Diff:\n")
                    _pat = file.patch.split("\n")
                    _len = max(10, len(_pat)//3)
                    f.write("\n".join(_pat[:_len]) + "\n")
                f.write("\n" + "-" * 40 + "\n\n")
            except:
                print(f"Error writing file {file.filename}")

    print(f"Data has been saved to {output_file}")
    return output_file

# tell chatgpt to generate a release note
def gen_rn(name_with_owner: str, output_file: str, output_folder: str):
    with open(output_file, "rb") as f:
        input_text = f.read().decode("utf-8")

    #with open("token.txt", "r") as f:
    #    api_key = f.read()

    model_input = [{
        "role": "system",
        "content": "Now you are given the commits, PRs and file changes between two tags. Please generate a release note based on this information."
    },{
        "role": "user",
        "content": shorten_to_token_limit(input_text, max_token, llm_model)
    }]

    oai = OpenAI(api_key=api_key)

    response = oai.chat.completions.create(
        model=llm_model,
        messages=model_input,
        top_p=0.1,
        temperature=0.0,
    )

    output_file = f"{name_with_owner.split('/')[-1]}_release_note.txt"
    if (output_folder != ""):
        output_file = f"{output_folder}/{output_file}"
        os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, "w") as f:
        f.write(response.choices[0].message.content)

    print(f"Release note has been generated and saved to {output_file}")

def load_projects(file_path):
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

if __name__ == '__main__':
    #name_with_owner = "rustdesk/rustdesk"
    #start_version = "1.2.7"
    #end_version = "1.3.0"
    #output_folder = "naive_rn_no_prompt_engineering/"
    output_folder = ""

    projects = load_projects("projects.csv")
    for row in tqdm(projects, desc="Naive RN"):
        print(f"Starting {row['project_name']}...")
        output_file = write_commit_data(row['project_name'].strip(), row['old_version'].strip(), row['new_version'].strip(), output_folder)
        print("Generating RN...")
        gen_rn(row['project_name'], output_file, output_folder)
        print("")


    