# v1.3.2
## 🐛 fix
- Updated the prompt for opening a URL in the browser to request 'Y' or 'N' input instead of just pressing Enter. [#4898](https://github.com/bentoml/bentoml/pull/4898) <span style='color:grey;'>(significance=0.03)</span>
- Improved error handling for null tracer ID, ensuring a direct return response. [#4899](https://github.com/bentoml/bentoml/pull/4899) <span style='color:grey;'>(significance=0.03)</span>
- Fixed resource type definitions to allow integer, float, and string inputs for CPU and memory specifications, enhancing accuracy and user-friendliness. [#4904](https://github.com/bentoml/bentoml/pull/4904) <span style='color:grey;'>(significance=0.02)</span>
- The build process now preserves index URL options in requirements.txt. [#4914](https://github.com/bentoml/bentoml/pull/4914) <span style='color:grey;'>(significance=0.02)</span>
- Fixed issue where metrics duration defined with min, max, and factor was not taking effect. [#4903](https://github.com/bentoml/bentoml/pull/4903) <span style='color:grey;'>(significance=0.01)</span>
- Modified the test logic to handle process termination more robustly and excluded certain tests from running on Python 3.12 to avoid compatibility issues. [#4917](https://github.com/bentoml/bentoml/pull/4917) <span style='color:grey;'>(significance=0.01)</span>

## ✨ feat
- Added a reload option to the start-http-server command in the CLI for automatic server restart on code changes. [#4916](https://github.com/bentoml/bentoml/pull/4916) <span style='color:grey;'>(significance=0.05)</span>

## ♻️ refactor
- Refactored code to store cloud context in the container, eliminating the need to pass it explicitly in function calls and class methods. [#4907](https://github.com/bentoml/bentoml/pull/4907) <span style='color:grey;'>(significance=0.03)</span>

## 📚 docs
- Updated documentation images. [#4901](https://github.com/bentoml/bentoml/pull/4901) <span style='color:grey;'>(significance=0.02)</span>
- Updated the CI status badge in the documentation. [#4918](https://github.com/bentoml/bentoml/pull/4918) <span style='color:grey;'>(significance=0.02)</span>
- Updated Azure BYOC instructions to streamline sharing the service principal information with the BentoML team. Now specifies sharing the `bcAdminSP.json` file through a secure channel. [#4905](https://github.com/bentoml/bentoml/pull/4905) <span style='color:grey;'>(significance=0.01)</span>
- Updated documentation describes BentoML as a Python library for building online serving systems optimized for AI applications and model inference. Highlights include support for any model format/runtime, custom Python code, serving optimizations, task queues, batching, multi-model chains, distributed orchestration, and multi-GPU serving. [#4910](https://github.com/bentoml/bentoml/pull/4910) <span style='color:grey;'>(significance=0.01)</span>
- Updated index.rst documentation to remove redundant entries on deploying custom models with BentoML. [#4913](https://github.com/bentoml/bentoml/pull/4913) <span style='color:grey;'>(significance=0.01)</span>
- The documentation for HTTP behavior testing now uses the `starlette.testclient` module. This simplifies creating a test client for sending HTTP requests to a BentoML Service. Example code and instructions have been revised for a more streamlined approach to testing HTTP endpoints. [#4915](https://github.com/bentoml/bentoml/pull/4915) <span style='color:grey;'>(significance=0.01)</span>
- New metrics documentation added with detailed instructions on configuring and customizing metrics in BentoML. Includes guidance on using Prometheus for scraping metrics and creating Grafana dashboards for visualization. Introduces custom metrics support and examples for defining and using metrics like Counter, Histogram, Summary, and Gauge within BentoML services. [#4912](https://github.com/bentoml/bentoml/pull/4912) <span style='color:grey;'>(significance=0.01)</span>
- Updated README and documentation to reflect latest project changes. Improvements to description, installation instructions, and example service code. Removed or replaced outdated images and references. [#4906](https://github.com/bentoml/bentoml/pull/4906) <span style='color:grey;'>(significance=0.00)</span>

## 👷 ci
- Pre-commit configuration updated and a check modified to use `isinstance` for better type checking. [#4897](https://github.com/bentoml/bentoml/pull/4897) <span style='color:grey;'>(significance=0.01)</span>

## 🔧 chore
- Updated project configuration and test files: removed lockfile settings for Python 3.12, modified test cases for list inputs, and updated dependencies. [#4911](https://github.com/bentoml/bentoml/pull/4911) <span style='color:grey;'>(significance=0.01)</span>