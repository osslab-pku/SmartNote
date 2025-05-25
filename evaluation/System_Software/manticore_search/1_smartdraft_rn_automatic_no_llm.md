# 6.3.4
## 🐛 fix
- executor 1.1.6 in deps.txt [2fc2e9b](https://github.com/manticoresoftware/manticoresearch/commit/2fc2e9b8f7685e7f9371008b31a3da3d819e78e5) <span style='color:grey;'>(significance=0.11)</span>
- fixed join filter on columnar attributes from right table when attribute [24d77c8](https://github.com/manticoresoftware/manticoresearch/commit/24d77c8706c6b1cd76575e530e17c602816360ab) <span style='color:grey;'>(significance=0.13)</span>
- fixed left join returning non-matching entries when match() over right t [662e8e3](https://github.com/manticoresoftware/manticoresearch/commit/662e8e3a59ad2c21ae50bef7d09069fc67eea945) <span style='color:grey;'>(significance=0.28)</span>
- fixed crash on mva min or max for empty mva array; fixed #2332; added re [24e69f7](https://github.com/manticoresoftware/manticoresearch/commit/24e69f735f95705e22b3a704e0f5a6ac68699aa4) <span style='color:grey;'>(significance=0.13)</span>
- fixed range aggregation result set for infinite range case; fixed #2339; [5cf62e2](https://github.com/manticoresoftware/manticoresearch/commit/5cf62e2fd44cc11d89d9891192a8e7cfe80ffb4c) <span style='color:grey;'>(significance=0.17)</span>
- fixed xxhash build on visual studio and gcc; fixed #2343 [76aeb4d](https://github.com/manticoresoftware/manticoresearch/commit/76aeb4d196ece8da427d66ff2e832141810ca05b) <span style='color:grey;'>(significance=0.24)</span>
- fixed save of disk chunk at RT index with hitless_words; added case to t [122150f](https://github.com/manticoresoftware/manticoresearch/commit/122150f92ab14278e639791c053c052734fa3e71) <span style='color:grey;'>(significance=0.15)</span>
- disabled local_df calculation for all wildcard terms in the query; fixed [e7d72c8](https://github.com/manticoresoftware/manticoresearch/commit/e7d72c8afa650a942ccead4c90accc1008fcb358) <span style='color:grey;'>(significance=0.13)</span>
- fixed sort property depends on the properties order at the aggs node; ad [f55d215](https://github.com/manticoresoftware/manticoresearch/commit/f55d215245cdd79130d6940006b3974018597079) <span style='color:grey;'>(significance=0.11)</span>
- fixed error on full-text vs filter order at the JSON query; added case t [bff5ebd](https://github.com/manticoresoftware/manticoresearch/commit/bff5ebd26c61f8ce6389157c3a6f0dcea268a821) <span style='color:grey;'>(significance=0.29)</span>
- updated deps [30b318f](https://github.com/manticoresoftware/manticoresearch/commit/30b318f84b63436f30f5c26d9c35a6abc7ef6b8e) <span style='color:grey;'>(significance=0.14)</span>
- CI improvements in building test kit and auto tag feature/tag for test-kit (#2271) [69b8eaf](https://github.com/manticoresoftware/manticoresearch/commit/69b8eaf68820ed67d2eb8b434e5d9fabff0be0f9) <span style='color:grey;'>(significance=0.31)</span>
- Copied a few clt tests from the master branch to pass CI [7e7c5d9](https://github.com/manticoresoftware/manticoresearch/commit/7e7c5d9ed7ad66611d1c9f690bc2d32ff73fb5d0) <span style='color:grey;'>(significance=0.13)</span>
## 📚 docs
- manual: improve cutoff section by adding info about how it works with ag [d02b0fd](https://github.com/manticoresoftware/manticoresearch/commit/d02b0fda3927f06fc696e5736f8d63395c0a164c) <span style='color:grey;'>(significance=0.15)</span>
## ✨ feat
- fixed calculation of presort/prefilter expressions that depend on joined [92aab99](https://github.com/manticoresoftware/manticoresearch/commit/92aab9914b7597dfe027345a6dacda7716cdd9ba) <span style='color:grey;'>(significance=0.25)</span>
