# Zulip Server 9.1
Released 2024-08-02

- Clarified upgrade notes and installer error messages. Improved documentation to smooth the process of upgrading Ubuntu 20.04 to 22.04 before upgrading to Zulip 9.x. Installations currently running Ubuntu 20.04 should first upgrade to the latest Zulip 8.x release, and then follow the [Zulip host OS upgrade instructions](https://zulip.readthedocs.io/en/latest/production/upgrade.html#upgrading-the-operating-system) in preparation for upgrading to Zulip 9.x.
- Improved web and mobile app loading times and bandwidth usage by tuning API response compression and removing some unnecessary entropy in user object payloads.
- Fixed how Zulip handles a GitHub quirk, to avoid duplicate notifications when pull request reviews are submitted.
- Fixed a rare race condition that could cause uploaded images to be displayed as a perpetual loading spinner.
- Fixed video player controls appearing in the lightbox bottom carousel.
- Fix several minor visual bugs, most notably with composebox typeahead overflowing incorrectly.
- Fixed a subtle live-update bug rerendering the inbox view.
- Fixed a couple of subtle performance issues involving the analytics cron job and listing invitations in organization settings.
- Updated documentation for a couple of integrations.
- Updated translations.