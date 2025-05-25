# v1.9.0
## ⚠️ breaking changes
- Removed support for Go 1.9 by deleting corresponding code and simplifying indentation logic. [7ccaf0a](https://github.com/fullstorydev/grpcurl/commit/7ccaf0a21fedf97d7dd429cd75f00bc0a15a882b) 
 <span style='color:grey;'>(significance=0.52)</span>

## ✨ feat
- Enables xDS credentials, using xDS-provided certificates specified in the GRPC_XDS_BOOTSTRAP environment variable. Effective only for xDS targets, ensuring relevant credentials are automatically used. [#424](https://github.com/fullstorydev/grpcurl/pull/424) 
 <span style='color:grey;'>(significance=0.89)</span>
- Added initial support for a new `-t` flag to display timing data for the Dial stage (including TLS setup and BlockingDial), the InvokeRPC method, and the total time. This timing data is part of the very verbose output functionality. [#428](https://github.com/fullstorydev/grpcurl/pull/428) 
 <span style='color:grey;'>(significance=0.66)</span>

## 🐛 fix
- The default authority for Unix domain sockets now uses 'localhost' when no authority is specified. [#445](https://github.com/fullstorydev/grpcurl/pull/445) 
 <span style='color:grey;'>(significance=0.84)</span>
- Expanded `-max-time` flag documentation to clarify it sets the RPC timeout, adding "timeout" and "deadline" to the help text for better discoverability. [#435](https://github.com/fullstorydev/grpcurl/pull/435) 
 <span style='color:grey;'>(significance=0.68)</span>

## 🛠️ perf
- Introduces leniency in handling missing dependencies from the server and includes code improvements to enhance compatibility and maintainability. [#453](https://github.com/fullstorydev/grpcurl/pull/453) 
 <span style='color:grey;'>(significance=0.68)</span>

## 🔧 chore
- Support for nfmp added. [#440](https://github.com/fullstorydev/grpcurl/pull/440) 
 <span style='color:grey;'>(significance=0.49)</span>
- Cleaned up Go module dependencies. [#437](https://github.com/fullstorydev/grpcurl/pull/437) 
 <span style='color:grey;'>(significance=0.45)</span>
- Updated dependencies. [#436](https://github.com/fullstorydev/grpcurl/pull/436) 
 <span style='color:grey;'>(significance=0.34)</span>
- Updated project dependency. [#443](https://github.com/fullstorydev/grpcurl/pull/443) 
 <span style='color:grey;'>(significance=0.32)</span>
- Updated the brand name throughout the project. [#452](https://github.com/fullstorydev/grpcurl/pull/452) 
 <span style='color:grey;'>(significance=0.23)</span>
- Minor improvements and bug fixes. [#446](https://github.com/fullstorydev/grpcurl/pull/446), [#448](https://github.com/fullstorydev/grpcurl/pull/448) 
 (significance=0.27, 0.15)

## 📚 docs
- Updated the tarball URL used by Homebrew. [#421](https://github.com/fullstorydev/grpcurl/pull/421) 
 <span style='color:grey;'>(significance=0.21)</span>