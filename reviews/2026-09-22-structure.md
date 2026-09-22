# Structural follow-up — September 22, 2026

Read the chapter sources and existing September audits. The linked ChatGPT preview contained only the handoff exchange; its earlier editorial decisions were unavailable. This pass therefore follows the repository’s writing standards and recorded review criteria, rather than claiming to reproduce unseen decisions.

## Changes

- Chapter 02 now finishes the conceptual route through loss, cancellation, datagrams, security, WebTransport, and fallback before the packet and handshake detail. The loss example immediately follows independent streams. A link lets first-time readers continue to the object model and return to packet fields later. Existing diagrams, byte examples, headings, and anchors are retained.
- Chapter 04 introduces session setup before discovery and subscription. Its early-arrival paragraph now distinguishes recommended buffering from permitted request-stream reset, checked directly against [draft-21 §6.3](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-21#section-6.3). The existing explanation that exchanges can overlap remains.
- Chapter 09 removes a redundant opening and makes clear that the final Nix command starts the demo; the preceding Git command only reports the revision. The warning that the walkthrough has not been executed remains.
- Chapter 10 includes publication/track discovery in its diagnostic diagram and accessible description, matching the prose investigation sequence.

## Validation

Quarto rebuilt all 14 pages. Book checks passed 598 local links/assets; SEO checks passed. Diff review verified that all changed chapters retain their headings and that chapter 02 retains every diagram and HTML figure unchanged. Browser inspection confirmed the packet-section navigation and desktop layout, and the expanded debugging diagram rendered on a 390-pixel viewport without horizontal page overflow.

This is an editorial follow-up with a targeted draft check, not a new interoperability test or exhaustive technical recertification. Generated HTML and search content are included with the sources.
