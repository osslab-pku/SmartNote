# v1.0.121
## 🐛 fix
- This update fixes issues with environment variables POD_NAME and POD_NAMESPACE when high availability is enabled and corrects default memory and CPU settings. [#723](https://github.com/stakater/Reloader/pull/723) <span style='color:grey;'>(significance=0.91)</span>
## 🔧 chore
- Updated resource field references for environment variables by swapping the resources for GOMAXPROCS and GOMEMLIMIT. [70ab566](https://github.com/stakater/Reloader/commit/70ab56606df1f9fd4877b0f615b0b929f8269511) <span style='color:grey;'>(significance=0.98)</span>
