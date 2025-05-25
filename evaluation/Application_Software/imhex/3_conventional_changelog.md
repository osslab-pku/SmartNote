## [1.35.4](https://github.com/WerWolv/ImHex/compare/v1.35.3...v1.35.4) (2024-07-09)


### Bug Fixes

* Build issue due to uncaptured this pointer ([4d1e29d](https://github.com/WerWolv/ImHex/commit/4d1e29d7479178ac5baab9b8a0e8b2dac7170f79))
* Crash on macOS when dirtying or undirtying a provider from a thread ([22dc3c6](https://github.com/WerWolv/ImHex/commit/22dc3c65893f34a11787b8dc80b30e8b07e28400)), closes [#1799](https://github.com/WerWolv/ImHex/issues/1799)
* Hex editor popups getting transparent when hovering over combo box popup ([1c2bb0c](https://github.com/WerWolv/ImHex/commit/1c2bb0c04959549890d5d97d26c05b469f0fbcf5))
* Make sure welcome screen always stays in the background ([a0ca0e8](https://github.com/WerWolv/ImHex/commit/a0ca0e859694c41b1dcd562b4281adb7374cde8f))
* Multiple definitions errors with plugin features ([edb1a88](https://github.com/WerWolv/ImHex/commit/edb1a8876b5eb8cf6ba3840df3611203b91bfeac))
* Potential race condition with sorting in the pattern drawer ([dd8e702](https://github.com/WerWolv/ImHex/commit/dd8e7025d037b424caedb702571cb36f7a919528))
* Remove interactive help debug code ([d5a69d9](https://github.com/WerWolv/ImHex/commit/d5a69d9201878bd5b436c4631bba688c353543b6))
* Remove unnecessary touch padding ([0785270](https://github.com/WerWolv/ImHex/commit/0785270dfadb8d112c8c30d966b900fbe4fa1cc4))
* Updater executable not being launched correctly when path had spaces in it ([c922d9c](https://github.com/WerWolv/ImHex/commit/c922d9ceecb143b4793e3b84da448a8dd24a590d)), closes [#1780](https://github.com/WerWolv/ImHex/issues/1780)
* Wrong start/end offset and size for static array entries in pattern data view ([cfbc6e0](https://github.com/WerWolv/ImHex/commit/cfbc6e085a4dda0145321bd7e197b7b7f945be6c))