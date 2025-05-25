# Release Notes for v1.9.0

## Overview
This release introduces several enhancements, bug fixes, and dependency updates to improve the functionality and security of the project. Key highlights include the addition of timing data support, improved documentation, and updates to various dependencies.

## New Features
- **Timing Data Support**: Initial support for the `-t` flag has been added to show basic timing data for the Dial stage and InvokeRPC method, as well as the total time. This feature is part of the very verbose output functionality. [#428]

## Enhancements
- **Documentation Improvements**: Expanded the documentation for the `-max-time` flag to clarify that it sets the RPC timeout, aiding in the discovery of this feature. [#435]
- **Brand Name Update**: Updated the brand name references in the project. [#452]
- **Unix Domain Socket Authority**: Default authority for Unix domain sockets is now set to `localhost`. [#445]

## Dependency Updates
- **gRPC**: Bumped `golang.google.org/grpc` to v1.57.1 to address security advisories. [#427]
- **Protobuf**: Updated `google.golang.org/protobuf` from v1.31.0 to v1.32.0. [#437]
- **Protoreflect**: Multiple updates to `github.com/jhump/protoreflect` from v1.15.3 to v1.15.6, addressing various bug fixes and compatibility issues. [#436, #443, #446]
- **Golang Protobuf**: Updated `github.com/golang/protobuf` from v1.5.3 to v1.5.4. [#448]

## Bug Fixes
- **xDS Credentials**: Enabled xDS credentials, allowing the use of xDS-provided certificates. This change is a no-op outside of xDS contexts. [#424]
- **Protoreflect Bug Fixes**: Updated to the latest protoreflect to fix bugs related to missing file descriptors and other issues. [#453]

## Build and CI
- **Go Version Update**: Removed support for Go 1.9 and updated the CI configuration to use newer Go versions.
- **GoReleaser Configuration**: Updated the GoReleaser configuration to support newer versions and added support for building deb and rpm packages. [#440]
- **CGO Disabled**: Disabled CGO for improved compatibility across different Linux distributions. [#420]

## Miscellaneous
- **Tarball URL Update**: Updated the tarball URL used by Homebrew to align with recent changes in Homebrew's requirements. [#421]

This release focuses on enhancing the usability and security of the project while ensuring compatibility with the latest dependencies. Users are encouraged to update to this version to benefit from the improvements and fixes.