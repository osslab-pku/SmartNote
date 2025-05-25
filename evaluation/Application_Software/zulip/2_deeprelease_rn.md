
## Features

- Nginx : adjust default gzip level (#31212)
- Integrations_dev_panel : convert module to typescript (#31142)
- Message_events_util : convert module to typescript (#31145)
- Mypy : reenable explicit-override for models (#31223)
- Message_previews : simplify presentation of message previews (#31177)
- Help : message and compose actions illustrations (#31181)
- Settings : add group-based setting for who can create web-public streams (#31122)
- Integration-docs : update to the new format ( sentry and semaphore ) (#31038)
- Landing_page : convert module to typescript (#30899)

## BugFix

- Invitation performance fixes (#31197)
- Stream_list : fix handling of unsubscribing from last channel (#31175)
- Inbox_ui : fix row_focus not synced with inbox rows (#31226)
- Help center stage 1 (#30570)
- Setup make_stream function to create streams in node tests (#30831)
- Avoid repeated count queries (#31179)
- Modal_button : use negative outline-offset to compensate for scaling (#31124)
- Fix typeahead overflowing out of window (#31140)
- Complete : complete ` huddle ` to ` direct_message_group ` in non api files (#30766)
- Properly center icon for copying urls (#31178)
- Fix settings section when increasing screen width (#31184)
- Prevent duplicate pr review messages (#30848)
- Message_controls : add missing class to edit buttons (#31174)
- Rendered_markdown : lay out time spans with inline-flex (#31185)
- Listwidget : fix sliding of actions column in tables (#30700)
- Web : condense unnecessarily verbose function signatures (#31194)
- Delete incorrectly committed dump.rdb file (#31200)
- Compose : specify non-alpha message-area colors (#31217)
- Help : use message for global times examples (#31183)
- Lightbox : disable controls on video previews in lightbox (#31210)
- Thumbnail : resolve a race condition when rendering messages (#31186)

## Documentation

- Tweak : tweak server roadmap documentation (#31195)
- Fix up some paths and references in architecture-overview.md (#31149)
- Upgrade documentation fixes (#31187)
- Docs : note required os upgrade in upgrade notes (#31209)
- Rendered_markdown : remove universal selector for embedded content (#31158)
- Thumbnail : fix typo in comment (#31160)

## NonFunctional

- Input pill : refactor to move custom attributes into relevant modules (#31173)
- Endpoints : migrate to typed_endpoint (#31141)
- Message_controls : consolidate css ; clean clean up overly broad selectors (#31157)
- Upgrade python requirements (#31180)
- User_groups : migrate to (#30807)
- Migrate action functions to send event on commit (#31169)
- Remove the queue worker (#31196)
- Clients : drop `` desktop app '' substring check (#31211)
- Rendered_markdown : update markdown timestamps to use zulip icon (#31220)
- Better indexed join to analytics_usercount , using realm_id (#31171)
- Api docs : clarify event structure when moving channels (#31176)
- Users : reduce date_joined precision to minutes (#31190)
