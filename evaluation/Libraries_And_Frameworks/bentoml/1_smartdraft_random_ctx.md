# v1.3.2
## ✨ feat
- Added a reload option to the start-http-server command in the CLI, enabling the server to reload on code changes. [#4916](https://github.com/bentoml/bentoml/pull/4916) 

## 🐛 fix
- Fixed resource type definitions to allow CPU and memory values as strings, integers, or floats, enhancing flexibility. Includes automatic fixes from pre-commit.ci for code quality and consistency. [#4904](https://github.com/bentoml/bentoml/pull/4904) 
- Addressed issue where response is returned if tracer ID is null. Includes automatic fixes from pre-commit.ci. [#4899](https://github.com/bentoml/bentoml/pull/4899) 
- Fixed issue where metrics duration defined with min, max, and factor was not taking effect. [#4903](https://github.com/bentoml/bentoml/pull/4903) 
- Updated build process to preserve index URL options in the requirements file. [#4914](https://github.com/bentoml/bentoml/pull/4914) 
- Modified test logic to handle process termination more effectively. Introduced a subprocess timeout mechanism to ensure proper termination of processes exceeding the specified duration. Excluded certain tests from specific configurations to avoid known issues. [#4917](https://github.com/bentoml/bentoml/pull/4917) 

## ♻️ refactor
- The cloud context is now stored in the container, simplifying the codebase by eliminating the need to pass the context explicitly in various functions and methods. [#4907](https://github.com/bentoml/bentoml/pull/4907) 

## 📚 docs
- Updated documentation images. [#4901](https://github.com/bentoml/bentoml/pull/4901) 
- The Azure BYOC instructions now require sharing the `bcAdminSP.json` file through a secure channel. [#4905](https://github.com/bentoml/bentoml/pull/4905) 
- Updated documentation now details BentoML as a Python library for building online serving systems optimized for AI applications and model inference. [#4910](https://github.com/bentoml/bentoml/pull/4910) 
- The documentation for testing HTTP behavior of a BentoML Service now uses the `starlette.testclient` module to create a test client. This change simplifies sending HTTP requests and validating responses. The updated instructions and example code offer a clearer and more streamlined approach to testing. [#4915](https://github.com/bentoml/bentoml/pull/4915) 
- The documentation now includes a comprehensive guide on configuring and customizing default and custom metrics using Prometheus, integrating Prometheus for scraping metrics, and creating Grafana dashboards for visualization. [#4912](https://github.com/bentoml/bentoml/pull/4912) 
- Updated the CI status badge in the documentation. [#4918](https://github.com/bentoml/bentoml/pull/4918) 

## 🔧 chore
- Updated `pdm.lock`, removed `pdm.py312.lock`, and modified `pyproject.toml` to include a new dependency. Updated test cases for compatibility with the new SDK. [#4911](https://github.com/bentoml/bentoml/pull/4911) 

## 👷 ci
- Pre-commit autoupdate with several dependency updates. Improved code by using `isinstance` for better type checking. [#4897](https://github.com/bentoml/bentoml/pull/4897)
