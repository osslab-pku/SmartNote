# v1.3.2
## ♻️ refactor
- The cloud context is now stored in the container, simplifying the codebase by eliminating the need to pass it explicitly in functions and methods. This change affects files related to cloud deployment, configuration, and CLI commands, ensuring a more streamlined and maintainable approach. [#4907](https://github.com/bentoml/bentoml/pull/4907) <span style='color:grey;'>(significance=0.03)</span>

## ✨ feat
- Added a reload option to the start-http-server command in the CLI, enabling the server to reload on code changes. [#4916](https://github.com/bentoml/bentoml/pull/4916) <span style='color:grey;'>(significance=0.05)</span>

## 🐛 fix
- Updated the prompt text for user confirmation to open a URL in the browser to request a 'Y' or 'N' input instead of just pressing Enter. [#4898](https://github.com/bentoml/bentoml/pull/4898) <span style='color:grey;'>(significance=0.03)</span>
- Fixed resource type definitions to enhance CPU and memory specifications. CPU and memory values can now be strings, integers, or floats, with detailed documentation on interpretation. [#4904](https://github.com/bentoml/bentoml/pull/4904) <span style='color:grey;'>(significance=0.02)</span>
- Addresses an issue where the response is returned directly if the tracer ID is null, ensuring proper error handling. [#4899](https://github.com/bentoml/bentoml/pull/4899) <span style='color:grey;'>(significance=0.03)</span>
- Fixed issue where metrics duration defined with min, max, and factor was not taking effect. [#4903](https://github.com/bentoml/bentoml/pull/4903) <span style='color:grey;'>(significance=0.01)</span>
- Updated the build process to preserve index URL options in requirements.txt. [#4914](https://github.com/bentoml/bentoml/pull/4914) <span style='color:grey;'>(significance=0.02)</span>
- Modified the test logic to handle process termination more effectively by introducing a subprocess timeout mechanism. Ensured processes are terminated if they exceed the specified duration. Excluded certain tests from specific configurations to avoid known issues. [#4917](https://github.com/bentoml/bentoml/pull/4917) <span style='color:grey;'>(significance=0.01)</span>

## 📚 docs
- Updated documentation images. [#4901](https://github.com/bentoml/bentoml/pull/4901) <span style='color:grey;'>(significance=0.02)</span>
- Updated Azure BYOC instructions: Share the `bcAdminSP.json` file through a secure channel instead of the `account_info.json` file. [#4905](https://github.com/bentoml/bentoml/pull/4905) <span style='color:grey;'>(significance=0.01)</span>
- Updated documentation and codebase: improved README and service files, enhanced BentoML description and usage instructions, updated service implementation for better performance, refined project configuration, removed outdated image, and made minor adjustments to project metadata. [#4906](https://github.com/bentoml/bentoml/pull/4906) <span style='color:grey;'>(significance=0.00)</span>
- Updated documentation provides a clearer description of BentoML, emphasizing it as a Python library for building online serving systems optimized for AI applications and model inference. Highlights include support for various model formats, custom Python code, and key primitives for serving optimizations, task queues, batching, multi-model chains, distributed orchestration, and multi-GPU serving. [#4910](https://github.com/bentoml/bentoml/pull/4910) <span style='color:grey;'>(significance=0.01)</span>
- Updated index.rst to remove a redundant section duplicating the "Deploy custom models with BentoML" entry. [#4913](https://github.com/bentoml/bentoml/pull/4913) <span style='color:grey;'>(significance=0.01)</span>
- The documentation for testing HTTP behavior of a BentoML Service now uses the `starlette.testclient` module to create a test client. This change simplifies sending HTTP requests and validating responses. The updated instructions and example code offer a clearer and more streamlined approach to testing. [#4915](https://github.com/bentoml/bentoml/pull/4915) <span style='color:grey;'>(significance=0.01)</span>
- The documentation now includes a comprehensive guide on metrics, detailing how to configure default metrics, create custom metrics, and integrate with Prometheus and Grafana for enhanced observability. This update provides users with the tools and instructions to monitor and analyze the performance of their BentoML services effectively. [#4912](https://github.com/bentoml/bentoml/pull/4912) <span style='color:grey;'>(significance=0.01)</span>
- Updated the CI status badge in the documentation. [#4918](https://github.com/bentoml/bentoml/pull/4918) <span style='color:grey;'>(significance=0.02)</span>

## 👷 ci
- Pre-commit autoupdate with several dependency updates. Improved code by using `isinstance` for better type checking. [#4897](https://github.com/bentoml/bentoml/pull/4897) <span style='color:grey;'>(significance=0.01)</span>

## 🔧 chore
- Updates to the lock file, fixes for tests, and adjustments to new SDK tests. [#4911](https://github.com/bentoml/bentoml/pull/4911) <span style='color:grey;'>(significance=0.01)</span>