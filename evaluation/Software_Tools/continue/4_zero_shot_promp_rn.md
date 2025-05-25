# Release Notes for v0.8.45-vscode

## New Features
- **Llama 3.1 and GPT-4o-mini Support**: Added support for the latest Llama 3.1 models and GPT-4o-mini, enhancing the range of available models for users.
- **WatsonX+Granite Models**: Integration with WatsonX+Granite models, expanding the model provider options.
- **Quick Actions CodeLens**: Introduced Quick Actions using CodeLens to streamline common tasks like adding docstrings directly from the code editor.
- **DeepSeek API FIM Support**: Added support for DeepSeek API FIM, improving functionality for specific use cases.

## Improvements
- **Indexing Performance**: Significant enhancements to indexing performance, reducing the time taken for indexing large codebases.
- **@codebase Quality**: Improved the accuracy of @codebase by more effectively searching over file names and paths.
- **Autocomplete Enhancements**: Updated the autocomplete feature with better model recommendations and improved UX for text areas.
- **Control Plane Settings UX**: Enhanced user experience for control plane settings, making it more intuitive to configure.

## Bug Fixes
- **Code Snippets**: Fixed an issue where code snippets were missing due to uncaught exceptions in MiniSearch.
- **SQLite WAL Mode**: Enabled Write-Ahead Logging (WAL) mode for SQLite to improve concurrency and stability.
- **File Indexing**: Resolved issues with file indexing in large workspaces by chunking segments of the workspace.
- **UI Fixes**: Addressed various UI issues, including layout alignment and scroll issues with code blocks.

## Documentation
- **Updated Model Provider Docs**: Added new documentation for model providers, including Azure, DeepSeek, and WatsonX.
- **Prompt Files Library**: Introduced a library of example prompt files to help users get started with custom prompts.

## Miscellaneous
- **Telemetry Enhancements**: Added telemetry for various features to improve tracking and analytics.
- **Codebase Re-index Command**: Added a command to force re-index the codebase, ensuring up-to-date indexing.

This release brings a host of new features, improvements, and bug fixes to enhance the user experience and expand the capabilities of the Continue extension for VS Code.