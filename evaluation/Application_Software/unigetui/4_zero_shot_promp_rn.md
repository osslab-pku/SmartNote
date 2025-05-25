# Release Notes for Version 3.1.1

## Overview
This release marks the transition from the 3.1.1-beta3 to the stable 3.1.1 version. It includes a series of improvements, bug fixes, and optimizations aimed at enhancing the overall performance and usability of the application. The update also includes translation updates and code refactoring for better maintainability.

## Key Changes

### Bug Fixes
- **WinGet Local Source Parser**: Fixed and optimized the parser to prevent crashes and ensure accurate package management.
- **Package Manager Logs**: Resolved an issue where logs were not displaying correctly.
- **Local Packages**: Addressed duplication issues when reloading installed packages.
- **Widgets Server**: Fixed a crash issue related to the Widgets server.
- **Package Manager Name Display**: Corrected an issue where sources wouldn't show the Package Manager name.
- **Non-Sources Package Managers**: Fixed a crash when non-sources package managers had their sources loaded.

### Improvements
- **Close Buttons**: Enhanced the functionality and appearance of close buttons across the application.
- **WinGet Package Finding**: Improved the method by which WinGet locates packages, increasing efficiency and accuracy.
- **System Tray Notifications**: Disabled notifications when the System Tray is disabled, addressing user feedback.

### Code Quality
- **Refactoring**: Removed redundant code, such as unnecessary constructors, string interpolations, and semicolons, to streamline the codebase.
- **Warnings and Typos**: Fixed various warnings and typos across multiple projects to improve code quality and readability.
- **XML Comments**: Improved XML comments for better code documentation and understanding.

### Translations
- **Tolgee Updates**: Integrated the latest translations from Tolgee, ensuring the application is accessible to a broader audience.
- **Language Files**: Updated language files to reflect the latest translations and corrections.

### Miscellaneous
- **Build Script**: Updated the build script to accommodate recent changes and ensure smooth deployment.
- **Version Number**: Updated the version number to reflect the transition from beta to stable release.

## Contributors
Special thanks to all contributors, including Adam Stachowicz, Martí Climent, Saibamen, and the Tolgee Bot, for their efforts in making this release possible.

For a detailed list of changes, please refer to the commit history and pull requests associated with this release.