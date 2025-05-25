# Release Notes for UmbrelOS 1.2.0

## New Features
- **IP Address Display**: Users can now view the IP addresses of their device directly in the Settings, enhancing network management and troubleshooting capabilities.
- **Automatic Translation Management**: A new GitHub action has been introduced to automatically manage translations. This includes removing unused keys, checking for missing variables, generating missing translations, and sorting all locale files.

## Improvements
- **Translation Updates**: Translations have been sorted alphabetically, and missing translations have been added, including a new Portuguese translation for the terminal.
- **UI Enhancements**: Console logs have been removed, and Prettier has been run on the UI codebase to ensure consistent code formatting.
- **Community App Stores**: Users can now add community app stores, allowing them to install apps not available in the official Umbrel App Store. This feature also facilitates testing beta versions of apps.

## Bug Fixes
- **Translation Cleanup**: Unused translations have been removed to streamline the codebase and improve performance.
- **Refetch Updates**: The system now refetches the latest updates when there is a change in the channel, ensuring users have the most current information.

## Technical Changes
- **Dependencies**: Added `fast-glob` and `openai` as new dependencies in the `package.json` for improved file handling and translation generation.
- **GitHub Actions**: A new workflow file `update-translations-in-pr.yml` has been added to automate translation updates in pull requests.

## Miscellaneous
- **Version Update**: The version has been updated from 1.2.0-beta.2 to 1.2.0, marking the transition from beta to a stable release.
- **Code Cleanup**: Various console logs have been removed from the codebase to clean up the output and improve performance.

This release focuses on enhancing user experience with new features, improving existing functionalities, and ensuring the system is up-to-date with the latest translations and network information.