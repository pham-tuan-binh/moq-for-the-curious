# Transport and introductory model audit — 2026-09-22

Scope: every paragraph, table, byte example and diagram in chapters 01–03. Read the actual pinned MOQT draft-21 and the primary sources below, not search summaries. This is a specification review, not interoperability or performance testing.

## Corrections applied

- Chapter 02 distinguished link MTU from path MTU. The old sentence conflated them. [RFC 8200 §5](https://www.rfc-editor.org/rfc/rfc8200.html#section-5).
- Qualified the bit table as base QUIC v1, and documented the negotiated fixed-bit exception. Without this qualification the table could mislead packet-capture readers. [RFC 9287 §3](https://www.rfc-editor.org/rfc/rfc9287.html#section-3).
- Explained that Initial protection uses publicly derivable keys and does not provide confidentiality against observers. Handshake/application protection is different. [RFC 9001 §5](https://www.rfc-editor.org/rfc/rfc9001.html#section-5).
- Described short headers as 1-RTT packets rather than requiring an already established connection; application transmission can precede handshake confirmation.
- Qualified subgroup-to-stream mapping: subscription delivery normally uses one stream per subgroup, with reset/out-of-order exceptions; different subgroups cannot share a subscription stream. [MOQT §2.2](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-21#section-2.2).
- Reworked chapter 01's comparison into browser responsibilities, connectivity/distribution, practical requirements, and coexistence. Added firsthand gateway and operator reading, explicitly distinguishing historical draft material and practitioner assessments from standards.

## Verified unchanged

| Claim or artifact | Evidence reviewed | Result |
|---|---|---|
| Independent ordered streams, stream IDs, no write/read message boundary equivalence | [RFC 9000 §§2–2.2](https://www.rfc-editor.org/rfc/rfc9000.html#section-2) | Accurate; shared connection limits already explained |
| Connection and stream flow control | [RFC 9000 §4.1](https://www.rfc-editor.org/rfc/rfc9000.html#section-4.1) | Accurate |
| Packet/frame containment, coalescing, retransmission under a fresh packet number | [RFC 9000 §§12–13](https://www.rfc-editor.org/rfc/rfc9000.html#section-12) | Diagrams and distinction valid |
| Short-header bit order and 0x41 example | [RFC 9000 §17.3.1](https://www.rfc-editor.org/rfc/rfc9000.html#section-17.3.1) | Bit masks and two-byte packet-number result correct |
| Varint capacities and 37/64 examples | [RFC 9000 §16](https://www.rfc-editor.org/rfc/rfc9000.html#section-16) | Arithmetic checked: 6/14/30/62 usable bits |
| STREAM wire table and 0e 02 00 03 61 62 63 | [RFC 9000 §19.8](https://www.rfc-editor.org/rfc/rfc9000.html#section-19.8) | OFF and LEN set; FIN unset; client-unidirectional stream 2; offset 0; three ASCII payload bytes |
| TLS handshake sequence and early application traffic caveat | [RFC 9001 §4](https://www.rfc-editor.org/rfc/rfc9001.html#section-4), [RFC 9000 §7.1](https://www.rfc-editor.org/rfc/rfc9000.html#section-7.1) | Correct fresh certificate-authenticated flow; ACK/Retry/resumption omissions disclosed |
| DATAGRAM reliability, congestion control, no transport fragmentation | [RFC 9221 §5](https://www.rfc-editor.org/rfc/rfc9221.html#section-5) | Accurate |
| TCP/UDP comparison | [RFC 9293](https://www.rfc-editor.org/rfc/rfc9293.html), [RFC 768](https://www.rfc-editor.org/rfc/rfc768.html) | Correct service distinction; no speed ranking |
| ICE/STUN/TURN versus SFU | [RFC 8835 §3.4](https://www.rfc-editor.org/rfc/rfc8835.html#section-3.4), [RFC 7667 §3.7](https://www.rfc-editor.org/rfc/rfc7667.html#section-3.7) | Correct roles |
| Browser responsibilities | [W3C WebRTC](https://www.w3.org/TR/webrtc/), [W3C WebTransport](https://www.w3.org/TR/webtransport/) | Protocol versus browser API distinction valid |
| Object identity, payload immutability, namespace bytes and scope | [MOQT §§2.1–2.5](https://datatracker.ietf.org/doc/html/draft-ietf-moq-transport-21#section-2) | Accurate |
| Keyframe group diagram and layered subgroup example | Same draft §2 and §2.3 | Explicit examples, not universal codec mapping; independence is a recommendation |
| Group IDs are not timestamps; restart needs noncolliding identities | Same draft §§2.3.1, 2.5 | Accurate |
| Publisher/subscriber are roles; direct QUIC and WebTransport mappings | Same draft §§1.3, 6.2 | Accurate |
| September 8, 2026 draft-21 date and draft status | Draft title block | Verified |
| moq-lite terminology and group streams | [Project documentation](https://doc.moq.dev/concept/moq-lite) | Matches current documentation |
| WebSocket fallback shares TCP ordering | [Project transport documentation](https://doc.moq.dev/concept/transport) | Matches documented fallback; implementation-specific label retained |

## Limits and contextual reading

No claims of benchmarked latency, browser compatibility completeness, or verified production capacity were added. Example byte sequences are illustrative, not captured traffic. Keyframe examples assume a usable random-access point and available decoder configuration, as stated in the chapter. Draft-21 remains the edition's baseline; this audit does not claim it is the latest draft.

[Meetecho's 2024 demonstration](https://www.meetecho.com/blog/moq-webrtc/) supports coexistence/gateway architecture only, not draft-21 wire behavior. [Cloudflare](https://blog.cloudflare.com/moq/) provides an operator's motivation, and [webrtcHacks](https://webrtchacks.com/webrtc-vs-moq-by-use-case/) provides practitioner assessment. Neither is used as authority for packet fields, protocol requirements, or promised performance.
