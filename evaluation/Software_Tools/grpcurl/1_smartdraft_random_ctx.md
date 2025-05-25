# v1.9.0
## ✨ feat
- Initial support for the -t flag added to show timing data for stages like Dial (TLS setup and BlockingDial), InvokeRPC, and total time. This data is part of the very verbose functionality. [#428](https://github.com/fullstorydev/grpcurl/pull/428)
- Support for xDS credentials now allows the use of xDS-provided certificates specified in the GRPC_XDS_BOOTSTRAP environment variable. xDS credentials are enabled only if the target address uses the xds:/// prefix, signaling the gRPC client to use an xDS server for resolving the target. This enhancement is a no-op outside the context of xDS, ensuring existing functionality remains unaffected. [#424](https://github.com/fullstorydev/grpcurl/pull/424)

## 🐛 fix
- Expanded the -max-time flag documentation to clarify it sets the RPC timeout. Updated help text includes "timeout" and "deadline" for better discoverability and understanding. [#435](https://github.com/fullstorydev/grpcurl/pull/435)
- The default authority for a Unix domain socket is 'localhost' if unspecified. [#445](https://github.com/fullstorydev/grpcurl/pull/445)

## ♻️ refactor
- Removed support for Go 1.9 by deleting corresponding code files and updating indentation handling logic. [7ccaf0a](https://github.com/fullstorydev/grpcurl/commit/7ccaf0a21fedf97d7dd429cd75f00bc0a15a882b)

## 🔧 chore
- Updated `golang.google.org/grpc` dependency to version 1.57.1 to address a security advisory. [#427](https://github.com/fullstorydev/grpcurl/pull/427)
- Cleaned up Go module dependencies. [#437](https://github.com/fullstorydev/grpcurl/pull/437)
- Updated the `github.com/golang/protobuf` dependency. [#448](https://github.com/fullstorydev/grpcurl/pull/448)
- Introduces leniency in handling missing dependencies for smoother operations. Improves static analysis tool functionality. [#453](https://github.com/fullstorydev/grpcurl/pull/453)
- Added support for nfmp. [#440](https://github.com/fullstorydev/grpcurl/pull/440)
- Updated the brand name throughout the project. [#452](https://github.com/fullstorydev/grpcurl/pull/452)
- Dependency updates. [#436](https://github.com/fullstorydev/grpcurl/pull/436)
- Minor updates, changes, and improvements. [#443](https://github.com/fullstorydev/grpcurl/pull/443) [#446](https://github.com/fullstorydev/grpcurl/pull/446)

## 📚 docs
- Updated the URL format for downloading tarballs for Homebrew to ensure compatibility with the latest GitHub URL structure. [#421](https://github.com/fullstorydev/grpcurl/pull/421)
