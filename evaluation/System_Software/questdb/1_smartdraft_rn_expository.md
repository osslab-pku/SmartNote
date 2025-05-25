# 8.1.0
## 🐛 fix
- fix(sql): fix spurious "unsupported operation" errors (#4632) [#4632](https://github.com/questdb/questdb/pull/4632) <span style='color:grey;'>(significance=0.06)</span>
- fix(sql): fix wrong results returned from parallel WHERE and GROUP BY fo [#4796](https://github.com/questdb/questdb/pull/4796) <span style='color:grey;'>(significance=0.10)</span>
- fix(sql): some window functions might double count rows (#4804) [#4804](https://github.com/questdb/questdb/pull/4804) <span style='color:grey;'>(significance=0.05)</span>
## 🔧 chore
- chore(sql): hide pre-touch magic number shutdown message (#4767) [#4767](https://github.com/questdb/questdb/pull/4767) <span style='color:grey;'>(significance=0.06)</span>
- chore(build): fix sqllogictest binary load to make it work where questdb [#4809](https://github.com/questdb/questdb/pull/4809) <span style='color:grey;'>(significance=0.08)</span>
## 🚀 perf
- perf(sql): speed up like/ilike operator on symbol column (#4794) [#4794](https://github.com/questdb/questdb/pull/4794) <span style='color:grey;'>(significance=0.06)</span>
## ✨ feat
- feat(sql): introduce SAMPLE BY FROM-TO syntax for specifying result rang [#4733](https://github.com/questdb/questdb/pull/4733) <span style='color:grey;'>(significance=0.06)</span>
- feat(core): trigger file to initiate snapshot recovery (#4807) [#4807](https://github.com/questdb/questdb/pull/4807) <span style='color:grey;'>(significance=0.06)</span>
