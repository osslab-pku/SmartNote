# Release Notes for v2.52.1

## Overview

This release includes several enhancements, bug fixes, and updates to dependencies and documentation. Key highlights include the addition of a new related software, improvements in HTTP request handling, and updates to the build process with Go 1.23.

## New Features

- **Related Software**: Added `github.com/johan-weitner/chezmoi-ui` to the list of related software. This is a web UI for managing a list of apps to seed/feed a Chezmoi setup. [Commit ca0d133]

## Bug Fixes

- **HTTP Requests**: Fixed the issue where the User-Agent header was not set correctly on all HTTP requests. The User-Agent is now set to `chezmoi.io/version`. This fix addresses issue #3900. [PR #3903]

- **Windows Permission Changes**: Resolved an issue where permission changes were not ignored in the `re-add` command on Windows. This fix addresses issue #3891. [PR #3893]

## Documentation Updates

- Added links to two new articles and a video to the documentation:
  - Articles: "Development Environment Setup with Chezmoi" and another unnamed article.
  - Video: "Automating Development Environments with Ansible & Chezmoi". [Commits 4843d55, 8e40c43]

## Build and Dependency Updates

- **Go Version**: Updated the build process to use Go 1.23. This update allows the use of new features available in Go 1.22 and later. [PR #3860]
- **Dependencies**: Updated various dependencies to their latest versions, including `github.com/1password/onepassword-sdk-go`, `github.com/Azure/azure-sdk-for-go`, and others. [Commit 9042768]
- **GitHub Actions**: Updated GitHub Actions workflows to align with the latest changes and improvements. [Commit b18b769]
- **GoReleaser**: Updated GoReleaser to version 2.2.0. [Commit 7f44957]

## Code Quality and Maintenance

- **Commit Hash Length**: Limited the commit hash length to seven characters in the website to improve readability. [PR #3894]
- **Code Refactoring**: Minor refactoring and cleanup in the codebase to improve maintainability and performance.

## Platform Support

- **OpenBSD**: Added support for the `riscv64` architecture in OpenBSD. [File Changes in `install-local-bin.sh` and `install.sh`]

## Conclusion

This release focuses on improving the robustness of HTTP requests, enhancing documentation, and updating the build process to leverage the latest Go features. Users are encouraged to update to this version to benefit from these improvements and fixes.