# Content refinement

Reviewed the introduction and all 13 chapters for explanatory gaps, misleading inferences, repetition, and awkward prose. Updated the introduction and 11 chapters.

## Corrections and additions

- Replaced a debugging question that treated increasing frame age as evidence of a queue problem. A frozen picture ages under several different failures; the replacement checks decoded frames waiting past their scheduled display times.
- Clarified that the arrival-to-display example includes parsing and decoding, which must finish before presentation.
- Added catch-up arithmetic: matching source bitrate to capacity stops queue growth but does not drain a backlog. Dropping old content once cannot fix a continuing rate mismatch.
- Added session recovery and planned shutdown, with a draft-21 reference for GOAWAY, plus a disconnect experiment in the walkthrough.
- Added cryptographic token validation before trusting JWT claims and distinguished credential expiry from the lifetime of accepted subscriptions.
- Qualified payload descriptions to include subscription end markers and added scope to the glossary.
- Changed the WebRTC comparison's direct-connection row to connectivity: TURN supplies a relayed path.
- Shortened repeated introductions and table summaries; corrected the claim that a player alone supplies the capture path.

## Sources checked

- MOQT draft-21, particularly sections 6.6.1 and 11.1.2.
- RFC 8725 for token validation.
- W3C WebCodecs for the decoding/presentation boundary.
- moq.dev hang and quick-start documentation for context.

The protocol baseline remains draft-21. No upstream demo or interoperability test was run.

## Validation

Rebuilt the tracked static output. Book checks passed for all 14 pages and 656 local links/assets; SEO and whitespace checks passed. Inspected the rendered latency explanation in the local browser, then split the longer worked-example paragraph for readability.
