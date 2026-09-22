# moq.dev reading and editorial follow-up

Reviewed September 22, 2026. MOQT remains pinned to draft-21.

## Changes

- Added a brief WebRTC orientation immediately after the definition of MoQ. Kept the existing detailed comparison and its anchor, so the opening does not require learning ICE, SFUs, or codecs first.
- Used the 2023 Replacing WebRTC essay for its architectural motivation: applications need different buffering choices. Labeled its historical context rather than importing its old browser-support claims.
- Added demand-driven encoding to the relay chapter, with an application-owned startup example.
- Corrected the unconditional moq-lite group-per-stream description for its documented single-frame datagram option.
- Distinguished moq-lite media-timeline age from draft-21 hop-local timers.
- Made container parsing concrete with hang's timestamp prefix; retained codec/container separation.
- Added current gateway documentation and protocol/container observations to the experiment notebook.
- Added a question-led moq.dev reading route rather than an undirected source list.

## Review scope and boundaries

Read the concepts, transport, moq-lite, hang, standards, conferencing, distribution, RTC gateway, and clustering guides. Also reviewed Replacing WebRTC, Never Use Datagrams, QUIC Powers, and Forward Error Correction for possible gaps. The hang draft was consulted for catalog context.

The existing chapters already explain stream cancellation, congestion versus adaptation, per-viewer queues, codec configuration, and application-owned playback. Kept those explanations rather than adding parallel versions of the blog arguments.

Did not adopt categorical claims about datagrams, FEC, browser availability, audience limits, or relative performance. Did not equate QUIC connection migration with moving an application to another relay. These need their own qualified explanations and evidence; neither is required to explain the new passages.

Normative baseline checked against draft-21: delivery timers in section 5.2 remain distinct from implementation-specific media-age limits. New implementation details are explicitly attributed to moq.dev rather than presented as MOQT requirements.

## Validation

Build passed. Book checks passed for 14 pages and 642 local links/assets; SEO and whitespace checks passed. Reviewed the source diff. Browser inspection verified opening heading order and no page overflow at 390px on the opening and reference chapters. The upstream media demo is not executed by this editorial review.
