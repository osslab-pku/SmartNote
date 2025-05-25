# Release Notes for v4.6.2

## New Features
- **Reopen Last Closed Tab**: Introduced a new feature allowing users to reopen the last closed tab using the shortcut `Ctrl+Shift+T`. This enhancement improves user experience by providing a quick way to recover accidentally closed tabs. [PR #1963](https://github.com/beekeeper-studio/beekeeper-studio/pull/1963)

## Enhancements
- **Database Support Documentation**: Added a special table for supported databases, providing one page per supported database. This update enhances the documentation by offering detailed information about each supported database. [PR #2262](https://github.com/beekeeper-studio/beekeeper-studio/pull/2262)
- **Updated README Files**: The README files have been updated to reflect the current list of supported databases, ensuring users have the most accurate information. [PR #2272](https://github.com/beekeeper-studio/beekeeper-studio/pull/2272)

## Bug Fixes
- **Copying Values**: Fixed an issue where using `Ctrl+C` on the result table was copying incorrect values. The fix ensures that only the active query tab's result table is considered during the copy operation. [PR #2273](https://github.com/beekeeper-studio/beekeeper-studio/pull/2273)
- **Zero Input Handling**: Resolved a bug where zero input was being converted to null. This fix ensures that zero values are correctly handled and not misinterpreted as null. [PR #2286](https://github.com/beekeeper-studio/beekeeper-studio/pull/2286)
- **CSV Export Headers**: Addressed an issue where headers were missing in CSV exports by adding columns and total count to the query stream. This fix ensures that CSV exports include the necessary headers. [PR #2281](https://github.com/beekeeper-studio/beekeeper-studio/pull/2281)

## Dependency Updates
- **WebSocket Security Update**: Bumped the `ws` package from version 6.2.2 to 6.2.3 to incorporate security fixes and improvements. [PR #2263](https://github.com/beekeeper-studio/beekeeper-studio/pull/2263)

## Technical Improvements
- **Launcher Script**: The launcher script now defaults to `--no-sandbox` to address issues with certain Linux distributions disabling clone for non-root users. This change ensures better compatibility across different environments.
- **Workflow Enhancements**: Multiple updates and iterations were made to the GitHub Actions workflows to improve automation and integration processes.

This release focuses on enhancing user experience with new features and fixing critical bugs to ensure a smoother and more reliable application performance.