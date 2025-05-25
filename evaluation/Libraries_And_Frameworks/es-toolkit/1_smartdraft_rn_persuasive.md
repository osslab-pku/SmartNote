# v1.16.0
## ♻️ refactor
- Refactored the internal function for comparing values to ensure consistency across sorting methods. Fixed type errors and updated documentation accordingly. [#382](https://github.com/toss/es-toolkit/pull/382) <span style='color:grey;'>(significance=0.33)</span>

## ✨ feat
- Implemented the `indexOf` function, similar to `Array.prototype.indexOf` but with support for finding `NaN` values. Includes comprehensive tests and updated documentation. [#378](https://github.com/toss/es-toolkit/pull/378) <span style='color:grey;'>(significance=0.42)</span>
- Added memoization feature for caching function results based on arguments. Supports custom cache implementations and resolver functions for flexible, efficient executions. Comprehensive documentation and tests included. [#208](https://github.com/toss/es-toolkit/pull/208) <span style='color:grey;'>(significance=0.35)</span>
- Implemented a new `sortBy` function for sorting an array of objects by specified keys or iteratees in ascending order. Supports mixed iteratees (keys and functions). Added documentation, examples, performance benchmarks, and tests for reliability and efficiency. [#381](https://github.com/toss/es-toolkit/pull/381) <span style='color:grey;'>(significance=0.32)</span> [d4037c7](https://github.com/toss/es-toolkit/commit/d4037c755c5498b0b646e3738eb96d7944295742) <span style='color:grey;'>(significance=0.31)</span>
- Introduced a `padEnd` function that pads the end of a string with a specified character until it reaches a given length, similar to lodash's `padEnd`. Includes comprehensive documentation and tests. [#380](https://github.com/toss/es-toolkit/pull/380) <span style='color:grey;'>(significance=0.26)</span>
- New functions `partial` and `partialRight` enable partial application of arguments to functions, supporting placeholders without altering `this` binding. Comprehensive documentation and tests ensure proper functionality and usage examples. [#368](https://github.com/toss/es-toolkit/pull/368) <span style='color:grey;'>(significance=0.26)</span>

## 🐛 fix
- Fixed type export for MemoizeCache. [aef394d](https://github.com/toss/es-toolkit/commit/aef394d8c4b4a8eb71002dd8c2897f726cefc510) <span style='color:grey;'>(significance=0.27)</span>

## 📚 docs
- The `findIndex` function is now supported. [c639dd7](https://github.com/toss/es-toolkit/commit/c639dd7209977140cf184d281d1ebdf31fb734df) <span style='color:grey;'>(significance=0.50)</span>
- Improved documentation for the `rest` function. It now includes detailed descriptions, parameter explanations, return values, and examples in multiple languages. [98af4a3](https://github.com/toss/es-toolkit/commit/98af4a3a114c5e0db118db96ac352e3ad5b93341) <span style='color:grey;'>(significance=0.29)</span>
- Documentation for `isString` function added. [8310cd9](https://github.com/toss/es-toolkit/commit/8310cd9d5d0898b9cb53761c25fb6a7097d1ab5f) <span style='color:grey;'>(significance=0.28)</span>
- Documentation for `find` function updated. [f71ff9e](https://github.com/toss/es-toolkit/commit/f71ff9e511ef98cf854abc28f16a0c6ae8f727b5) <span style='color:grey;'>(significance=0.27)</span>
- Documentation for the `indexOf` function added, detailing its usage and behavior. [418183b](https://github.com/toss/es-toolkit/commit/418183b0aa167aabaca95fa2221deac68fb728dd) <span style='color:grey;'>(significance=0.27)</span>
- Documentation for `find` and `findIndex` methods added. [2d96265](https://github.com/toss/es-toolkit/commit/2d96265951562d80a3d148895519c4cdcb23bb1f) <span style='color:grey;'>(significance=0.26)</span>
- Updated `has` function signature documentation to include missing backticks for proper formatting in English and Simplified Chinese versions. [da091c4](https://github.com/toss/es-toolkit/commit/da091c49d8988ee0ec2544c7cc7f38c39419785b) <span style='color:grey;'>(significance=0.26)</span>

## 🎨 style
- Reformatted codebase to adhere to Prettier's style guidelines for consistent code formatting. [be4162d](https://github.com/toss/es-toolkit/commit/be4162dc19003c7accde6c051edc0f85e3b72d76) <span style='color:grey;'>(significance=0.26)</span>