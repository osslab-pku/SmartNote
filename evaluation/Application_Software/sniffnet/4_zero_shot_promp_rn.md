# Release Notes for v1.3.1

## Overview
The v1.3.1 release of Sniffnet brings a host of improvements, new features, and updates to existing functionalities. This release focuses on enhancing user experience with new keyboard shortcuts, improved thumbnail mode, and expanded support for IPinfo databases. Additionally, several translations have been updated to ensure better localization support.

## New Features and Improvements
- **Thumbnail Mode Enhancements**: 
  - Fixed an issue where users could not exit thumbnail mode on Linux systems.
  - Introduced a keyboard shortcut (`Ctrl + T`) to toggle thumbnail mode.
  - Improved the network hosts list in thumbnail mode to prevent duplicate entries.

- **Keyboard Shortcuts**:
  - Added shortcuts to change zoom levels, enhancing navigation and accessibility.
  - Increased the range of selectable zoom values for better user control.

- **IPinfo Database Support**:
  - Added support for IPinfo ASN and Country databases, allowing users to import and utilize these databases seamlessly.

## Translations
- Updated translations for several languages to align with the v1.3 release:
  - **French**: Updated translations for better accuracy and consistency.
  - **German**: Added new translations and adjusted existing ones.
  - **Russian**: Added version 3 translations and fixed errors in previous versions.
  - **Polish**: Improved translations for natural language flow.
  - **Romanian**: Updated translations to reflect the latest changes.
  - **Japanese**: Added new translations, with some characters pending due to font limitations.
  - **Uzbek**: Updated translations to match the latest version.

## Dependency Updates
- Bumped several dependencies to their latest versions for improved performance and security:
  - `rstest` updated from 0.18.2 to 0.21.0.
  - `serde` updated from 1.0.197 to 1.0.204.
  - `rodio` updated from 0.18.0 to 0.19.0.
  - `pcap` updated from 1.3.0 to 2.0.0.
  - `chrono` updated from 0.4.37 to 0.4.38.
  - `etherparse` updated from 0.14.3 to 0.15.0.
  - `rustls` updated from 0.22.3 to 0.22.4.
  - `serial_test` updated from 3.0.0 to 3.1.0.
  - `toml` updated from 0.8.12 to 0.8.15.

## Bug Fixes
- Resolved an issue with the `etherparse` library that caused build errors.
- Fixed clippy lints and optimized imports for cleaner code.

## Documentation and Contributors
- Added new contributors for translations and ideas, acknowledging their valuable input.
- Updated the `SECURITY.md` and `README.md` to reflect the latest changes and installation instructions.

## Miscellaneous
- Added a new sample theme: `sniffnet_rebrand.toml`.
- Optimized images using ImgBot to reduce file sizes and improve loading times.

This release is a testament to the ongoing commitment to improving Sniffnet's functionality and user experience. We thank all contributors for their efforts and look forward to more enhancements in future releases.