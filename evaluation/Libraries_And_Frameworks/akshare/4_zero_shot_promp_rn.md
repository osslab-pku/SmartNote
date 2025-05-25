# Release Notes for Version 1.14.62

## Overview

This release focuses on documentation updates and a critical fix to the `stock_zt_pool_em` interface. Additionally, a new version tag has been added to reflect these changes.

## New Features

- **Version Update**: The version has been updated to 1.14.62 to incorporate the latest changes and fixes.

## Bug Fixes

- **`stock_zt_pool_em` Interface**: 
  - Fixed an issue where the interface would fail when attempting to retrieve data from a date too far in the past. The function now correctly returns an empty DataFrame if the data pool is empty, preventing errors and improving stability.

## Documentation

- **General Updates**: 
  - Updated various documentation files to reflect the latest changes and ensure accuracy. This includes updates to the changelog and other relevant documentation sections.

## Pull Requests Merged

- **PR #5133**: Addressed an error in `stock_ztb_em.py` when fetching data from dates too far in the past. The fix involves checking if the data pool is empty and returning an empty DataFrame if so.
- **PR #5135**: General development updates (details not specified).
- **PR #5132**: Updated documentation dates.
- **PR #5131**: General development updates (details not specified).

## File Changes

- **`akshare/__init__.py`**: Updated the version number to 1.14.62.
- **`akshare/stock_feature/stock_ztb_em.py`**: Added a condition to handle cases where the data pool is empty, returning an empty DataFrame.
- **`docs/changelog.md`**: Added an entry for version 1.14.62, detailing the fix to the `stock_zt_pool_em` interface.
- **`docs/data/stock/stock.md`**: Minor updates to ensure consistency and accuracy.
- **`docs/introduction.md`**: Updated the document's last updated date to reflect recent changes.

This release ensures improved functionality and documentation accuracy, enhancing the overall user experience.