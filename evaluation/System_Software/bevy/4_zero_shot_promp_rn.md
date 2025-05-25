# Release Notes for v0.14.1

## Overview
This release focuses on bug fixes, performance improvements, and minor feature additions. It addresses several issues related to rendering, asset management, and system scheduling, while also introducing new functionalities and optimizations.

## Key Changes

### Bug Fixes
- **Rendering and Graphics:**
  - Fixed a crash related to asset load failure events being processed after asset drop.
  - Resolved issues with SMAA shader errors and viewport default size causing validation errors.
  - Corrected the handling of morph targets and vertex indices in mesh rendering.
  - Fixed overflow in `RenderLayers::iter_layers` and NaN issues in AABB implementations for round shapes.

- **UI and Layout:**
  - Addressed layout glitches caused by removed nodes still set as children.
  - Improved error messages for unstyled child warnings in UI hierarchy.

- **Assets and Resources:**
  - Fixed issues with `bevy_gltf` and `bevy_window` failing to build with certain features enabled.
  - Corrected the handling of DDS features in `bevy_gltf`.

- **System and Scheduling:**
  - Fixed ambiguities in system ordering and improved error messages for missing state schedules.
  - Resolved issues with repeated window close requests causing panics.

### Performance Improvements
- Optimized transform propagation and UI layout systems to reduce CPU usage.
- Improved meshlet mesh deserialization speed significantly.
- Enhanced batching and buffer management for rendering, reducing overhead and improving performance.

### New Features
- **Rendering:**
  - Added support for environment map and skybox transformations.
  - Introduced a new postprocessing effect: chromatic aberration.

- **System and Scheduling:**
  - Added `insert_before` and `insert_startup_before` methods for more flexible system scheduling.
  - Implemented `ObserverSystem` traits to allow observer systems to have outputs.

- **Assets and Resources:**
  - Enabled reflection for `DepthOfFieldSettings` and added missing reflect attributes for various types.
  - Exposed the default font bytes for external use.

### Documentation and Examples
- Updated documentation to clarify usage and improve accuracy, including better intra-doc links and examples.
- Added new examples for fixed timestep movement and specialized mesh pipelines.
- Improved existing examples to reflect recent changes and optimizations.

### Miscellaneous
- Deprecated `is_playing_animation` in favor of `animation_is_playing`.
- Made `Msaa` a component for more granular control over multisampling settings.
- Removed the deprecated `bevy_dynamic_plugin` due to unsoundness.

## Migration Guide
- Users should update their code to handle changes in system scheduling and asset management APIs.
- The `Msaa` resource is now a component, requiring updates to camera setup.
- Deprecated functions and features should be replaced with their updated counterparts as per the migration guide.

This release ensures better stability, performance, and flexibility for developers using the Bevy engine. Users are encouraged to update to this version to benefit from the improvements and fixes.