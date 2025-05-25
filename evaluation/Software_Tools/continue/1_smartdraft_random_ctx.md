# v0.8.45-vscode
## ✨ feat
- Improved indexing performance and codebase searches by accurately searching file names and paths. Added support for Llama 3.1 and gpt-4o-mini. [#1750](https://github.com/continuedev/continue/pull/1750) 
- The update introduces a new model dropdown and control plane, adds documentation and schema for the "OS" provider, and improves context rendering. It includes caching imports for autocomplete, adding stop tokens to prompts, and updating onboarding with an embeddings model. Enhances the user interface with new styling improvements, adds a free trial card to onboarding, and provides a toast notification for configuration updates. Includes several small fixes and improvements to the overall user experience. [#1931](https://github.com/continuedev/continue/pull/1931) 

## 🐛 fix
- The update introduces a new model dropdown and control plane client, along with documentation and schema for the "OS" provider. It improves GUI rendering, adds caching for autocomplete imports, and includes a toast notification for configuration updates. Enhancements include an embeddings model for onboarding, updated styles, a free trial card, new model styling improvements, labels for the "Add docs" dialog, and several small fixes to improve performance and user experience. [#1930](https://github.com/continuedev/continue/pull/1930)

## 🔧 chore
- Added support for .prompt files and a new onboarding experience. Improved indexing reliability and testing. Fixed autocomplete text positioning and timing. [823dcd6](https://github.com/continuedev/continue/commit/823dcd6e66180ed74039d335980a8bc253239606) 
- Improvements include partial autocomplete acceptance, an autocomplete status bar spinner, and a fix for duplicate completions. [2eafdff](https://github.com/continuedev/continue/commit/2eafdff54b1a77c6d403fa26a64c6793d7a4dfb9) 
- Updated version number in the package configuration file. [029dc5a](https://github.com/continuedev/continue/commit/029dc5aceac1df7cbde5f955f693a86c647eab61) 
- Updates include a new model dropdown, control plane client, enhanced onboarding, and updated documentation. Introduces toast notification for configuration updates, improved UI styling, and labels in the "Add docs" dialog. Adds support for Node.js versions below 20 for streaming response handling, along with various small fixes and enhancements. [#1934](https://github.com/continuedev/continue/pull/1934) 
- Support for new models, significant indexing performance improvements, and accuracy enhancements. Fixes for documentation indexing and management, and improvements to the embeddings provider. [5309067](https://github.com/continuedev/continue/commit/5309067ac0e55ac1f464c1b24b8facf2d06896bd) 
- Commented out the pull request trigger and steps for running extension tests on different operating systems in the CI configuration. Fixed a bug in the `WorkOsAuthProvider` class to correctly calculate the session expiration timeout. [9bf3fac](https://github.com/continuedev/continue/commit/9bf3facee0f722ea082054698f8d74fa4c5168ad) 

## 📚 docs
- Updated recommended models, including DeepSeek Coder versions and GPU requirements. [7b99524](https://github.com/continuedev/continue/commit/7b99524d16999af78a00b198724d3beb45334ff1) 
- Updated documentation links to reflect the new structure. [#1812](https://github.com/continuedev/continue/pull/1812) 
- Added a link to the Autocomplete (beta) page in the Features section. [#1879](https://github.com/continuedev/continue/pull/1879) 
- Updated the copyright year in the extension READMEs. [#1856](https://github.com/continuedev/continue/pull/1856)
