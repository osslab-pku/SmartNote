# v1.3.2
## ✨ feat
- Added a reload option to the start-http-server command in the CLI, enabling the server to reload on code changes. [#4916](https://github.com/bentoml/bentoml/pull/4916) <span style='color:grey;'>(significance=0.14)</span>

## 🐛 fix
- Fixed resource type definitions to allow CPU and memory requirements as strings, integers, or floats. CPU and memory values now default to cores and Gibibytes when specified as integers or floats. [#4904](https://github.com/bentoml/bentoml/pull/4904) <span style='color:grey;'>(significance=0.08)</span>
- Addressed issue where a response is returned if the tracer ID is null. Modified to handle missing "x-trace-id" header, ensuring appropriate error messages based on tracer ID presence. [#4899](https://github.com/bentoml/bentoml/pull/4899) <span style='color:grey;'>(significance=0.08)</span>
- Fixed an issue in the build process to preserve index URL options in the requirements.txt file. [#4914](https://github.com/bentoml/bentoml/pull/4914) <span style='color:grey;'>(significance=0.06)</span>
- Modified the test logic to handle process termination more effectively, introducing a subprocess timeout mechanism to ensure proper termination if processes exceed the specified duration. Excluded certain tests from specific configurations to avoid known issues. [#4917](https://github.com/bentoml/bentoml/pull/4917) <span style='color:grey;'>(significance=0.07)</span>
- Updated the `duration_buckets` function to correctly handle metrics duration defined with min, max, and factor, ensuring proper generation of exponential buckets. [#4903](https://github.com/bentoml/bentoml/pull/4903) <span style='color:grey;'>(significance=0.05)</span>

## ♻️ refactor
- The cloud context is now stored in the container, simplifying the codebase by eliminating the need to pass the context explicitly in various functions and methods. [#4907](https://github.com/bentoml/bentoml/pull/4907) <span style='color:grey;'>(significance=0.15)</span>

## 📚 docs
- The Azure BYOC instructions now require sharing the `bcAdminSP.json` file through a secure channel. [#4905](https://github.com/bentoml/bentoml/pull/4905) <span style='color:grey;'>(significance=0.08)</span>
- Updated documentation provides a clearer description of BentoML, emphasizing it as a Python library for building online serving systems optimized for AI applications and model inference. Highlights include support for various model formats, custom Python code, and key primitives for serving optimizations, task queues, batching, multi-model chains, distributed orchestration, and multi-GPU serving. [#4910](https://github.com/bentoml/bentoml/pull/4910) <span style='color:grey;'>(significance=0.08)</span>
- Updated documentation images. [#4901](https://github.com/bentoml/bentoml/pull/4901) <span style='color:grey;'>(significance=0.05)</span>
- Updated HTTP behavior test instructions to use `starlette.testclient`, simplifying the creation of a test client for sending HTTP requests to a BentoML Service. Revised example code and explanations for a more streamlined and accurate testing process. [#4915](https://github.com/bentoml/bentoml/pull/4915) <span style='color:grey;'>(significance=0.05)</span>
- Updated documentation includes a comprehensive guide on configuring and using metrics in BentoML. Instructions cover accessing default metrics, creating custom metrics, and integrating with Prometheus and Grafana for monitoring and visualization. The new metrics documentation replaces the previous metrics API reference, providing detailed examples and explanations for setting up and customizing metrics to gain insights into service performance. [#4912](https://github.com/bentoml/bentoml/pull/4912) <span style='color:grey;'>(significance=0.05)</span>
- Updated the CI status badge in the documentation. [#4918](https://github.com/bentoml/bentoml/pull/4918) <span style='color:grey;'>(significance=0.06)</span>

## 👷 ci
- Pre-commit configuration updated with newer dependency versions. Improved code readability and accuracy by using `isinstance` for type checks. [#4897](https://github.com/bentoml/bentoml/pull/4897) <span style='color:grey;'>(significance=0.09)</span>

## 🔧 chore
- Updated project configuration and test files: removed lockfile settings for Python 3.12, modified test cases to handle input as a list, and updated dependencies. [#4911](https://github.com/bentoml/bentoml/pull/4911) <span style='color:grey;'>(significance=0.07)</span>