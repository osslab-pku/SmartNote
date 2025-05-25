# v1.16.0
## ♻️ refactor
- Refactored `compareValues` function to handle ascending and descending order comparisons. Fixed type errors and updated documentation. [#382](https://github.com/toss/es-toolkit/pull/382) <span style='color:grey;'>(significance=0.33)</span>

## ✨ feat
- Implemented `partial` and `partialRight` functions for partial application of arguments. These methods support placeholders and do not alter the `this` binding. [#368](https://github.com/toss/es-toolkit/pull/368) <span style='color:grey;'>(significance=0.26)</span>
- Implemented the `indexOf` function in the `es-toolkit/compat` module, including comprehensive tests and documentation updates for compatibility and performance. [#378](https://github.com/toss/es-toolkit/pull/378) <span style='color:grey;'>(significance=0.42)</span>
- The `sortBy` function now allows sorting arrays of objects by specified criteria, supporting both object keys and custom iteratee functions for flexible, stable sorting. Added documentation, examples, and performance benchmarks for efficiency comparison with other libraries. [#381](https://github.com/toss/es-toolkit/pull/381) <span style='color:grey;'>(significance=0.32)</span> | [d4037c7](https://github.com/toss/es-toolkit/commit/d4037c755c5498b0b646e3738eb96d7944295742) <span style='color:grey;'>(significance=0.31)</span>
- Introduced `padEnd` function to pad the end of a string with a specified character until it reaches a given length. Part of the compatibility toolkit, similar to lodash. Comprehensive documentation and tests added. [#380](https://github.com/toss/es-toolkit/pull/380) <span style='color:grey;'>(significance=0.26)</span>
- Introduced a `memoize` function that caches results based on arguments, supporting custom cache implementations and resolver functions for flexible and efficient memoization. [#208](https://github.com/toss/es-toolkit/pull/208) <span style='color:grey;'>(significance=0.35)</span>

## 🐛 fix
- Fixed type export for MemoizeCache. [aef394d](https://github.com/toss/es-toolkit/commit/aef394d8c4b4a8eb71002dd8c2897f726cefc510) <span style='color:grey;'>(significance=0.27)</span>

## 🎨 style
- Formatted the codebase using Prettier for consistent spacing, indentation, and single quotes for strings. [be4162d](https://github.com/toss/es-toolkit/commit/be4162dc19003c7accde6c051edc0f85e3b72d76) <span style='color:grey;'>(significance=0.26)</span>

## 📚 docs
- Updated `find` function documentation for clarity and accuracy. [f71ff9e](https://github.com/toss/es-toolkit/commit/f71ff9e511ef98cf854abc28f16a0c6ae8f727b5) <span style='color:grey;'>(significance=0.27)</span>
- Documentation for the `indexOf` function added, detailing its usage and behavior. The function finds the index of the first occurrence of a value in an array, including `NaN`, using strict equality for comparisons. [418183b](https://github.com/toss/es-toolkit/commit/418183b0aa167aabaca95fa2221deac68fb728dd) <span style='color:grey;'>(significance=0.27)</span>
- Added missing backticks in the function signature for better readability in the documentation. [da091c4](https://github.com/toss/es-toolkit/commit/da091c49d8988ee0ec2544c7cc7f38c39419785b) <span style='color:grey;'>(significance=0.26)</span>
- The compatibility status for the `findIndex` function is now supported. [c639dd7](https://github.com/toss/es-toolkit/commit/c639dd7209977140cf184d281d1ebdf31fb734df) <span style='color:grey;'>(significance=0.50)</span>
- Documentation for `isString` function added. [8310cd9](https://github.com/toss/es-toolkit/commit/8310cd9d5d0898b9cb53761c25fb6a7097d1ab5f) <span style='color:grey;'>(significance=0.28)</span>
- Improved `rest` function documentation with clearer explanations and examples. The `rest` function creates a new function that groups arguments from a specified index into an array, passing previous arguments as individual elements. [98af4a3](https://github.com/toss/es-toolkit/commit/98af4a3a114c5e0db118db96ac352e3ad5b93341) <span style='color:grey;'>(significance=0.29)</span>