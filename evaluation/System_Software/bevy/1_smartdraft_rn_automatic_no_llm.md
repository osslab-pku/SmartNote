# v0.14.1
## 🐛 fix
- EmptyPathStream is only used in android/wasm32 (#14200) [a6fde10](https://github.com/bevyengine/bevy/commit/a6fde1059c8a413b353d4f39581b09b296cd6b9a) <span style='color:grey;'>(significance=0.02)</span>
- impl Reflect + Clone for StateScoped (#14156) [4275669](https://github.com/bevyengine/bevy/commit/4275669b07492ea66d5cf09fbd0c94c8833dafac) <span style='color:grey;'>(significance=0.01)</span>
- add entity to error message (#14163) [c6b80c5](https://github.com/bevyengine/bevy/commit/c6b80c56644a35faad6aa7452102fa289f53ece4) <span style='color:grey;'>(significance=0.02)</span>
- use Display for entity id in log_components (#14164) [7ed1f6a](https://github.com/bevyengine/bevy/commit/7ed1f6a9b6b24224052ae2284d01239b11824c3f) <span style='color:grey;'>(significance=0.02)</span>
- Optimize unnecessary normalizations for `Transform::local_{xyz}` (#14171) [e941264](https://github.com/bevyengine/bevy/commit/e941264b6f3f44af865e0e1642e93d34e8afee65) <span style='color:grey;'>(significance=0.04)</span>
- disable gpu preprocessing on android with Adreno 730 GPU and earilier (#14176) [5d9e44b](https://github.com/bevyengine/bevy/commit/5d9e44b9dce73ef35670212a399955988e28ccec) <span style='color:grey;'>(significance=0.03)</span>
- fix: Possible NaN due to denormalised quaternions in AABB implementations for round shapes. (#14240) [0e1858b](https://github.com/bevyengine/bevy/commit/0e1858bc4f1a9e7664898c27d41ad19e9c651c31) <span style='color:grey;'>(significance=0.03)</span>
- Dirty fix for App hanging when windows are invisible on WindowsOS (#14155) [4bd56b6](https://github.com/bevyengine/bevy/commit/4bd56b6da1362f503203b66941bdbec742ec3cd7) <span style='color:grey;'>(significance=0.06)</span>
- Fix swapped docs for `Rot2::rotation_to/from_y` (#14307) [d0583c8](https://github.com/bevyengine/bevy/commit/d0583c8b5444660049a6a397604389f16323be97) <span style='color:grey;'>(significance=0.05)</span>
- Allow observer systems to have outputs (#14159) [7f3fea9](https://github.com/bevyengine/bevy/commit/7f3fea9a5bb86a7f6a64dc45723b5c6b25a8f2e0) <span style='color:grey;'>(significance=0.02)</span>
- Make initial `StateTransition` run before `PreStartup` (#14208) [524fb01](https://github.com/bevyengine/bevy/commit/524fb01457378096bf08e6bc90b085816cd24844) <span style='color:grey;'>(significance=0.04)</span>
- Fix overflow in `RenderLayers::iter_layers` (#14264) [728c5b9](https://github.com/bevyengine/bevy/commit/728c5b98d4d1530ff86801cfb521af5e4c4dd246) <span style='color:grey;'>(significance=0.01)</span>
- Fix `bevy_window` failing with `serialize` feature (#14298) [70a0c21](https://github.com/bevyengine/bevy/commit/70a0c211ffcb6df7afd8ce645c43712c1d20d2e7) <span style='color:grey;'>(significance=0.01)</span>
- Fix error/typo in SMAA shader (#14338) [42412f3](https://github.com/bevyengine/bevy/commit/42412f35006607db0036f16829f3e4e4d4067042) <span style='color:grey;'>(significance=0.02)</span>
- Make `Viewport::default()` return a 1x1 viewport (#14372) [420ca6c](https://github.com/bevyengine/bevy/commit/420ca6c43c2d65d822b2f2c7da5e2808af867f4c) <span style='color:grey;'>(significance=0.06)</span>
- fix building cargo_gltf with feature dds (#14360) [295ed1f](https://github.com/bevyengine/bevy/commit/295ed1fdb4c0779da7c784b41ccc7996801eda0a) <span style='color:grey;'>(significance=0.02)</span>
- Fix incorrect function calls to hsv_to_rgb in render debug code. (#14260) [df3fcbd](https://github.com/bevyengine/bevy/commit/df3fcbd116fb38bdd8ee6cde2740a98290a61c86) <span style='color:grey;'>(significance=0.01)</span>
- Add some missing reflect attributes (#14259) [6882420](https://github.com/bevyengine/bevy/commit/6882420c7fc674742ac1161d52198a07fdf0e444) <span style='color:grey;'>(significance=0.03)</span>
- Fix single keyframe animations. (#14344) [2e577bc](https://github.com/bevyengine/bevy/commit/2e577bcdc9c09f18f4d06fe5f580e7ce26ff37dc) <span style='color:grey;'>(significance=0.04)</span>
- Fix `bevy_gltf` PBR features not enabling corresponding `bevy_pbr` flags (#14486) [2870d89](https://github.com/bevyengine/bevy/commit/2870d89d5ca28a1d3580d67630ee9659969cc11c) <span style='color:grey;'>(significance=0.02)</span>
- Handle 0 height in prepare_bloom_textures (#14423) [9daf16b](https://github.com/bevyengine/bevy/commit/9daf16bb870ff4ae4f50a8dda9cef350bef2a791) <span style='color:grey;'>(significance=0.03)</span>
- Fix `bevy_winit` not building with `serialize` feature (#14469) [c4ea477](https://github.com/bevyengine/bevy/commit/c4ea4776c419a44bfa49ad3e7f13a675d28d8d1a) <span style='color:grey;'>(significance=0.01)</span>
- Fix TextureCache memory leak and add is_empty() method (#14480) [680c994](https://github.com/bevyengine/bevy/commit/680c994100db29ab77b183ee8f6539d6fe6473d6) <span style='color:grey;'>(significance=0.02)</span>
- Fix breaking image 0.25.2 release. (#14421) [27cafda](https://github.com/bevyengine/bevy/commit/27cafdae9b4dd31b45e234279f9b4d3857721c7f) <span style='color:grey;'>(significance=0.03)</span>
- Fix `bevy_render`'s `image` dependency version (#14505) [587cffd](https://github.com/bevyengine/bevy/commit/587cffdcde0377a8c0191d41349f6cc26b5de372) <span style='color:grey;'>(significance=0.02)</span>
- Disabled usage of the POLYGON_MODE_LINE gpu feature in the examples (#14402) [0886e6a](https://github.com/bevyengine/bevy/commit/0886e6a302e8d74254fd3ec6ede5fd483e0220b7) <span style='color:grey;'>(significance=0.02)</span>
- fix issue with phantom ui node children (#14490) [ebfe545](https://github.com/bevyengine/bevy/commit/ebfe545f796a8d5073ad25d1832a6d983cb0e9e8) <span style='color:grey;'>(significance=0.01)</span>
- Properly handle repeated window close requests (#14573) [3a6176b](https://github.com/bevyengine/bevy/commit/3a6176b6cbf0952435cb3fc47f5e21215cfb95e0) <span style='color:grey;'>(significance=0.04)</span>
- fix asymmetrical 9-slicing (#14148) [d888640](https://github.com/bevyengine/bevy/commit/d8886408bf1af50d4eff660e07063a5541f31bb4) <span style='color:grey;'>(significance=0.02)</span>
- Skip batching for phase items from other pipelines (#14296) [833ee3f](https://github.com/bevyengine/bevy/commit/833ee3f577e973a9d4c40c23c9c3ff1aee94b4c7) <span style='color:grey;'>(significance=0.02)</span>
- clippy happy [c217238](https://github.com/bevyengine/bevy/commit/c217238c5e239cb7ac4d82a462c37fd24b084abf) <span style='color:grey;'>(significance=0.04)</span>
## ✨ feat
- bevy_input: allow use without bevy_reflect (#14167) [1bc5ecd](https://github.com/bevyengine/bevy/commit/1bc5ecda9b1a1828b61af30149bcd40a8cde82c7) <span style='color:grey;'>(significance=0.03)</span>
- feat: add insert_after and insert_startup_before (#13941) [61c683f](https://github.com/bevyengine/bevy/commit/61c683fb6a10240424f0905598ed94e1547a8492) <span style='color:grey;'>(significance=0.04)</span>
## 🔧 chore
- Release 0.14.1 [d65eb39](https://github.com/bevyengine/bevy/commit/d65eb39277c4f85749ba27460b8398f815ef3802) <span style='color:grey;'>(significance=0.00)</span>
