# 6.3.4

## 🛠️ Breaking Changes & Security
- Fixed a crash when calculating the minimum or maximum of an empty MVA array (issue #2332). Added a regression test to ensure stability. [24e69f7](https://github.com/manticoresoftware/manticoresearch/commit/24e69f735f95705e22b3a704e0f5a6ac68699aa4) <span style='color:grey;'>(significance=0.28)</span>
- Fixed the range aggregation result set for infinite range (issue #2339). Added a new test case to test 466 to ensure correctness. [5cf62e2](https://github.com/manticoresoftware/manticoresearch/commit/5cf62e2fd44cc11d89d9891192a8e7cfe80ffb4c) <span style='color:grey;'>(significance=0.28)</span>
- Fixed saving disk chunks at the RT index with hitless_words. Added a test case to ensure resolution. Resolves issue #2350. [122150f](https://github.com/manticoresoftware/manticoresearch/commit/122150f92ab14278e639791c053c052734fa3e71) <span style='color:grey;'>(significance=0.29)</span>

## 🐛 fix
- Fixed the join filter on columnar attributes from the right table to work correctly when the attribute is not in the select list. [24d77c8](https://github.com/manticoresoftware/manticoresearch/commit/24d77c8706c6b1cd76575e530e17c602816360ab) <span style='color:grey;'>(significance=0.27)</span>
- Fixed an issue where a left join returned non-matching entries when using the match() function over the right table. [662e8e3](https://github.com/manticoresoftware/manticoresearch/commit/662e8e3a59ad2c21ae50bef7d09069fc67eea945) <span style='color:grey;'>(significance=0.20)</span>
- Fixed build issues for xxhash on Visual Studio and GCC. [76aeb4d](https://github.com/manticoresoftware/manticoresearch/commit/76aeb4d196ece8da427d66ff2e832141810ca05b) <span style='color:grey;'>(significance=0.21)</span>
- Fixed calculation of presort and prefilter expressions dependent on joined attributes, improving query accuracy and reliability. [92aab99](https://github.com/manticoresoftware/manticoresearch/commit/92aab9914b7597dfe027345a6dacda7716cdd9ba) <span style='color:grey;'>(significance=0.22)</span>
- Improved performance for full-text queries with wildcards and RT index with multiple disk chunks. [e7d72c8](https://github.com/manticoresoftware/manticoresearch/commit/e7d72c8afa650a942ccead4c90accc1008fcb358) <span style='color:grey;'>(significance=0.26)</span>
- The sort property now depends on the properties order at the aggregation node. New test cases ensure proper functionality. [f55d215](https://github.com/manticoresoftware/manticoresearch/commit/f55d215245cdd79130d6940006b3974018597079) <span style='color:grey;'>(significance=0.36)</span>
- Addresses an error in the order of full-text and filter queries in JSON queries. Introduces a function to identify the full-text query node and updates query parsing logic. Adds a test case to ensure the fix works. [bff5ebd](https://github.com/manticoresoftware/manticoresearch/commit/bff5ebd26c61f8ce6389157c3a6f0dcea268a821) <span style='color:grey;'>(significance=0.23)</span>
- Updated executor dependency version. [2fc2e9b](https://github.com/manticoresoftware/manticoresearch/commit/2fc2e9b8f7685e7f9371008b31a3da3d819e78e5) <span style='color:grey;'>(significance=0.20)</span>
- Dependencies updated. [30b318f](https://github.com/manticoresoftware/manticicoresoftware/manticoresearch/commit/30b318f84b63436f30f5c26d9c35a6abc7ef6b8e) <span style='color:grey;'>(significance=0.21)</span>

## ✨ feat
- Improved CI process for building and tagging the test kit. Enhancements for detecting and handling tags and branches, fixed tag detection and fetching issues, and refactored code for better readability. Ensures proper branch and tag detection during Docker image push stage and better handling of development suffixes. [69b8eaf](https://github.com/manticoresoftware/manticoresearch/commit/69b8eaf68820ed67d2eb8b434e5d9fabff0be0f9) <span style='color:grey;'>(significance=0.24)</span>

## 📚 docs
- Updated changelog to include fixes for:
  - Grouping by stored check vs. rset merge
  - Daemon crash when querying with wildcard characters in an RT index using a CRC dictionary and `local_df` enabled
  - Crash in JOIN on `count(*)` without GROUP BY
  - JOIN not returning a warning when grouping by a full-text field [cdf1309](https://github.com/manticoresoftware/manticoresearch/commit/cdf13094135728314d73ce41e0be5086588afce8) <span style='color:grey;'>(significance=0.13)</span>
- The cutoff section in the manual now includes details on its interaction with aggregations. Using `cutoff` in aggregation queries is not recommended due to potential incorrect results. Examples illustrate the differences in results with and without `cutoff` in aggregation queries. [d02b0fd](https://github.com/manticoresoftware/manticoresearch/commit/d02b0fda3927f06fc696e5736f8d63395c0a164c) <span style='color:grey;'>(significance=0.19)</span>

## 🧪 test
- Copied tests from the master branch to ensure CI passes. [7e7c5d9](https://github.com/manticoresoftware/manticoresearch/commit/7e7c5d9ed7ad66611d1c9f690bc2d32ff73fb5d0) <span style='color:grey;'>(significance=0.22)</span>

## 🔧 chore
- The script now distinguishes development and release candidate packages based on the version number's last digit. [e748c12](https://github.com/manticoresoftware/manticoresearch/commit/e748c12b34857fb2f3dc24e617db87b9ac24e3e2) <span style='color:grey;'>(significance=0.23)</span>
- Modified the project. [d5fcd38](https://github.com/manticoresoftware/manticoresearch/commit/d5fcd380aeaf128ec0842a722416ba35b0b28aa5) <span style='color:grey;'>(significance=0.28)</span>
- Updated to the latest release version. [c78f758](https://github.com/manticoresoftware/manticoresearch/commit/c78f758a6bc240959c0bd7fc42644bb1d40d4b31) <span style='color:grey;'>(significance=0.11)</span>