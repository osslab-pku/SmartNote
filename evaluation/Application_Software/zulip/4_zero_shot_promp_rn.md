# Release Notes for Zulip Server 9.1

## Overview

Zulip Server 9.1 introduces several enhancements, bug fixes, and documentation improvements to ensure a smoother user experience and more efficient system operations. This release focuses on improving upgrade processes, optimizing performance, and enhancing user interface elements.

## Key Changes

### Upgrade and Installation Improvements
- **OS Upgrade Documentation**: Enhanced documentation to guide users through upgrading from Ubuntu 20.04 to 22.04 before moving to Zulip 9.x. This includes clearer instructions and error messages to prevent common pitfalls during the upgrade process.
- **PostgreSQL Support**: Updated documentation to reflect supported PostgreSQL versions for the 9.x series, ensuring compatibility and stability.

### Performance Enhancements
- **Compression Optimization**: Adjusted the default gzip compression level in Nginx to improve web and mobile app loading times and reduce bandwidth usage.
- **Database Query Optimization**: Improved indexing for analytics queries and reduced database contention by optimizing how server statistics are reported.

### Bug Fixes
- **GitHub Integration**: Resolved an issue with duplicate notifications for pull request reviews due to GitHub's payload quirks.
- **Image Uploads**: Fixed a race condition that could cause uploaded images to display as perpetual loading spinners.
- **Video Previews**: Disabled controls on video previews in the lightbox to prevent unintended interactions.

### User Interface and Experience
- **Typeahead Overflow**: Addressed an issue where typeahead suggestions could overflow the window, ensuring they remain within visible boundaries.
- **Inbox UI**: Fixed synchronization issues with inbox row focus, preventing errors when messages are marked as read in another tab.
- **Message Previews**: Simplified the presentation of message previews to improve readability and consistency across different modes.

### Documentation and Developer Experience
- **Integration Documentation**: Updated Sentry and Semaphore integration docs to the new format, providing clearer setup instructions.
- **API Documentation**: Clarified event structure for moving channels, ensuring developers have accurate information for integration purposes.

### Miscellaneous
- **Translation Updates**: Synced translations from Transifex to ensure language support is up-to-date.
- **Code Refactoring**: Various internal code improvements and refactoring to enhance maintainability and performance.

## Conclusion

Zulip Server 9.1 is a robust update that addresses key areas of user experience, system performance, and upgrade processes. Users are encouraged to upgrade to this version to benefit from the latest improvements and fixes. For detailed upgrade instructions, please refer to the [Zulip upgrade documentation](https://zulip.readthedocs.io/en/latest/production/upgrade.html).