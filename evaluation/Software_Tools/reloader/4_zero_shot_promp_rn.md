# Release Notes for v1.0.121

## Overview

This release includes important fixes and improvements to the Reloader project, focusing on environment variable handling and resource configuration. The changes ensure better stability and performance, especially in high-availability (HA) configurations.

## Key Changes

### Bug Fixes

- **POD_NAME and POD_NAMESPACE Environment Variables**: Fixed an issue where the `POD_NAME` and `POD_NAMESPACE` environment variables were not set correctly when `enableHA` was true. This fix addresses errors encountered in HA mode, ensuring that the application can run without issues. This was resolved in [PR #723](https://github.com/stakater/Reloader/pull/723).

- **Resource Configuration**: Corrected the default values for memory and CPU resources in the deployment templates. This change ensures that the resource limits are set appropriately, preventing potential misconfigurations that could lead to resource allocation issues.

### Enhancements

- **Test Coverage**: Added a test case to verify that the `POD_NAME` and `POD_NAMESPACE` environment variables are correctly set when `enableHA` is true. This enhancement improves the reliability of the deployment in HA scenarios.

## File Modifications

- **Chart Version Update**: Updated the `Chart.yaml` and related files to reflect the new version `v1.0.121`.

- **Deployment Templates**: Modified the `deployment.yaml` and `values.yaml` files to fix resource field references and update image tags to `v1.0.121`.

- **Manifest Updates**: Adjusted the Kubernetes manifests to align with the new versioning and ensure consistency across deployment configurations.

## Conclusion

This release is a maintenance update that addresses critical issues related to environment variable handling and resource configuration. Users are encouraged to update to this version to benefit from the improved stability and performance, especially in high-availability deployments.