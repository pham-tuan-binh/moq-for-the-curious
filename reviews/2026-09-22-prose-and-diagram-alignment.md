# Prose and diagram alignment

Reviewed the README, introduction, and all 13 chapters for the pattern the author flagged: vague attribution, abstract descriptions of what an explanation does, and closing sentences that repeat the paragraph. Revised 31 passages across 13 files, in addition to the previously corrected Replacing WebRTC sentence. The FAQ and glossary did not need edits in this pass.

Examples:

- “gives useful background on that architectural problem” became “explains why streaming systems often combine several protocols.”
- “The chapter's pipeline then provides a way to investigate a failure” became specific checks for the media description, starting picture, decoding, and display.
- “A network of these relationships provides distribution across regions” became “Viewers in each region can receive content from their local relay.”
- Removed redundant final sentences from the introduction, README draft recommendation, and relay deployment advice.

Kept concrete uses of words such as “through” and “useful,” including descriptions of actual network paths and media that can still be decoded. These words alone are not the problem.

## Diagrams

- Centered the lecture illustration's labels on their boxes with consistent line spacing. Aligned the legend text with its color keys and the footer note with the right margin.
- Replaced the excessively wide nested packet flowchart with selectable, vertically nested HTML fields. Preserved the containment relationships and field descriptions.
- Wait for the reading font before measuring Mermaid labels. Limit diagram reduction to 80% so 15px labels remain at least 12px; wider diagrams scroll inside their containers.
- Give the lecture illustration a minimum display width so phone layouts scroll instead of shrinking its labels below readability.

## Validation

Rebuilt static output. Book checks passed for 14 pages and 662 local links/assets. SEO and whitespace checks passed. Inspected the illustration and packet layout visually, including the packet layout at a 390px viewport. Checked all nine chapters containing Mermaid diagrams at that width: all 17 diagrams rendered, no page overflow, and measured flowchart label centers were within two pixels of their rectangular node centers. Restored the browser viewport after testing.

The earlier Cloudflare and MoQ Alliance resource additions remain in the working tree. No push was made in this pass.
