# 1. About
SmartNote is a release note generation tool aimed at generating release notes **personalized** to your **project domain** and **audience type**. It does this by providing configurability and utilizating what is colloquially referred to as AI. More specifically, SmartNote utilizes **Supervised Learning** for classification and prioirity scoring and **LLMs (Large Language Models)** for summarization and formatting.

## 1.1 Replication
We have provided a docker image for those who want to simply generate a release note. For more information please see the README.md file in the replication folder. 

# 2. Setup Instructions
Before using SmartNote you need to prepare your working environment by installing the dependencies and correctly setting up the configuration file. Below you can find details on how to do that.

## 2.1 Set up prerequisites
We use conda and pixi for managing the dependencies of the project. To install:
```bash
# install miniforge
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
# install pixi
curl -fsSL https://pixi.sh/install.sh | bash
```

The commands above are for unix-like systems (Linux, MacOS). For Windows, you can download the Miniforge installer from [here](https://github.com/conda-forge/miniforge) and pixi from [here](https://pixi.sh).

## 2.2 Install dependencies
To install the dependencies and activate the environment, run the following command:
```bash
pixi install  # install dependencies
pixi shell  # start a shell with the dependencies installed
```

## 2.3. Configuration
The configuration for the classifier models are located in the `settings.toml` and `.settings.toml` files. These files are managed by `dynaconf`, and you can override the settings with environment variables. Check dynaconf's documentation (https://dynaconf.com/) for more information.

In `.secrets.toml`, the following settings are required:

```toml
[github]
token = "ghp_IIAAQQBBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSS"
# tokens = [ ... ] # optional

[openai]
# base_url = "https://api.openxxx.xxx" # optional
api_key = "sk-AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSS"

[proxy]
# https = "http://127.0.0.1:1080" # optional
```

## 2.4. Usage

The `smartdraft` module now supports a simple CLI interface. Below is an example of how to use the CLI to generate release notes for QuestDB between versions 8.0.3 and 8.1.0.

```bash
pixi run ipython --pdb -m smartdraft.generator -- questdb/questdb --previous-release 8.0.3 --current-release 8.1.0 --project-domain System --min-significance 0.15 --writing-style "Automatic" --structure-type "Change Type" --group-commits --show-significance
```

Note: Remove the `group-commits` flag to disable it. Similarly, remove `show-significance` flag to disable it.

We suggest you run the command above in an interactive python shell to debug any issues that may arise. When an exception is raised, run `interact` to enter the interactive mode and inspect the variables.

## 2.5. Command Line Arguments

| Argument Name         | Description                                                                                                                                 |
|-----------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| `-h`, `--help`        | **Help**: Displays the arguments and their descriptions before exiting.                                                                              |
| `--previous-release`  | **Previous Version Tag**: The previous version to compare the new version against (usually a branch or release tag).                      |
| `--current-release`   | **Current Version Tag**: The new version to compare to the old version (usually a branch or release tag).                                 |
| `--project-domain`    | **Project Domain**: The domain of the project (referenced in Table 3.1), or leave blank for automatic identification.                     |
| `--group-commits`     | **Group Commits**: Determines whether similar commits should be grouped and summarised into one entry (enabled by default).               |
| `--writing-style`     | **Writing Style**: Specifies the writing style for the release note (referenced in Table 2.2), or leave blank for automatic identification.|
| `--structure-type`    | **Structure Type**: Specifies the organisational structure of the release note (referenced in Table 2.1), or leave blank for automatic.   |
| `--min-significance`  | **Minimum Significance Threshold**: The minimum significance value required for commits to appear in the release note (default: 0.1).     |
| `--showsignificance`  | **Show Significance Value**: Appends the significance score of each commit to the generated release note.                                 |


# 3. Personalization Information

## 3.1. Project Domain

Research finds that different project domains utilize different writing styles and prioritize different types of content in their release notes. To take this into account, SmartNote automatically identifies the project domain using your project's readme file and description. You can also manually specify the project domain using the `--project-domain` arg. Below you can find a description of each project domain, its writing style and the type of content that would primarily be focused on in the release note.

| # | Project Domain         | Description                                                                                                                                              | Writing Style | Content                                                                                                      |
|---|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------|
| 0 | Application Software   | Software that offers end-users with functionality, such as browsers and text editors.                                                                    | Expository    | Prioritize performance, document changes, and dependency/environment information for ease of installation and upgrade for end users. Users of some Application Software projects may not be developers, thus technical details are not necessary and even cause confusion. |
| 1 | Libraries & Frameworks | Software that provides a collection of reusable functionalities to facilitate software development in specific domains such as Web and machine learning. | Expository    | Prioritize breaking changes and document changes to facilitate the usage of downstream projects.                                  |
| 2 | System Software        | Software that offers basic services and infrastructure to other software, e.g., operating systems, servers, and databases.                               | Persuasive    | Prioritize breaking changes and security changes but provide a more comprehensive introduction of various categories to serve a variety of audiences.            |
| 3 | Software Tool          | Software that facilitates developers with universal software development tasks, like IDEs and compilers.                                                 | Descriptive   | Prioritize performance, breaking changes, enhancements, and security to strengthen developers' confidence when they develop software with it. Most users of Software Tools projects are developers, who benefit from technical details. |

### 3.2. Writing Styles
The writing style determines how the content of the release note document is worded (i.e., use commit/pr title or summarize the commit using the LLM). It is set to automatic by default which means it will be based on the project domain. You can manually specify the writing style using the `--writing-style` arg.
| #  | Writing Style | Description                                                                                                                                                                                                                                   |
|----|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -1 | Automatic     | The writing style will automatically be determined by the project domain. See the [project domain](#31-project-domain) section for more details on which project domain utilizes which writing style.                                         |
| 0  | Persuasive    | In addition to presenting the content of related commits/PRs/issues, provide additional information to help developers understand the changes, such as the rationale behind the changes, the impact of the changes, and guides for upgrading. |
| 1  | Descriptive   | Rephrase the content of change-related commits/PRs/issues to increase the readability and summarize the content of similar commits/PRs/issues.                                                                                                |
| 2  | Expository    | Directly list the content (usually title) of change-related commits/PRs/issues.                                                                                                                                                               |

## 3.3. List Structure Type (Organization Strategies)
Research finds that 2/3rds of release notes are formatted as hierarchical lists and finds that organizing by change type is more common across all domains. Therefore, SmartNote is pre-configured to format as a heirarchical list which organises by change type. However, you can manually specify the structure type using the `--structure-type` arg.

| # | Strategy        | Description                                                                                                  |
|---|-----------------|--------------------------------------------------------------------------------------------------------------|
| 0 | Plain List      | All changes are presented as a plain list.                                                                   |
| 1 | Change Type     | Changes are organized based on their types of content, e.g., New Features, Fixed Bugs, and Breaking Changes. |
| 2 | Affected Module | Changes are grouped based on the modules they affect.                                                        |
| 3 | Change Priority | Changes are ranked based on their importance perceived by RN producers.                                      |

## 3.4. Minimum Significance
The minimum significance threshold, specified via the `--min-significance` arg, is used to determine which commits to remove from the output. The significance of each commit is calculated using a classification model that has been trained on commits using the Conventional Commit standard. The significance value is a float which ranges between 0 and 1. Important commits are ranked 1, while insignificant commits are ranked 0. 

Setting the minimum significance threshold to 0 means no commits will be removed. We recommend a minimum significance threshold of 0.15 as it strikes a good balance between verbosity and conciseness. However, you can adjust this value based on your project or the release.

## 3.5. Commit Grouping
The `--group-commits` arg determines whether commits are grouped by their associated pull request. Grouping commits helps improve readability by making the release note more concise. We recommend you group commits. 
