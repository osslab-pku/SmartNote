# 6.3.4
## 🐛 fix
- Fixed an issue where a left join returned non-matching entries when using the match() function on the right table. [662e8e3](https://github.com/manticoresoftware/manticoresearch/commit/662e8e3a59ad2c21ae50bef7d09069fc67eea945) <span style='color:grey;'>(significance=0.22)</span>
- Fixed an error with the order of full-text and filter queries in JSON queries. Added a test case to ensure resolution. [bff5ebd](https://github.com/manticoresoftware/manticoresearch/commit/bff5ebd26c61f8ce6389157c3a6f0dcea268a821) <span style='color:grey;'>(significance=0.20)</span>
- Addressed an issue with join filters on columnar attributes from the right table when the attribute is not included in the select list. [24d77c8](https://github.com/manticoresoftware/manticoresearch/commit/24d77c8706c6b1cd76575e530e17c602816360ab) <span style='color:grey;'>(significance=0.10)</span>
- Fixed range aggregation result set for infinite range case (issue #2339). Added new test case to test 466. [5cf62e2](https://github.com/manticoresoftware/manticoresearch/commit/5cf62e2fd44cc11d89d9891192a8e7cfe80ffb4c) <span style='color:grey;'>(significance=0.12)</span>
- Fixed build issues for xxhash on Visual Studio and GCC. [76aeb4d](https://github.com/manticoresoftware/manticoresearch/commit/76aeb4d196ece8da427d66ff2e832141810ca05b) <span style='color:grey;'>(significance=0.17)</span>
- Improves CI process for building and tagging the test kit. Enhances tagging mechanism by including both tag and branch, refines detection of development suffixes, and addresses issues related to branch and tag detection during Docker image push. Fixes tag fetching and incorrect tags in Docker push script, and updates current branch detection to work in both pull requests and the original branch. [69b8eaf](https://github.com/manticoresoftware/manticoresearch/commit/69b8eaf68820ed67d2eb8b434e5d9fabff0be0f9) <span style='color:grey;'>(significance=0.22)</span>

## ✨ feat
- Fixed calculation of presort and prefilter expressions dependent on joined attributes. [92aab99](https://github.com/manticoresoftware/manticoresearch/commit/92aab9914b7597dfe027345a6dacda7716cdd9ba) <span style='color:grey;'>(significance=0.20)</span>

## 📚 docs
- Improved the cutoff section in the manual by adding information on its interaction with aggregations. [d02b0fd](https://github.com/manticoresoftware/manticoresearch/commit/d02b0fda3927f06fc696e5736f8d63395c0a164c) <span style='color:grey;'>(significance=0.11)</span>