# 6.3.4
## 🐛 fix
- Improved performance for full-text queries with wildcards and real-time indexes by disabling local_df calculation for all wildcard terms. [e7d72c8](https://github.com/manticoresoftware/manticoresearch/commit/e7d72c8afa650a942ccead4c90accc1008fcb358)
- Fixed join filters on columnar attributes from the right table not applying when the attribute was excluded from the select list. [24d77c8](https://github.com/manticoresoftware/manticoresearch/commit/24d77c8706c6b1cd76575e530e17c602816360ab)
- Fixed an issue where a left join returned non-matching entries when using the match() function on the right table. [662e8e3](https://github.com/manticoresoftware/manticoresearch/commit/662e8e3a59ad2c21ae50bef7d09069fc67eea945)
- Fixed a crash when calculating the minimum or maximum of an empty MVA array. Added a regression test to prevent recurrence. [24e69f7](https://github.com/manticoresoftware/manticoresearch/commit/24e69f735f95705e22b3a704e0f5a6ac68699aa4)
- Fixed range aggregation result set for infinite range case (issue #2339). Added a test case to ensure correctness. [5cf62e2](https://github.com/manticoresoftware/manticoresearch/commit/5cf62e2fd44cc11d89d9891192a8e7cfe80ffb4c)
- Fixed xxhash build issues on Visual Studio and GCC (bug #2343). [76aeb4d](https://github.com/manticoresoftware/manticoresearch/commit/76aeb4d196ece8da427d66ff2e832141810ca05b)
- Fixed calculation of presort and prefilter expressions dependent on joined attributes. [92aab99](https://github.com/manticoresoftware/manticoresearch/commit/92aab9914b7597dfe027345a6dacda7716cdd9ba)
- Fixed saving disk chunks at RT index with hitless_words, added test case for test 408, and resolved issue #2350. [122150f](https://github.com/manticoresoftware/manticoresearch/commit/122150f92ab14278e639791c053c052734fa3e71)
- Addressed an issue where the sort property depended on the order of properties at the aggregation node. Added test cases to ensure the fix is effective. [f55d215](https://github.com/manticoresoftware/manticoresearch/commit/f55d215245cdd79130d6940006b3974018597079)
- Fixed the order of full-text and filter queries in JSON queries and added a test case. [bff5ebd](https://github.com/manticoresoftware/manticoresearch/commit/bff5ebd26c61f8ce6389157c3a6f0dcea268a821)

## ✨ feat
- Improved CI process for building and tagging the test kit: better detection and handling of branch and tag names, fixed tag fetching and detection issues, ensured proper tagging during Docker image push, and refactored scripts for readability and functionality. [69b8eaf](https://github.com/manticoresoftware/manticoresearch/commit/69b8eaf68820ed67d2eb8b434e5d9fabff0be0f9)

## 📚 docs
- Updated Changelog: Fixed grouping by stored check vs. rset merge, daemon crash when querying with wildcard characters in an RT index using a CRC dictionary and `local_df` enabled, crash in JOIN on `count(*)` without GROUP BY, and JOIN not returning a warning when grouping by a full-text field. [cdf1309](https://github.com/manticoresoftware/manticoresearch/commit/cdf13094135728314d73ce41e0be5086588afce8)
- The cutoff section in the manual now includes information on its interaction with aggregations. Using `cutoff` in aggregation queries is not recommended due to potential incorrect results. Examples illustrate these issues. [d02b0fd](https://github.com/manticoresoftware/manticoresearch/commit/d02b0fda3927f06fc696e5736f8d63395c0a164c)

## 🧪 test
- Copied tests from the master branch to ensure CI passes. [7e7c5d9](https://github.com/manticoresoftware/manticoresearch/commit/7e7c5d9ed7ad66611d1c9f690bc2d32ff73fb5d0)

## 🔧 chore
- The script now searches for non-development packages in the release candidate. [e748c12](https://github.com/manticoresoftware/manticoresearch/commit/e748c12b34857fb2f3dc24e617db87b9ac24e3e2)
- Updated to the latest release version. [c78f758](https://github.com/manticoresoftware/manticoresearch/commit/c78f758a6bc240959c0bd7fc42644bb1d40d4b31)
