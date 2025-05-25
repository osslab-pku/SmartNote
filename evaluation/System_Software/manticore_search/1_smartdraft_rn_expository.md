# 6.3.4
## 📚 docs
- manual: improve cutoff section by adding info about how it works with ag [d02b0fd](https://github.com/manticoresoftware/manticoresearch/commit/d02b0fda3927f06fc696e5736f8d63395c0a164c) <span style='color:grey;'>(significance=0.11)</span>
## 🐛 fix
- fixed join filter on columnar attributes from right table when attribute [24d77c8](https://github.com/manticoresoftware/manticoresearch/commit/24d77c8706c6b1cd76575e530e17c602816360ab) <span style='color:grey;'>(significance=0.10)</span>
- fixed left join returning non-matching entries when match() over right t [662e8e3](https://github.com/manticoresoftware/manticoresearch/commit/662e8e3a59ad2c21ae50bef7d09069fc67eea945) <span style='color:grey;'>(significance=0.22)</span>
- fixed range aggregation result set for infinite range case; fixed #2339; [5cf62e2](https://github.com/manticoresoftware/manticoresearch/commit/5cf62e2fd44cc11d89d9891192a8e7cfe80ffb4c) <span style='color:grey;'>(significance=0.12)</span>
- fixed xxhash build on visual studio and gcc; fixed #2343 [76aeb4d](https://github.com/manticoresoftware/manticoresearch/commit/76aeb4d196ece8da427d66ff2e832141810ca05b) <span style='color:grey;'>(significance=0.17)</span>
- fixed error on full-text vs filter order at the JSON query; added case t [bff5ebd](https://github.com/manticoresoftware/manticoresearch/commit/bff5ebd26c61f8ce6389157c3a6f0dcea268a821) <span style='color:grey;'>(significance=0.20)</span>
- CI improvements in building test kit and auto tag feature/tag for test-kit (#2271) [69b8eaf](https://github.com/manticoresoftware/manticoresearch/commit/69b8eaf68820ed67d2eb8b434e5d9fabff0be0f9) <span style='color:grey;'>(significance=0.22)</span>
## ✨ feat
- fixed calculation of presort/prefilter expressions that depend on joined [92aab99](https://github.com/manticoresoftware/manticoresearch/commit/92aab9914b7597dfe027345a6dacda7716cdd9ba) <span style='color:grey;'>(significance=0.20)</span>
