# Release Notes for v0.28.0

## New Features and Enhancements
- **Admin Panel Enhancements**: 
  - Introduced enhanced user management features, including the ability to block automatic user registration and display active sessions in the admin panel. Admins can now disable user accounts and view the last request timestamp for better user activity monitoring. [#1658]
  - Redesigned the footer for a more modern look. [#1674]

- **File Selector Fragment**: 
  - Implemented conditional attribute binding for the `multiple` attribute, allowing dynamic behavior based on JavaScript variables. [#1665]

- **Translation Updates**:
  - Updated translations for Japanese, Brazilian Portuguese, and Italian languages to improve accuracy and coverage. [#1654, #1673, #1661]

- **Tessdata Availability**: 
  - Made tessdata available to local Windows users, enhancing the usability of OCR features. [#1677]

## Dependency Updates
- Upgraded several dependencies to their latest versions for improved performance and security:
  - `org.apache.pdfbox:xmpbox` to 3.0.3
  - `io.github.pixee:java-security-toolkit` to 1.2.0
  - `org.projectlombok:lombok` to 1.18.34
  - `com.bucket4j:bucket4j_jdk17-core` to 8.13.1
  - `org.springframework:spring-webmvc` to 6.1.12
  - `ch.qos.logback:logback-classic` to 1.5.7
  - `com.github.jk1.dependency-license-report` to 2.9
  - `io.micrometer:micrometer-core` to 1.13.3
  - `edu.sc.seis.launch4j` to 3.0.6

## Bug Fixes
- Fixed an issue with the conditional attribute binding in the file selector fragment, ensuring the `multiple` attribute is dynamically set based on JavaScript variables. [#1665]
- Resolved a bug that prevented SSO login due to faulty verification. [#1658]

## Code Quality and Maintenance
- Updated build configurations and workflows to streamline the development process, including enhancements to the auto-labeler and build scripts. [#1693]
- Improved logging and error handling across various components for better debugging and maintenance.

## Documentation
- Updated the README to reflect the latest translation progress and other minor documentation improvements. [#1651, #1655, #1675]

This release focuses on enhancing user management capabilities, improving translation accuracy, and updating dependencies to ensure the application remains secure and efficient. The admin panel now offers more control over user sessions and registration, while the redesigned footer and updated translations contribute to a better user experience.