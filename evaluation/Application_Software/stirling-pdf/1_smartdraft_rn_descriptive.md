# v0.28.0
## 🐛 fix
- Fixed a bug in the conditional binding of the "multiple" attribute in the file selector fragment, ensuring correct functionality of the file input element. [#1665](https://github.com/Stirling-Tools/Stirling-PDF/pull/1665) <span style='color:grey;'>(significance=0.25)</span>

## ✨ feat
- Enhanced admin panel with improved user management: enable/disable users, better SSO login handling. Updated translations and clearer error messages. [#1658](https://github.com/Stirling-Tools/Stirling-PDF/pull/1658) <span style='color:grey;'>(significance=0.33)</span>
- Ensures tessdata availability for local Windows users by introducing a configurable tessdata directory path. [#1677](https://github.com/Stirling-Tools/Stirling-PDF/pull/1677) <span style='color:grey;'>(significance=0.21)</span>

## 🔧 chore
- Updated java-security-toolkit dependency to improve security features. [#1667](https://github.com/Stirling-Tools/Stirling-PDF/pull/1667) <span style='color:grey;'>(significance=0.24)</span>
- Minor patch to the logback-classic library, enhancing logging framework stability and performance. [#1685](https://github.com/Stirling-Tools/Stirling-PDF/pull/1685) <span style='color:grey;'>(significance=0.29)</span>
- Updated `dependabot.yml` to limit open pull requests to a maximum of 10. Set Dependabot rebase strategy to "auto" in the configuration file. [909054a](https://github.com/Stirling-Tools/Stirling-PDF/commit/909054a49d8b3befa25d81682e9ab7528cbea257) [6fa7c2e](https://github.com/Stirling-Tools/Stirling-PDF/commit/6fa7c2e5e128b23658ea6203444f46b2bae89b95) <span style='color:grey;'>(significance=0.21)</span>
- Updated org.apache.pdfbox:xmpbox, org.springframework:spring-webmvc, io.micrometer:micrometer-core, and org.apache.pdfbox:pdfbox dependencies. [#1670](https://github.com/Stirling-Tools/Stirling-PDF/pull/1670) [#1680](https://github.com/Stirling-Tools/Stirling-PDF/pull/1680) [#1689](https://github.com/Stirling-Tools/Stirling-PDF/pull/1689) [#1691](https://github.com/Stirling-Tools/Stirling-PDF/pull/1691) <span style='color:grey;'>(significance=0.20)</span>
- Minor version bump for the com.github.jk1.dependency-license-report plugin. [#1690](https://github.com/Stirling-Tools/Stirling-PDF/pull/1690) <span style='color:grey;'>(significance=0.20)</span>
- Includes improvements and bug fixes from the latest Lombok library version. [#1684](https://github.com/Stirling-Tools/Stirling-PDF/pull/1684) <span style='color:grey;'>(significance=0.19)</span>
- Added "org.apache.pdfbox:jbig2-imageio" to third-party licenses. [#1698](https://github.com/Stirling-Tools/Stirling-PDF/pull/1698) <span style='color:grey;'>(significance=0.18)</span>
- Updated project configuration and build configuration to use common version variables for dependencies. [#1686](https://github.com/Stirling-Tools/Stirling-PDF/pull/1686) [#1697](https://github.com/Stirling-Tools/Stirling-PDF/pull/1697) <span style='color:grey;'>(significance=0.16)</span>
- Modified 3rd Party Licenses: adjusted module versions for "ch.qos.logback:logback-classic" and "ch.qos.logback:logback-core". [#1696](https://github.com/Stirling-Tools/Stirling-PDF/pull/1696) <span style='color:grey;'>(significance=0.15)</span>
- Localization update for Italian, improving the "Remove image" feature description in the home section. [#1661](https://github.com/Stirling-Tools/Stirling-PDF/pull/1661) <span style='color:grey;'>(significance=0.14)</span>
- Enhanced workflow for updating licenses to include automatic approval and auto-merge for new pull requests. [ea2d755](https://github.com/Stirling-Tools/Stirling-PDF/commit/ea2d7558081b9ce62acf994ad60fc5c6a9b2e17d) <span style='color:grey;'>(significance=0.12)</span>
- Updated the 3rd Party Licenses file. [#1687](https://github.com/Stirling-Tools/Stirling-PDF/pull/1687) [#1695](https://github.com/Stirling-Tools/Stirling-PDF/pull/1695) <span style='color:grey;'>(significance=0.11)</span>
- Updated GitHub Actions workflows to enhance CI/CD pipeline automation and efficiency. [#1693](https://github.com/Stirling-Tools/Stirling-PDF/pull/1693) <span style='color:grey;'>(significance=0.11)</span>