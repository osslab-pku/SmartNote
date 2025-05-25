# Release Notes for Version 8.1.0

## New Features
- **SQL Enhancements:**
  - Introduced `read_parquet()` function to enable querying of Parquet files directly from the server's file system. [#4460]
  - Added `SAMPLE BY FROM-TO` syntax for specifying result ranges in SQL queries. This feature allows for more precise control over query output ranges and supports value fills. [#4733]

- **Core Improvements:**
  - Implemented a trigger file mechanism to initiate snapshot recovery, simplifying the recovery process. [#4807]

## Performance Improvements
- **SQL Performance:**
  - Enhanced the performance of the `like/ilike` operator on symbol columns, resulting in faster query execution. [#4794]
  - Improved the `regexp_replace(varchar)` function for simple patterns, reducing execution time. [#4668]

- **Core Performance:**
  - Achieved a 50-100% speedup in writing small transactions, significantly increasing throughput. [#4793]

## Bug Fixes
- **SQL Fixes:**
  - Resolved issues with incorrect results being returned from parallel `WHERE` and `GROUP BY` operations for certain function keys. [#4796]
  - Fixed a bug where some window functions might double count rows under specific conditions. [#4804]
  - Addressed spurious "unsupported operation" errors in SQL queries. [#4632]

- **Core Fixes:**
  - Prevented table suspension under memory pressure by implementing a retry mechanism with reduced parallelism. [#4745]

- **UI Fixes:**
  - Fixed issues with Charts when used in conjunction with OAuth, ensuring proper functionality. [#4813]

## Documentation Updates
- Updated documentation to reflect changes in the `read_parquet()` function and the new `SAMPLE BY FROM-TO` syntax. [#4460, #4733]
- Revised examples in the ILP documentation to use the `trades` table for better clarity. [#4764]

## Build and CI Enhancements
- Added Red Hat UBI Docker build to comply with Red Hat certification requirements. [#4783]
- Introduced Java code formatting checks using IntelliJ in the CI pipeline to ensure consistent code style. [#4774]

## Miscellaneous
- Various code quality improvements and refactoring for better maintainability and readability.
- Updated the README to better reflect the use cases and capabilities of QuestDB. [#4784]

This release brings significant improvements in performance, new features for SQL querying, and important bug fixes, enhancing the overall stability and functionality of QuestDB.