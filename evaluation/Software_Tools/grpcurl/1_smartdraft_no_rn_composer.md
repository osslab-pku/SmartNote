# v1.9.0
## 📚 docs
- Updated the tarball URL used by Homebrew. [#421](https://github.com/fullstorydev/grpcurl/pull/421) <span style='color:grey;'>(significance=0.83)</span>
## 🔧 chore
- Changes to the project's dependencies. [#427](https://github.com/fullstorydev/grpcurl/pull/427) <span style='color:grey;'>(significance=0.91)</span>
- Updated project dependencies. [#437](https://github.com/fullstorydev/grpcurl/pull/437) <span style='color:grey;'>(significance=0.83)</span>
- Updated project dependencies. [#436](https://github.com/fullstorydev/grpcurl/pull/436) <span style='color:grey;'>(significance=0.84)</span>
- No functional changes in this update. [#443](https://github.com/fullstorydev/grpcurl/pull/443) <span style='color:grey;'>(significance=0.83)</span>
- Minor update. [#446](https://github.com/fullstorydev/grpcurl/pull/446) <span style='color:grey;'>(significance=0.84)</span>
- Added support for nfmp. [#440](https://github.com/fullstorydev/grpcurl/pull/440) <span style='color:grey;'>(significance=0.85)</span>
- Updated project dependencies. [#448](https://github.com/fullstorydev/grpcurl/pull/448) <span style='color:grey;'>(significance=0.90)</span>
- Updated the brand name throughout the project. [#452](https://github.com/fullstorydev/grpcurl/pull/452) <span style='color:grey;'>(significance=0.79)</span>
- Introduces leniency for missing server dependencies and adjusts code for static analysis tools. [#453](https://github.com/fullstorydev/grpcurl/pull/453) <span style='color:grey;'>(significance=0.95)</span>
## 🐛 fix
- Removed support for Go 1.9, simplifying the codebase by eliminating outdated indentation handling logic. [7ccaf0a](https://github.com/fullstorydev/grpcurl/commit/7ccaf0a21fedf97d7dd429cd75f00bc0a15a882b) <span style='color:grey;'>(significance=0.95)</span>
- The `-max-time` flag documentation now clarifies it sets the RPC timeout. "Timeout" and "deadline" have been added to the help text for better discoverability. [#435](https://github.com/fullstorydev/grpcurl/pull/435) <span style='color:grey;'>(significance=0.89)</span>
- The default authority for a Unix domain socket is set to 'localhost'. [#445](https://github.com/fullstorydev/grpcurl/pull/445) <span style='color:grey;'>(significance=0.96)</span>
## ✨ feat
- Added initial support for a new flag to show timing data for stages like Dial, TLS setup, BlockingDial, InvokeRPC, and total time. Integrated into the very verbose output functionality. [#428](https://github.com/fullstorydev/grpcurl/pull/428) <span style='color:grey;'>(significance=0.93)</span>
- This update adds support for xDS credentials, allowing the use of xDS-provided certificates for xDS targets. Relevant credentials are automatically retrieved from environment variables when the address has an xds:/// prefix. This enhancement is non-intrusive outside the xDS context, as shown by successful test results. [#424](https://github.com/fullstorydev/grpcurl/pull/424) <span style='color:grey;'>(significance=0.91)</span>
