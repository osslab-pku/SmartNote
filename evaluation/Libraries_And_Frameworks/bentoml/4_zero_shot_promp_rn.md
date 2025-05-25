# Release Notes for Version 1.3.2

## Overview
This release includes a variety of improvements, bug fixes, and documentation updates. Key highlights include enhancements to the CLI, updates to the documentation, and several bug fixes to improve the stability and performance of the system.

## New Features
- **CLI Enhancement**: Added a `--reload` option for the `start-http-server` command, allowing the server to automatically reload when code changes are detected. [#4916]

## Bug Fixes
- **Metrics Configuration**: Fixed an issue where custom duration histogram buckets defined via `@bentoml.service(metrics=...)` were not taking effect. [#4895]
- **Resource Type Fix**: Corrected the resource type handling to ensure proper configuration. [#4904]
- **Tracer ID Handling**: Fixed a bug where the response was not directly returned if the tracer ID was null. [#4899]
- **Build Process**: Ensured that index URL options are preserved in the `requirements.txt` file during the build process. [#4914]
- **Timeout Test Cases**: Addressed issues with timeout test cases to improve test reliability. [#4917]

## Documentation Updates
- **Metrics Documentation**: Added comprehensive documentation on configuring and using metrics within BentoML, including default metrics and custom metrics setup. [#4912]
- **Azure BYOC Instructions**: Updated the Azure BYOC (Bring Your Own Cloud) instructions for clarity and accuracy. [#4905]
- **General Documentation**: Various updates to improve clarity and accuracy across multiple documentation files, including updates to README.md and index.rst. [#4906, #4913, #4910]

## Refactoring
- **Cloud Context Management**: Refactored the code to store the cloud context into the container instead of passing it around, simplifying the codebase. [#4907]

## Continuous Integration
- **Pre-commit Updates**: Updated pre-commit hooks to the latest versions, ensuring code quality and consistency. [#4897]

## Other Changes
- **PDM Lock File**: Updated the `pdm.lock` file to reflect the latest dependencies and lock targets. [#4911]
- **CI Status Badge**: Updated the CI status badge in the README to reflect the current workflow status. [#4918]

This release focuses on enhancing the user experience through improved documentation, bug fixes, and new features that streamline the development and deployment process. We encourage all users to upgrade to this version to take advantage of these improvements.