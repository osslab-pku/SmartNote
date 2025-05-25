![](https://img.shields.io/github/downloads/marticliment/wingetui/3.1.1/total?style=for-the-badge)

# Changelog
 - **PowerShell 7** PSGet is anailable as a package manager.
 - WinGet now uses the COM API to fetch installed packages. Bundled WinGet can be used instead of the PowerShell Module
 - Improved compatibility for non-ascii characters on WinGet.
 - The **Package Bundles** page has been rebuilt in the same way the other Software Pages were improved in 3.1.0.
 - Improvements to UI Icons. They are not loaded from disk anymore, increasing the smoothness and responsiveness of the UI.
 - WinGet and Scoop icons have been changed so they are coherent with their official icons.
 - Other changes and bugfixes

## What's Changed
* Make WingetUI to UniGetUI by @skanda890 in https://github.com/marticliment/UniGetUI/pull/2353
* Fix typo "Naive" -> "Native" by @headquarter8302 in https://github.com/marticliment/UniGetUI/pull/2401
* Update Issue and Pull Request templates by @skanda890 in https://github.com/marticliment/UniGetUI/pull/2406
* Use different encoding code pages depending on the user's locale by @marticliment in https://github.com/marticliment/UniGetUI/pull/2439
* Add back bundled winget compatibility by @marticliment in https://github.com/marticliment/UniGetUI/pull/2440
* WinGet COM API to fetch installed packages and available updates by @marticliment in https://github.com/marticliment/UniGetUI/pull/2451
* update installation via winget in ReadMe by @a-mnich in https://github.com/marticliment/UniGetUI/pull/2475
* Update scoop_cleanup.cmd so that its output can be reviewed by @redactedscribe in https://github.com/marticliment/UniGetUI/pull/2482
* Fix unable to open link by @MSDNicrosoft in https://github.com/marticliment/UniGetUI/pull/2483
* Update README.md, CONTRIBUTING.md, and PULL_REQUEST_TEMPLATE.md by @skanda890 in https://github.com/marticliment/UniGetUI/pull/2493
* Update icons and screenshots from the excel file by @github-actions in https://github.com/marticliment/UniGetUI/pull/2509
* Shared Assembly Info by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2512
* Add missing implicit usings by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2511
* Update Funding.yml, and PULL_REQUEST_TEMPLATE.md by @skanda890 in https://github.com/marticliment/UniGetUI/pull/2510
* Update nugets. Fix consolidate by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2516
* Code style + small performance improvements by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2517
* Add PowerShell 7.x Support by @marticliment in https://github.com/marticliment/UniGetUI/pull/2525
* Add modified EditorConfig from Microsoft official aspnetcore repo by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2518
* Remove `SupportedOsPlatformVersion` tag in csproj files by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2526
* Fix some warnings by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2527
* Fix CA1823: Avoid unused private fields by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2529
* Migrate icons from .png to FontIcon, UI Controls refactoring, for faster and smoother UI by @marticliment in https://github.com/marticliment/UniGetUI/pull/2530
* Create interfaces for Package and PackageManager, migrate PackageBundlesPage to new page type by @marticliment in https://github.com/marticliment/UniGetUI/pull/2352
* Fix warnings + fix typos by @Saibamen in https://github.com/marticliment/UniGetUI/pull/2531
* Update translations from Tolgee by @github-actions in https://github.com/marticliment/UniGetUI/pull/2548

## New Contributors
* @headquarter8302 made their first contribution in https://github.com/marticliment/UniGetUI/pull/2401
* @a-mnich made their first contribution in https://github.com/marticliment/UniGetUI/pull/2475
* @redactedscribe made their first contribution in https://github.com/marticliment/UniGetUI/pull/2482
* @MSDNicrosoft made their first contribution in https://github.com/marticliment/UniGetUI/pull/2483
* @Saibamen made their first contribution in https://github.com/marticliment/UniGetUI/pull/2512

**Full Changelog**: https://github.com/marticliment/UniGetUI/compare/3.1.0...3.1.1

SHA256: `dc03f02df89f23f6f0afa47b8b8830a81516d3d5d83095c1da5c59760950c758`