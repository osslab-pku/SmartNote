# v0.28.0
## 🐛 fix
- Fixed a bug in the file selector fragment to ensure the "multiple" attribute is correctly bound based on the provided condition, improving file input functionality. [#1665](https://github.com/Stirling-Tools/Stirling-PDF/pull/1665) <span style='color:grey;'>(significance=0.25)</span>

## ✨ feat
- Enhanced user management in the admin panel: 
  - Prevent SSO login due to faulty verification
  - Improved error message display
  - Introduced user status management
  - Block SSO login without prior admin registration
  - Enable or disable users
  - New indicators for active and disabled users
  - Added support for multiple languages [#1658](https://github.com/Stirling-Tools/Stirling-PDF/pull/1658) <span style='color:grey;'>(significance=0.33)</span>
- The tessdata directory is now configurable for local Windows users. Updated OCRController and OtherWebController classes to use the new tessdataDir property from ApplicationProperties. ApplicationProperties class and settings.yml.template file now include tessdataDir configuration. [#1677](https://github.com/Stirling-Tools/Stirling-PDF/pull/1677) <span style='color:grey;'>(significance=0.21)</span>

## 🔧 chore
- Updated `java-security-toolkit` dependency from version 1.1.3 to 1.2.0. [#1667](https://github.com/Stirling-Tools/Stirling-PDF/pull/1667) <span style='color:grey;'>(significance=0.24)</span>
- Minor version bump for `ch.qos.logback:logback-classic` and `ch.qos.logback-core` dependencies. [#1685](https://github.com/Stirling-Tools/Stirling-PDF/pull/1685) <span style='color:grey;'>(significance=0.29)</span>
- Updated the configuration file to limit the number of open pull requests. [909054a](https://github.com/Stirling-Tools/Stirling-PDF/commit/909054a49d8b3befa25d81682e9ab7528cbea257) <span style='color:grey;'>(significance=0.21)</span>
- Updated the dependabot configuration file to set the rebase strategy to "auto" for the weekly update schedule. [6fa7c2e](https://github.com/Stirling-Tools/Stirling-PDF/commit/6fa7c2e5e128b23658ea6203444f46b2bae89b95) <span style='color:grey;'>(significance=0.21)</span>
- Updated Lombok library version. [#1684](https://github.com/Stirling-Tools/Stirling-PDF/pull/1684) <span style='color:grey;'>(significance=0.19)</span>
- Updated 3rd Party Licenses to include "org.apache.pdfbox:jbig2-imageio" module. [#1698](https://github.com/Stirling-Tools/Stirling-PDF/pull/1698) <span style='color:grey;'>(significance=0.18)</span>
- Updated build configuration to use common version variables for dependencies. [#1697](https://github.com/Stirling-Tools/Stirling-PDF/pull/1697) <span style='color:grey;'>(significance=0.13)</span>
- Enhanced license update workflow to include auto-approval for new pull requests. Updated auto-merge functionality to use the latest version of the relevant action. [ea2d755](https://github.com/Stirling-Tools/Stirling-PDF/commit/ea2d7558081b9ce62acf994ad60fc5c6a9b2e17d) <span style='color:grey;'>(significance=0.12)</span>
- Localization updates for Italian: titles, descriptions, and tags for the "Remove image" feature in the home section. [#1661](https://github.com/Stirling-Tools/Stirling-PDF/pull/1661) <span style='color:grey;'>(significance=0.14)</span>
- Updated third-party licenses. [#1687](https://github.com/Stirling-Tools/Stirling-PDF/pull/1687) <span style='color:grey;'>(significance=0.11)</span>
- Updated third-party licenses. [#1695](https://github.com/Stirling-Tools/Stirling-PDF/pull/1695) <span style='color:grey;'>(significance=0.11)</span>
- Updated GitHub Actions workflows: revised build and auto-labeler configurations, removed test workflow, and added new steps to the build process for improved automation and efficiency. [#1693](https://github.com/Stirling-Tools/Stirling-PDF/pull/1693) <span style='color:grey;'>(significance=0.11)</span>
- Modified 3rd Party Licenses: adjusted module versions for "ch.qos.logback:logback-classic" and "ch.qos.logback-core". [#1696](https://github.com/Stirling-Tools/Stirling-PDF/pull/1696) <span style='color:grey;'>(significance=0.15)</span>

## 🔨 build
- Minor update to build configuration. [#1686](https://github.com/Stirling-Tools/Stirling-PDF/pull/1686) <span style='color:grey;'>(significance=0.16)</span>

## 🛠️ refactor
- Minor improvements and bug fixes. [#1670](https://github.com/Stirling-Tools/Stirling-PDF/pull/1670) <span style='color:grey;'>(significance=0.20)</span>
- Minor patch to the Spring Web MVC framework. [#1680](https://github.com/Stirling-Tools/Stirling-PDF/pull/1680) <span style='color:grey;'>(significance=0.20)</span>
- Minor improvements and bug fixes. [#1689](https://github.com/Stirling-Tools/Stirling-PDF/pull/1689) <span style='color:grey;'>(significance=0.20)</span>
- Minor improvements and bug fixes. [#1691](https://github.com/Stirling-Tools/Stirling-PDF/pull/1691) <span style='color:grey;'>(significance=0.11)</span>