# Writing Feedback — ZHAO Zhan (趙展)

## Feedback on ZHAO Zhan's First Draft: Introduction and Literature Review

**Student:** ZHAO Zhan (趙展)
**Topic:** Efficient Execution Frameworks for Structured LLM Programs
**Date:** 2 March 2026
**Reviewer:** Simon Wang (with AI-assisted analysis)

**Your draft:** writing/writingSampleCollection/firstDraft.md
**Your reflection:** writing/writingSampleCollection/firstDraft.md (reflection section)
**Your comments:** writing/writingSampleCollection/comments.md
**Assessment rubric:** writing/assessment/writing_instructions_formatted.md

---

## Overall Assessment

This is one of the stronger first drafts in the class. You clearly understand the move structure (Introduction Moves 1–3 and Literature Review Moves 1–4 are all present and identifiable), your research gap is genuine and well-articulated, and your writing demonstrates analytical thinking rather than mere description. The Literature Review shows genuine comparative analysis between Parrot and SGLang, which is exactly what we want to see. The main areas for improvement are: (1) adding citations throughout — the draft currently reads as all your own claims with no evidence, (2) expanding the Literature Review beyond two papers to demonstrate broader coverage, and (3) tightening the language to reduce some residual AI-polished phrasing.

**Estimated current level:** Good (7–8 range) — The structure and analytical quality are strong, but the draft needs citations, broader source coverage, and some language refinement to reach Excellent.

---

## Part 1: Introduction Feedback

### What Works Well

- **Move structure is clear and complete.** All three moves are present and distinguishable — this is a significant strength compared to many drafts that blur or skip moves
- **Move 1 (Establishing Territory)** effectively frames LLM systems as "programs executed over shared model infrastructure, rather than isolated API calls" — a crisp framing that positions your contribution
- **Move 2 (Identifying the Niche)** is well-constructed: you identify a genuine gap between system-level optimization work and application-level programming abstractions
- **Move 3 (Occupying the Niche)** states your research purpose clearly and names specific systems (Parrot, SGLang) you will examine
- Your self-identified "gap-first strategy" during revision is an excellent approach and it shows in this draft

### Issue 1: No Citations in the Entire Introduction

This is the most critical problem. Your Introduction contains four paragraphs of claims about LLM systems, optimization challenges, and research gaps — all without a single citation. Every factual claim needs evidence.

**Your sentence (no citation):** "Prior work has already shown that LLM applications often require chained or parallel invocations, prompt templates with repeated prefixes, and dynamic control flow under different task types."

Which prior work? This is a strong, specific claim that readers will want to verify. You need to cite the specific papers that demonstrate this.

**Your sentence (no citation):** "Studies in this area suggest that naive request by request serving causes unnecessary overhead and poor end to end performance."

Which studies? This sounds authoritative but without citations it is an unsupported assertion.

**Action:** Go through each paragraph and tag every claim with its source. As a rough guide:
- Paragraph 1 (Move 1): needs 3–5 citations establishing the territory of LLM infrastructure
- Paragraph 2 (Move 1 continued): needs 4–6 citations for the optimization opportunities and workload characteristics
- Paragraph 3 (Move 2): needs 3–4 citations for the specific system papers and application papers you contrast
- Paragraph 4 (Move 3): citation to Parrot and SGLang papers is essential here

### Issue 2: Move 1 Could Be More Specific

Your first paragraph effectively establishes the general territory, but it stays at a high level. You write "Recent products such as AI assistants, retrieval augmented chat tools, and multi agent copilots" without naming any specific systems or citing examples.

**Suggestion:** Ground at least one claim with a concrete example. For instance: "Systems such as ChatGPT (OpenAI, 2023), Microsoft Copilot (Microsoft, 2024), and multi-agent frameworks like AutoGen (Wu et al., 2023) rely on complex generation pipelines..." This makes Move 1 evidence-based rather than assertion-based.

### Issue 3: Move 3 Should Preview Contributions More Explicitly

Your Move 3 states the goal ("clarify what design choices are most effective for balancing programmability and performance") but does not preview specific contributions or findings. Strong Move 3 paragraphs typically enumerate numbered contributions.

**Suggestion:** Add a brief preview such as: "Specifically, this review makes three contributions: (1) a comparative analysis of service-level vs. language-level abstraction approaches, (2) identification of three underexplored gaps in current evaluation practices, and (3) a set of design principles for balancing programmability with runtime performance."

---

## Part 2: Literature Review Feedback

### What Works Well

- **Move 1 (Thematic Overview)** clearly identifies three themes (workflow-aware serving, structured programming, runtime acceleration) — this gives readers a useful organizational framework
- **Move 2 (Critical Analysis)** is the strongest part of the draft. You go beyond description to compare Parrot and SGLang on their assumptions, mechanisms, and limitations. The "cross-paper synthesis" paragraph at the end of Move 2 is excellent — it identifies a shared insight across both papers
- **Move 3 (Research Gaps)** identifies three specific, well-defined gaps (abstraction interoperability, developer effort evaluation, production workload evidence) — these are concrete and actionable
- **Move 4 (Conclusion)** effectively sets the stage for your research by specifying next steps

### Issue 4: Only Two Papers Reviewed

This is your most significant Literature Review weakness. The entire critical analysis section covers only Parrot and SGLang. For a Literature Review in a PhD-level assignment, you need to demonstrate broader engagement with the field.

