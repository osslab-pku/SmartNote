from dataclasses import dataclass, field
from typing import List, Set, Literal, Optional, Dict, Any

# 11 conventional commits categories
# check https://www.conventionalcommits.org/en/v1.0.0/
CONVENTIONAL_COMMITS_TYPE = Literal[
    "build",
    "chore",
    "ci",
    "docs",
    "feat",
    "fix",
    "perf",
    "refactor",
    "revert",
    "style",
    "test",
]

# 4 project domains, see Jianyu's paper
PROJECT_DOMAIN_TYPE = Literal["Application", "Library", "System", "Tool"]
# 3 semantic versioning release types
RELEASE_TYPE = Literal["Major", "Minor", "Patch", "Unknown"]
# writing style
WRITING_STYLE_TYPE = Literal["Automatic", "Persuasive", "Descriptive", "Expository"]
# 4 organization strategies of the RN
STRUCTURE_TYPE = Literal[
    "Plain List", "Change Type", "Affected Module", "Change Priority"
]


@dataclass
class ReleaseNoteEntry:
    sha: List[str]
    summary: str
    type: str
    significance: float
    associated_prs: Set[str]
    date_time: str
    affected_module: str = ""


@dataclass
class ReleaseNotePrEntry:
    title: str
    body: str
    commits: Set[str]
    date_time: str


@dataclass
class ReleaseNoteCommitEntry:
    message: str
    prs: Set[int]
    sha: str
    date_time: str


@dataclass
class PersonalizationConfig:
    writing_style: WRITING_STYLE_TYPE = "Automatic"
    """If writing style is Automatic it will automatically be determined using the project domain, otherwise the specified style will be used."""

    project_domain: PROJECT_DOMAIN_TYPE = "Library"
    """Used for the analysis of the commit type and significance (See ProjectDomains(Enum) in rn_formatter.py). System Software, Software Tool, Libraries & FrameWorks, Application Software"""

    min_significance: float = 0.15
    """The minimum significance required to be included in the release note."""

    structure_type: STRUCTURE_TYPE = "Change Type"
    """Organization Strategies of the RN (See StructureType(Enum) in rn_formatter.py). 0: Plain List, 1: Hierarchical List by Change Type, 2: Hierarchical List by Affected Module, 3: Hierarchical List by Change Priority"""

    group_commits: bool = True
    """Group commits by PR and summarize them into a single entry (taking into consideration PR title and body) which constitutes the PR."""


@dataclass
class OpenAIConfig:
    api_key: str = "OpenAIAPIKeyRequiredHere"
    """API key for authentication"""

    model: str = "gpt-4o"
    """Model name to use"""

    temperature: float = 0.0
    """Sampling temperature"""

    top_p: float = 0.1
    """Nucleus sampling probability"""

    tpm: int = 30000
    """Tokens per minute (TPM) limit. Each ASCII character is approximately 4 tokens. Organizations start with a limit of 30000, but it can increase (see: https://platform.openai.com/docs/guides/rate-limits/usage-tiers)."""

    max_string_length: int = 1048576
    """Maximum length of strings"""

    max_model_context_length: int = 128000
    """Maximum context length specified in tokens (varies by model)"""

    ascii_token_len: int = 4
    """Number of tokens per ASCII character"""

    base_url: Optional[str] = None
    """Base URL for the API"""


@dataclass
class CommitData:
    sha: str
    message: str
    author_date: str
    author_name: str
    author_email: str
    additions: int
    deletions: int
    total: int
    is_merge_commit: bool = False

    @classmethod
    def from_gh_response(cls, response: Dict[str, Any]) -> 'CommitData':
        """Create an instance of CommitData from a GitHub response dictionary"""
        return cls(
            sha=response["sha"],
            message=response["commit"]["message"],
            author_date=response["commit"]["author"]["date"],
            author_name=response["commit"]["author"]["name"],
            author_email=response["commit"]["author"]["email"],
            additions=response["stats"]["additions"],
            deletions=response["stats"]["deletions"],
            total=response["stats"]["total"]
        )
