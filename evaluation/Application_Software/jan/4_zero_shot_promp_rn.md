# Release Notes for Version 0.5.2

## New Features
- **Time-Weighted Retrieval**: Introduced a new feature for time-weighted retrieval, enhancing the retrieval process with time-based relevance. This includes configuration options for the `timeWeightedVectorStore` and integration with the AssistantTool.
- **Claude 3.5 Sonnet**: Added support for the Claude 3.5 Sonnet model, expanding the range of available models.
- **Spell Check Configuration**: Added options to configure spell check for chat input, allowing users to enable or disable spell checking as needed.
- **Shortcut for App Logs**: Introduced a shortcut to access application logs directly from the system monitor, improving accessibility for troubleshooting.

## Improvements
- **Model Management**: Updated the model dropdown to prioritize showing downloaded models first in search results, enhancing user experience when managing models.
- **UI Enhancements**: 
  - Enabled right-click to show settings on thread items.
  - Added tooltips to message toolbar icons for better user guidance.
  - Improved the appearance and functionality of the modal troubleshooting interface.
- **Cortex Updates**: Bumped the Cortex version to 0.4.20, ensuring compatibility and performance improvements.

## Bug Fixes
- **UI and UX Fixes**:
  - Resolved issues with handling long words and thread titles without spaces, preventing UI elements from disappearing.
  - Fixed the model dropdown search to ensure it displays configured models correctly.
  - Corrected the error message display when the API key is not set up.
  - Addressed the issue where the thread title was not updating upon editing.
- **File System and Path Validation**: Implemented path validation to restrict file access to the Jan folder, enhancing security and stability.
- **Miscellaneous Fixes**: 
  - Fixed grammar issues across the application.
  - Resolved issues with missing keyboard shortcuts screen.

## Chores
- **Dependency Updates**: Upgraded `marked-katex-extension` to version 5.0.2.
- **Code Quality**: Various code refactoring and linting improvements to maintain code quality and readability.

## Technical Changes
- **API and Configuration**: Updated API routes and configurations to support new features and improvements.
- **File Changes**: Modified several core and web files to implement new features, fix bugs, and improve performance.

This release focuses on enhancing the user experience with new features, improving existing functionalities, and fixing critical bugs to ensure a smoother and more efficient workflow.