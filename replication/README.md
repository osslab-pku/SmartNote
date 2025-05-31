# Download
Replication Package Download Link: [https://doi.org/10.6084/m9.figshare.26994352.v2](https://doi.org/10.6084/m9.figshare.26994352.v2)

# 1. File Structure

The file structure of the replication package is as follows:

```bash
- docker_image.tar.zst # A docker image with all dependencies installed
- datasets/ # Contains the datasets for the classifiers and evaluation
- evaluation/ # Contains the generated RNs for the evaluation
- rq3_*.ipynb # The Jupyter notebooks for the training and evaluation of the classifiers
- rq4_auto_eval.ipynb # The Jupyter notebook for the automatic evaluation of the release notes (quant_eval.ipynb)
- rq4_human_eval.ipynb # The Jupyter notebook for the manual evaluation of the release notes (qual_eval.ipynb)
- pixi* # Environment manifests
```

Due to the size of the datasets and models and the space constriant of Figshare, we did not include all files in the replication package.

# 2. Using the Release Note Generator

For the ease of use, we provide a battery-included docker image with all the dependencies installed. 

## 2.1. Setup Instructions

The only prerequisites are:

- A Linux x86_64 machine with Docker installed.
- A GitHub token with read access to public repositories.
- A token for an OpenAI-compliant LLM API.

Import the docker image using the following command:

```bash
zstd -cd docker_image.tar.zst | docker load
```

## 2.2 Usage

To generate release notes for a project:

```bash
docker run --rm -it -e SMARTNOTE_GITHUB__TOKEN="ghp_XXXXXXXXXXXXXXXX" -e SMARTNOTE_OPENAI__API_KEY="sk-XXXXXXXXXXXXXXXXX" --gpus all smartnote:v2 twpayne/chezmoi --previous-release v2.52.0 --current-release v2.52.1 --group-commits --show-significance
```

Note: Remove the `group-commits` flag to disable it. Similarly, remove `show-significance` flag to disable it. We list and explain the personalisation options in Section 4.

Though we have not tested it, the docker image should work with any OpenAI-compliant LLM API (e.g., Cloudflare's AI Gateway or DeepSeek's API). You may set the `SMARTNOTE_OPENAI__BASE_URL` environment variable to the API's base URL.

## 2.2.1 Argument Breakdown
| Component                                                                                                 | Description                                                                                                                     |
|-----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
| `docker run`                                                                                              | Runs a Docker container.                                                                                                        |
| `--rm`                                                                                                    | Automatically removes the container once it exits.                                                                              |
| `-it`                                                                                                     | Allocates an interactive terminal (useful for command-line tools).                                                              |
| `-e SMARTNOTE_GITHUB__TOKEN="ghp_XXXXXXXXXXXXXXXX"`                                                      | Sets the environment variable `SMARTNOTE_GITHUB__TOKEN` to your GitHub Token for authentication with GitHub.                                           |
| `-e SMARTNOTE_OPENAI__API_KEY="sk-XXXXXXXXXXXXXXXXX"`                                                   | Sets the environment variable `SMARTNOTE_OPENAI__API_KEY` to your OpenAI API key for authenticatation with the OpenAI API.                                |
| `--gpus all`                                                                                              | Grants the container access to all available GPUs.                                                                              |
| `smartnote:v2`                                                                                              | The name of the Docker image being used (pre-built and includes the SmartNote binary).                          |
| `twpayne/chezmoi`                                                                                         | The name of the project repository being analysed.                                                                              |
| `--previous-release v2.52.0`                                                                              | Specifies the previous release tag to compare against.                                                                          |
| `--current-release v2.52.1`                                                                               | Specifies the new/current release tag.                                                                                          |
| `--group-commits`                                                                                         | Groups similar commits together in the release notes.                                                                           |
| `--show-significance`                                                                                     | Appends a significance score to each commit in the release note output.                                                         |

## 2.2.2 Environment Variables

| Variable             | Description                                                      | Default Value                         |
|----------------------------------|------------------------------------------------------------------|----------------------------------------|
| `SMARTNOTE_GITHUB__TOKEN`        | GitHub token used for accessing repository metadata and commits. | *(empty)*                              |
| `SMARTNOTE_OPENAI__API_KEY`      | API key for authenticating requests to OpenAI.                   | *(empty)*                              |
| `SMARTNOTE_OPENAI__BASE_URL`     | Base URL for OpenAI API requests.                                | `https://api.openai.com/v1`            |
| `HF_ENDPOINT`                    | Mirror endpoint for Hugging Face to speed up or reroute traffic. | `https://hf-mirror.com`                |
| `HF_HOME`                        | Cache directory for Hugging Face models and token files.         | `/app/.cache/`                         |
| `TIKTOKEN_CACHE`                 | Directory for caching `tiktoken` tokenizer data.                 | `/app/.cache/tiktoken`                 |


## 2.3 LLM Key
We used Open AI for this project, however you can replace the OpenAI Key with any compatible OpenAI LLM key. Here are instructions for obtaining your key.

- **Link:** [OpenAI API Key Page](https://platform.openai.com/account/api-keys)
- **Steps:**
  1. Sign in to your [OpenAI account](https://platform.openai.com/).
  2. Navigate to the **API Keys** section.
  3. Click **"Create new secret key"**.
  4. Copy and save the key securely — it won’t be shown again.

> 💡 Make sure you have an active billing account or free-tier credits.

## 2.4 GitHub Token Key
- **Link:** [GitHub Token Settings](https://github.com/settings/tokens)
- **Steps:**
  1. Sign in to your [GitHub account](https://github.com/).
  2. Click **"Fine-grained tokens"** or **"Tokens (classic)"**, depending on your needs.
  3. Click **"Generate new token"**.
  4. Set required **scopes** (e.g., `repo`, `read:org`).
  5. Click **"Generate token"** and copy it securely.

> 🔒 Treat API keys and tokens as secrets. Never hardcode them or expose them publicly.

# 3. Running Evaluation Notebooks
You need to prepare your working environment by installing the dependencies and correctly setting up the configuration file. Below you can find details on how to do that.

## 3.1 Set up prerequisites
We use conda and pixi for managing the dependencies of the project. To install:
```bash
# install miniforge
curl -L -O "https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-$(uname)-$(uname -m).sh"
bash Miniforge3-$(uname)-$(uname -m).sh
# install pixi
curl -fsSL https://pixi.sh/install.sh | bash
```

The commands above are for unix-like systems (Linux, MacOS). For Windows, you can download the Miniforge installer from [here](https://github.com/conda-forge/miniforge) and pixi from [here](https://pixi.sh).

## 3.2 Install dependencies
To install the dependencies and activate the environment, run the following command:
```bash
pixi install  # install dependencies
pixi shell  # start a shell with the dependencies installed
```

## 3.3 Launch Jupyter Notebook
To launch the Jupyter notebook, run the following command:
```bash
pixi run jupyter notebook
```

# 4. Personalization Information

## 4.1. Project Domain

Research finds that different project domains utilize different writing styles and prioritize different types of content in their release notes. To take this into account, SmartNote requires users to specify their project domain. Below you can find a description of each project domain, its writing style and the type of content that would primarily be focused on in the release note.

| # | Project Domain         | Description                                                                                                                                              | Writing Style | Content                                                                                                      |
|---|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|---------------|--------------------------------------------------------------------------------------------------------------|
| 0 | Application Software   | Software that offers end-users with functionality, such as browsers and text editors.                                                                    | Expository    | Prioritize performance, document changes, and dependency/environment information for ease of installation and upgrade for end users. Users of some Application Software projects may not be developers, thus technical details are not necessary and even cause confusion. |
| 1 | Libraries & Frameworks | Software that provides a collection of reusable functionalities to facilitate software development in specific domains such as Web and machine learning. | Expository    | Prioritize breaking changes and document changes to facilitate the usage of downstream projects.                                  |
| 2 | System Software        | Software that offers basic services and infrastructure to other software, e.g., operating systems, servers, and databases.                               | Persuasive    | Prioritize breaking changes and security changes but provide a more comprehensive introduction of various categories to serve a variety of audiences.            |
| 3 | Software Tool          | Software that facilitates developers with universal software development tasks, like IDEs and compilers.                                                 | Descriptive   | Prioritize performance, breaking changes, enhancements, and security to strengthen developers' confidence when they develop software with it. Most users of Software Tools projects are developers, who benefit from technical details. |

### 4.2. Writing Styles
The writing style determines how the content of the release note document is worded (i.e., use commit/pr title or summarize the commit using the LLM). 

| #  | Writing Style | Description                                                                                                                                                                                                                                   |
|----|---------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -1 | Automatic     | The writing style will automatically be determined by the project domain. See the project domain section for more details on which project domain utilizes which writing style.                                         |
| 0  | Persuasive    | In addition to presenting the content of related commits/PRs/issues, provide additional information to help developers understand the changes, such as the rationale behind the changes, the impact of the changes, and guides for upgrading. |
| 1  | Descriptive   | Rephrase the content of change-related commits/PRs/issues to increase the readability and summarize the content of similar commits/PRs/issues.                                                                                                |
| 2  | Expository    | Directly list the content (usually title) of change-related commits/PRs/issues.                                                                                                                                                               |

## 4.3. List Structure Type (Organization Strategies)
Research finds that 2/3rds of release notes are formatted as hierarchical lists and finds that organizing by change type is more common across all domains. Therefore, SmartNote is pre-configured to format as a heirarchical list which organises by change type. However, users can change this setting to match their preferences or specific needs.

| # | Strategy        | Description                                                                                                  |
|---|-----------------|--------------------------------------------------------------------------------------------------------------|
| 0 | Plain List      | All changes are presented as a plain list.                                                                   |
| 1 | Change Type     | Changes are organized based on their types of content, e.g., New Features, Fixed Bugs, and Breaking Changes. |
| 2 | Affected Module | Changes are grouped based on the modules they affect.                                                        |
| 3 | Change Priority | Changes are ranked based on their importance perceived by RN producers.                                      |

## 4.4. Minimum Significance
The minimum significance threshold is used to determine which commits to remove from the output. The signiicance of each commit is calculated using a classification model that has been trained on commits using the Conventional Commit standard. The significance value is a float which ranges between 0 and 1. Important commits are ranked 1, while insignificant commits are ranked 0. 

Setting the minimum significance threshold to 0 means no commits will be removed. By default, SmartNote is configured wit a minimum significance threshold of 0.15.

## 4.5. Commit Grouping
This configuration setting determines whether commits are grouped by their associated pull request. Grouping commits helps improve readability by making the release note concise. By default SmartNote is configured to group commits, however, you can choose to disable this. 