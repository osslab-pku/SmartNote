# Release Notes for Version v1.16.0

## Release Date
August 15th, 2024

## New Features
- **Memoization**: Introduced the `memoize` function to cache the results of function calls based on the arguments provided. This enhances performance by avoiding redundant calculations.
- **Array Enhancements**:
  - Added `find` and `findIndex` functions to locate elements in arrays based on specified conditions.
  - Implemented `indexOf` to find the index of the first occurrence of a value in an array, with support for `NaN`.
  - Introduced `sortBy` for sorting arrays of objects based on specified criteria.
- **Object Utilities**:
  - Added `has` to check if a given path exists within an object.
  - Implemented `matchesProperty` to create functions that check if a given source object matches a specific property value.
- **String Utilities**:
  - Added `padEnd` to pad the end of a string with a given character until it reaches the specified length.
  - Introduced `isString` to check if a given value is a string.
- **Function Utilities**:
  - Implemented `partial` and `partialRight` for partial application of functions.
  - Added `rest` to create functions that transform arguments by grouping them into an array starting from a specified index.

## Bug Fixes
- Fixed missing export for `toMerged` function.
- Corrected type export for `MemoizeCache`.

## Documentation
- Updated and clarified documentation for new and existing functions, including `find`, `findIndex`, `has`, `partial`, `partialRight`, `sortBy`, `isString`, `rest`, and `padEnd`.
- Improved compatibility documentation and added missing links.

## Code Quality
- Applied Prettier for consistent code formatting.
- Fixed ESLint errors across the codebase.

## Performance
- Updated bundle size benchmarks and moved some files to a dedicated performance folder for better organization.

## Miscellaneous
- Removed broken links from documentation.
- Updated internal utility functions and added new ones like `compareValues` for consistent value comparison.

This release brings significant enhancements to the `es-toolkit` library, focusing on performance improvements, new utility functions, and better documentation. The introduction of memoization and new array and object utilities will help developers write more efficient and readable code.