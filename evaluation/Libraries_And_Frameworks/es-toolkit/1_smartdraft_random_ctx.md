# v1.16.0
## ✨ feat
- New functions `partial` and `partialRight` allow partial application of arguments to functions, support placeholders for partially applied arguments, and do not alter the `this` binding. [#368](https://github.com/toss/es-toolkit/pull/368) 
- Implemented the `has` function to check if a given path exists within an object. Supports single property keys, arrays of property keys, or strings representing deep paths. Verifies the validity of indexes for arrays and arguments objects, even if sparse. [01cf3a6](https://github.com/toss/es-toolkit/commit/01cf3a6c9ab401cace7149b4ff9985397d7832a4) 
- Implemented `matchesProperty` function to check if a target object matches a specific property value. Supports deep paths and various data types, including arrays and objects. Performs a deep comparison and returns `true` if the property value at the specified path matches the provided value, otherwise `false`. [dd97756](https://github.com/toss/es-toolkit/commit/dd97756ffb98a4a2e5bef0201c4e514a19c81d5e) 
- The `find` function now locates the first item in an array or object that meets specified conditions, supporting predicate functions, partial objects, property-value pairs, and property names. Comprehensive documentation and tests ensure proper usage and functionality. [fb05fbe](https://github.com/toss/es-toolkit/commit/fb05fbe3551f4e475c56d6a05e72770fd8cbfab5) 
- Implemented `findIndex` function to return the index of the first array item meeting a specified condition. The condition can be a predicate function, partial object, property-value pair, or property name. Compatible with lodash's `findIndex`. [c9587f3](https://github.com/toss/es-toolkit/commit/c9587f38165773eff2999a090d85f7465839e22f) 
- Implemented the `indexOf` function, similar to `Array.prototype.indexOf`, with added support for finding `NaN` values. Includes comprehensive tests and updated documentation. [#378](https://github.com/toss/es-toolkit/pull/378) 
- Introduced `isString` function to check if a value is a string, also serving as a type predicate in TypeScript to narrow the argument type to `string`. [#379](https://github.com/toss/es-toolkit/pull/379) 
- Implemented a `sortBy` function for sorting object arrays by specified keys or iteratee functions, with comprehensive documentation, examples, and performance benchmarks. [#381](https://github.com/toss/es-toolkit/pull/381) 
- Introduced a `padEnd` function that pads the end of a string with a specified character until it reaches a given length, similar to lodash's `padEnd`. Includes comprehensive documentation and tests. [#380](https://github.com/toss/es-toolkit/pull/380) 
- Added the `rest` function, which invokes another function with arguments from a specified start position provided as an array. Includes comprehensive documentation and tests. [#374](https://github.com/toss/es-toolkit/pull/374) 
- Introduced memoization feature for caching function results based on arguments. Supports custom cache implementations and resolver functions for flexible and efficient executions. [#208](https://github.com/toss/es-toolkit/pull/208) 

## 🐛 fix
- Added missing export to ensure proper functionality. [#373](https://github.com/toss/es-toolkit/pull/373) 
- Fixed type export for MemoizeCache. [aef394d](https://github.com/toss/es-toolkit/commit/aef394d8c4b4a8eb71002dd8c2897f726cefc510) 

## 📚 docs
- Clarified documentation for functions in the `es-toolkit/compat` library, which behave exactly like their lodash counterparts. [0ae3e51](https://github.com/toss/es-toolkit/commit/0ae3e5197755895eb41bc99f7761a00a491d93fc) 
- Updated documentation to reflect latest compatibility changes. [d7fa6ce](https://github.com/toss/es-toolkit/commit/d7fa6ceb50d31ba09a88c2cb3328585b8b328808) 
- Updated `find` function documentation to include details on its signature and parameters. [f71ff9e](https://github.com/toss/es-toolkit/commit/f71ff9e511ef98cf854abc28f16a0c6ae8f727b5) 
- Documentation added for `partial` and `partialRight` functions. [19e63de](https://github.com/toss/es-toolkit/commit/19e63dea7826abda9901e74bfcb334d813e3bc10) 
- Updated `partial` function documentation to include a reference link to the `bind` method, clarifying that `partial` does not alter the `this` binding. [4bc1fa8](https://github.com/toss/es-toolkit/commit/4bc1fa8704fe77f02e2ed4e6fd6b7909d9c8737c) 
- Updated documentation by removing a broken link. [8482793](https://github.com/toss/es-toolkit/commit/8482793737e5dace17f3d74a25199c6b417be44f) 
- Documentation for `find` and `findIndex` methods added. [2d96265](https://github.com/toss/es-toolkit/commit/2d96265951562d80a3d148895519c4cdcb23bb1f) 
- Documentation for the `indexOf` function added, detailing its usage and behavior. The function, available in the compatibility toolkit, can find `NaN` values and uses strict equality for other comparisons. [418183b](https://github.com/toss/es-toolkit/commit/418183b0aa167aabaca95fa2221deac68fb728dd) 
- Documentation now includes information on two new error classes: AbortError and TimeoutError, thrown when operations are aborted or timed out, respectively. [f99a6b2](https://github.com/toss/es-toolkit/commit/f99a6b26c3297647d0f3e8785c905620e72f6346) 
- Updated the `has` function documentation to include missing backticks in the function signature, improving readability and accuracy of code examples. [da091c4](https://github.com/toss/es-toolkit/commit/da091c49d8988ee0ec2544c7cc7f38c39419785b) 
- Updated compatibility for the `findIndex` function. [c639dd7](https://github.com/toss/es-toolkit/commit/c639dd7209977140cf184d281d1ebdf31fb734df) 
- Added documentation for the `isString` function. [8310cd9](https://github.com/toss/es-toolkit/commit/8310cd9d5d0898b9cb53761c25fb6a7097d1ab5f) 
- Improved documentation for the `rest` function. It now includes detailed descriptions, parameter explanations, return values, and examples in multiple languages. The `rest` function transforms arguments of a provided function, grouping arguments from a specified index into an array while passing previous arguments as individual elements. [98af4a3](https://github.com/toss/es-toolkit/commit/98af4a3a114c5e0db118db96ac352e3ad5b93341) 
- Updated compatibility documentation to reflect current implementation status of various functions. [82010d8](https://github.com/toss/es-toolkit/commit/82010d8cbba399f16429a7ad4989a5d3089ab12c) 
- Documentation for the `padEnd` function added. Pads the end of a string with a specified character until it reaches a given length. Returns the original string if already long enough or if the padding character is empty. [9d68f56](https://github.com/toss/es-toolkit/commit/9d68f5679d46689d612fefdea2d8e7b32b36d570) 

## 🎨 style
- Formatted the codebase with Prettier for consistent style and improved readability. [be4162d](https://github.com/toss/es-toolkit/commit/be4162dc19003c7accde6c051edc0f85e3b72d76) 
- Addressed various ESLint errors by adjusting code style: modified function parameters, added missing comments, and corrected variable declarations. Enhanced code readability and maintainability without altering functionality. [5cb0b78](https://github.com/toss/es-toolkit/commit/5cb0b78819bac7c729c9429e2ba4d9ceb4d6613d) 
- Fixed ESLint errors to improve code quality and maintainability. [ff49feb](https://github.com/toss/es-toolkit/commit/ff49feba5900f8e082f8a672ef9f0f1c6b1d7fb2) 

## 🔧 chore
- Updated bundle size benchmarks. [3c7e2ce](https://github.com/toss/es-toolkit/commit/3c7e2ce5dea05f550ff6dac9085ff6b9b16a1291) 
- Reorganized benchmark files by moving `cloneDeep`, `set`, and `startCase` to a performance folder. Removed duplicate `zipObjectDeep` benchmark and updated import paths. [#375](https://github.com/toss/es-toolkit/pull/375) 

## ♻️ refactor
- Refactored compareValues function for consistent use across internal functions and fixed type errors. [#382](https://github.com/toss/es-toolkit/pull/382)
