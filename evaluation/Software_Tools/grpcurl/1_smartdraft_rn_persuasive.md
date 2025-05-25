# v1.9.0
## 🐛 fix
- The default authority for a Unix domain socket is now 'localhost' when unspecified. [#445](https://github.com/fullstorydev/grpcurl/pull/445) <span style='color:grey;'>(significance=0.96)</span>
- Removed support for Go 1.9 and older versions by deleting related code and simplifying indentation logic. [7ccaf0a](https://github.com/fullstorydev/grpcurl/commit/7ccaf0a21fedf97d7dd429cd75f00bc0a15a882b) <span style='color:grey;'>(significance=0.94)</span>
- Expanded `-max-time` flag documentation to clarify it sets the RPC timeout. Added "timeout" and "deadline" to the help text for better understanding and discovery. [#435](https://github.com/fullstorydev/grpcurl/pull/435) <span style='color:grey;'>(significance=0.87)</span>

## ✨ feat
- Initial support for a new `-t` flag that displays timing data for stages like Dial (TLS setup and BlockingDial), InvokeRPC, and total time. Integrated into the very verbose output functionality. [#428](https://github.com/fullstorydev/grpcurl/pull/428) <span style='color:grey;'>(significance=0.91)</span>
- Support for xDS credentials added, enabling use of xDS-provided certificates when the target is an xDS target. Relevant credentials are automatically retrieved from environment variables. [#424](https://github.com/fullstorydev/grpcurl/pull/424) <span style='color:grey;'>(significance=0.89)</span>

## 🔧 chore
- Introduced leniency in handling missing dependencies for smoother operations. Refined code to address static analysis concerns, enhancing overall quality. [#453](https://github.com/fullstorydev/grpcurl/pull/453) <span style='color:grey;'>(significance=0.92)</span>
- Minor improvements and bug fixes. [#448](https://github.com/fullstorydev/grpcurl/pull/448) <span style='color:grey;'>(significance=0.90)</span>
- Support for nfmp added. [#440](https://github.com/fullstorydev/grpcurl/pull/440) <span style='color:grey;'>(significance=0.85)</span>
- Minor improvements and bug fixes. [#446](https://github.com/fullstorydev/grpcurl/pull/446) <span style='color:grey;'>(significance=0.85)</span>
- Minor dependency updates. [#436](https://github.com/fullstorydev/grpcurl/pull/436) <span style='color:grey;'>(significance=0.85)</span>
- Minor updates to project dependencies. [#443](https://github.com/fullstorydev/grpcurl/pull/443) <span style='color:grey;'>(significance=0.84)</span>
- Cleaned up project dependencies. [#437](https://github.com/fullstorydev/grpcurl/pull/437) <span style='color:grey;'>(significance=0.82)</span>
- Updated the brand name throughout the project. [#452](https://github.com/fullstorydev/grpcurl/pull/452) <span style='color:grey;'>(significance=0.80)</span>

## 📚 docs
- Updated the tarball URL used by Homebrew. [#421](https://github.com/fullstorydev/grpcurl/pull/421) <span style='color:grey;'>(significance=0.82)</span>