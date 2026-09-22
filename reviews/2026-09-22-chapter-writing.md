# Chapter structure and writing — September 22, 2026

Applied the author's feedback after comparing the opening and teaching approach of [WebRTC for the Curious](https://webrtcforthecurious.com/docs/01-what-why-and-how/), including its [signaling chapter](https://webrtcforthecurious.com/docs/02-signaling/). The changes use original prose and the existing MoQ examples.

## Reader-facing changes

- Chapter 01 now defines MoQ directly, explains its motivation, and develops connect/discover/request/deliver/present before the WebRTC comparison. Each activity points to the chapters that explain it. A chapter guide makes the expected learning outcomes explicit. Removed one redundant distribution diagram while retaining the illustrated version.
- Chapters 02–10 introduce their subject and route through the explanation before the details. The existing TCP/IP skip link and optional packet-detail route remain.
- Chapters 03 and 05–08 use specific question headings with the original section anchors preserved. Definitions and examples lead into mechanisms and limitations. Chapter 03 clarifies the subgroup definition, chapter 06 qualifies how much production must fall to stop queue growth, and chapter 07 defines encoded chunks.
- Chapter 05 explains forwarding metadata before caching. Chapter 08 puts the access-policy example before credential representation. Chapter 09 explains the frame path before the demo commands.
- Chapter 10 retains its diagnostic diagram and worked example. The FAQ explains how to use it and starts the WebRTC answer directly. Glossary groups are alphabetized; the references begin with the question-to-source guide.
- The introduction and contributor README now describe the same reading route and chapter-writing expectations.

## Verification

Quarto rebuilt all 14 pages. Book checks passed 629 local links/assets; SEO and whitespace checks passed. Source and generated diff review checked the reordered passages, transitions, and first-use definitions. All previous chapter section anchors and external source URLs remain. All code and diagram blocks remain unchanged except the deliberately removed duplicate diagram in chapter 01. Chapter em-dash counts did not increase.

Browser checks covered desktop chapter 01 and all 13 chapters at a 390-pixel viewport. The chapter guide was changed from a scrolling table to a wrapping list after narrow-screen inspection. No page-wide horizontal overflow was observed, and expected Mermaid diagrams rendered.

The MOQT baseline remains draft-21. The overview preserves overlap between activities rather than claiming a mandatory sequence of round trips. This is a writing and structure review, not a fresh exhaustive protocol audit or an execution of the upstream demo.
