# v1.35.4
## ✨ feat
- impr: Further try to improve window resize flickering on Windows [ad235fa](https://github.com/WerWolv/ImHex/commit/ad235fad25ddb1e355c4843f732b9df0799db345) <span style='color:grey;'>(significance=0.16)</span>
- impr: Improved size display in pattern data view [c7c4eca](https://github.com/WerWolv/ImHex/commit/c7c4ecad6dfce1f1e6629d8b1e8b96960c7573e4) <span style='color:grey;'>(significance=0.15)</span>
- web: Improved canvas webgl creation logic [3b79938](https://github.com/WerWolv/ImHex/commit/3b799388c25db45855688deb55f4648fb62ee7a3) <span style='color:grey;'>(significance=0.10)</span>
- impr: Added nicer console warning when .NET runtime isn't installed [dd0204f](https://github.com/WerWolv/ImHex/commit/dd0204f31df334f3424faaa27d2ed648f30bc965) <span style='color:grey;'>(significance=0.26)</span>
- web: Trigger right click when long touching area [5d53417](https://github.com/WerWolv/ImHex/commit/5d534176830fda39aee0b912fe4f5997ceb083cf) <span style='color:grey;'>(significance=0.40)</span>
- impr: Make highlight hovering more efficient [2757075](https://github.com/WerWolv/ImHex/commit/2757075a10cb9c6ac95ec83259859473765c4732) <span style='color:grey;'>(significance=0.17)</span>
## 🐛 fix
- impr: Prevent canvas flickering in web build [b305adb](https://github.com/WerWolv/ImHex/commit/b305adb2866b3d6291ff4c5db0b2ae5186934263) <span style='color:grey;'>(significance=0.27)</span>
- web: Fix ImHex logo and progress bar default fill [67930cf](https://github.com/WerWolv/ImHex/commit/67930cf65de72db95d913a25895a9c938f86d9a7) <span style='color:grey;'>(significance=0.15)</span>
- impr: Completely eradicate Window resize flickering on Windows [5fced6b](https://github.com/WerWolv/ImHex/commit/5fced6bb63b8858611383639d0de0c873557fcba) <span style='color:grey;'>(significance=0.13)</span>
- impr: Added Boost.Regex to about page [c6fc26e](https://github.com/WerWolv/ImHex/commit/c6fc26e2e75ecc0a4a9f5c331bfcf80843957721) <span style='color:grey;'>(significance=0.14)</span>
- fix: Potential race condition with sorting in the pattern drawer [dd8e702](https://github.com/WerWolv/ImHex/commit/dd8e7025d037b424caedb702571cb36f7a919528) <span style='color:grey;'>(significance=0.25)</span>
- impr: Disable tab overlines [6784678](https://github.com/WerWolv/ImHex/commit/6784678ff0aca040491fa8a374ab46b36768a9d2) <span style='color:grey;'>(significance=0.23)</span>
- fix: Remove interactive help debug code [d5a69d9](https://github.com/WerWolv/ImHex/commit/d5a69d9201878bd5b436c4631bba688c353543b6) <span style='color:grey;'>(significance=0.13)</span>
- impr: Added tooltips to toolbar buttons [a45d30e](https://github.com/WerWolv/ImHex/commit/a45d30edcaa282c5be5635df9d2b7ccb6dc58a51) <span style='color:grey;'>(significance=0.15)</span>
- fix: Wrong start/end offset and size for static array entries in pattern [cfbc6e0](https://github.com/WerWolv/ImHex/commit/cfbc6e085a4dda0145321bd7e197b7b7f945be6c) <span style='color:grey;'>(significance=0.16)</span>
- web: Fix touch input [1d99f85](https://github.com/WerWolv/ImHex/commit/1d99f8534ddfe89998673881e7eb330091529e2f) <span style='color:grey;'>(significance=0.24)</span>
- fix: Make sure welcome screen always stays in the background [a0ca0e8](https://github.com/WerWolv/ImHex/commit/a0ca0e859694c41b1dcd562b4281adb7374cde8f) <span style='color:grey;'>(significance=0.14)</span>
- web: Improve logo size on mobile [84999d5](https://github.com/WerWolv/ImHex/commit/84999d5c068467ea97a7bb120dc22bd383bd9d26) <span style='color:grey;'>(significance=0.17)</span>
- fix: Remove unnecessary touch padding [0785270](https://github.com/WerWolv/ImHex/commit/0785270dfadb8d112c8c30d966b900fbe4fa1cc4) <span style='color:grey;'>(significance=0.25)</span>
- web: Fix canvas to the top left of the screen [c79321b](https://github.com/WerWolv/ImHex/commit/c79321b550f8d0f6dccaaee8ab3cabec65abc773) <span style='color:grey;'>(significance=0.24)</span>
- fix: Hex editor popups getting transparent when hovering over combo box [1c2bb0c](https://github.com/WerWolv/ImHex/commit/1c2bb0c04959549890d5d97d26c05b469f0fbcf5) <span style='color:grey;'>(significance=0.30)</span>
- fix: Crash on macOS when dirtying or undirtying a provider from a thread [22dc3c6](https://github.com/WerWolv/ImHex/commit/22dc3c65893f34a11787b8dc80b30e8b07e28400) <span style='color:grey;'>(significance=0.12)</span>
- impr: Disable pattern debug mode after evaluation has finished [8a4599f](https://github.com/WerWolv/ImHex/commit/8a4599feeadc7432462fd946d8009df3c5430557) <span style='color:grey;'>(significance=0.24)</span>
- fix: Multiple definitions errors with plugin features [edb1a88](https://github.com/WerWolv/ImHex/commit/edb1a8876b5eb8cf6ba3840df3611203b91bfeac) <span style='color:grey;'>(significance=0.26)</span>
## 🔧 chore
- patterns: Updated pattern language [c2f661f](https://github.com/WerWolv/ImHex/commit/c2f661f02146d782120e9e89835be391aa04f1ee) <span style='color:grey;'>(significance=0.11)</span>
- git: Update Mesa3D link for Windows NoGPU version [32e2ccb](https://github.com/WerWolv/ImHex/commit/32e2ccbca004d5b6ba62cb47a53f103c2b5d45a9) <span style='color:grey;'>(significance=0.19)</span>
## 📦 build
- build: Update nativefiledialog and keep dialogs on top (#1771) [5a053aa](https://github.com/WerWolv/ImHex/commit/5a053aa146acd8e2dd06174faa5b7002f29d32dc) <span style='color:grey;'>(significance=0.15)</span>
- build: Streamline definition on plugin features [f8f4701](https://github.com/WerWolv/ImHex/commit/f8f47012c4c1e4b299cb48e46ef3b783b2422df2) <span style='color:grey;'>(significance=0.54)</span>
- build: Fix lzma support and simplify zstd building [cb406ea](https://github.com/WerWolv/ImHex/commit/cb406ea35728498e1d42b6b5d936d40900d9ce51) <span style='color:grey;'>(significance=0.12)</span>