**Action:** Expand to at least 6–8 papers. Based on your three themes, consider adding:
- **Workflow-aware serving:** vLLM (Kwon et al., 2023), Orca (Yu et al., 2022), or other serving systems that handle scheduling and batching
- **Structured programming:** DSPy (Khattab et al., 2023) or LMQL (Beurer-Kellner et al., 2023) as language-level approaches
- **Runtime acceleration:** Papers on KV cache management, speculative decoding, or continuous batching
- **Orchestration frameworks:** LangChain, LlamaIndex, or similar developer-facing tools that address the "programmer burden" you identify in the Introduction

You mention in your notes that you plan to expand sources — this is exactly the right instinct. Aim for a review that covers the breadth of your three themes, not just depth on two papers.

### Issue 5: Strengthen Synthesis Across More Sources

Your cross-paper synthesis paragraph comparing Parrot and SGLang is strong. When you add more papers, apply the same comparative lens. Specifically:

- Don't just describe each new paper independently. Instead, compare papers within each theme: "Unlike Parrot, which exposes request dependencies to the service layer, vLLM focuses on memory management through paged attention [citation]. Both approaches improve throughput, but they target different bottlenecks: Parrot addresses redundant computation from semantic overlap, while vLLM addresses memory fragmentation..."
- Look for tensions and tradeoffs across papers. Your self-feedback notes that you "tend to describe systems separately and need stronger synthesis across sources" — you've already solved this for Parrot vs. SGLang. Apply the same approach to the additional papers.

### Issue 6: Move 3 Gaps Need Citation Support

Your three gaps are well-identified but stated without evidence. For example:

**Your sentence:** "there is limited guidance on abstraction interoperability: it is unclear how service side abstractions and language side abstractions should be aligned"

Have any papers explicitly noted this problem? Or is it an absence you noticed while reading? Either way, you should cite the papers that come closest to this boundary and explain why they fall short.

**Action:** For each gap, cite at least one paper that partially addresses it and explain what remains unresolved.

---

## Part 3: Language and Style Feedback

### Issue 7: Some AI-Polished Phrasing

Your writing is generally clear and well-structured, but some phrases have the smoothness of AI-polished prose. Examples:

- "rapidly becoming a core infrastructure for intelligent applications" — vague; which applications? whose infrastructure?
- "This shift has made system level concerns central to research" — who made it central? cite specific papers or communities
- "create substantial optimization opportunities" — quantify if possible; "substantial" is subjective without evidence

Your reflection wisely notes: "AI is helpful for speed, structure, and language polishing. It is less reliable for nuanced claim strength and citation level precision." This is exactly right — and these examples illustrate the limitation. The language is fluent but lacks the specificity that comes from a human researcher who knows exactly which paper supports each claim.

**How to fix:** For each sentence that makes a general claim, ask yourself: "Can I name a specific paper, system, or result that supports this?" If yes, cite it and make the claim more specific. If no, consider whether the claim is necessary.

### Issue 8: Hyphenation and Formatting

Several compound modifiers need hyphens for clarity:
- "request by request serving" → "request-by-request serving"
- "end to end performance" → "end-to-end performance"
- "workflow aware serving" → "workflow-aware serving"
- "multi step reasoning" → "multi-step reasoning"
- "real world deployments" → "real-world deployments"

These are small but they affect readability and professional presentation.

---

## Part 4: Addressing Your Self-Identified Goals

Your reflection identifies four goals. Here is how your draft performs on each:

1. **"Writing sharper niche statements in Introduction Move 2"** — ✓ Your Move 2 is already one of the stronger parts. To sharpen further, add citations that demonstrate the gap concretely (e.g., "Paper X optimizes serving but ignores programming abstractions; Paper Y provides abstractions but lacks runtime integration").

2. **"Building synthesis paragraphs that compare multiple papers directly"** — ✓ Your Parrot vs. SGLang synthesis is good. Now replicate this for additional papers. Your instinct here is correct.

3. **"Improving citation-grounded critical evaluation"** — ✗ This is your biggest gap right now. Every critique needs evidence. When you say a system "may require users to adopt a new programming interface and mental model," cite evidence of this migration cost (user studies, anecdotal reports, or at minimum explain the technical basis).

4. **"Editing for concise and precise academic language"** — Partially achieved. The writing is generally concise but some phrases remain vague (see Issue 7). One more editing pass with a focus on specificity will help.

---

## Summary of Priority Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 High | Add citations throughout the Introduction and Literature Review | Transforms unsupported claims into evidence-based argument |
| 🔴 High | Expand Literature Review to 6–8 papers across all three themes | Demonstrates breadth of engagement with the field |
| 🟡 Medium | Add comparative synthesis for new papers (as you did for Parrot vs. SGLang) | Deepens critical analysis |
| 🟡 Medium | Support Move 3 gaps with specific citations | Strengthens the research gap argument |
| 🟡 Medium | Preview specific contributions in Move 3 | Signals clear research value |
| 🟢 Lower | Fix hyphenation and formatting | Improves professional presentation |
| 🟢 Lower | One more editing pass to replace vague phrases with specific claims | Reduces AI-polished tone |

---

## Next Steps

1. Read the [full writing instructions](https://github.com/tesolchina/mccpSpring2026/blob/main/writing/assessment/writing_instructions_formatted.md) carefully
2. Add citations to every paragraph — this is your top priority
3. Expand the Literature Review with 4–6 additional papers
4. Apply the same comparative synthesis you used for Parrot vs. SGLang to the new papers
5. Submit your revised draft by **15 March 2026** via both Moodle forum and Turnitin
6. Please add **tesolchina** as a collaborator on your GitHub repository so I can provide future feedback directly
