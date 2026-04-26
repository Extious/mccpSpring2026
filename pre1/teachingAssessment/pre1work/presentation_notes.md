# Presentation Notes — Storytelling in SGLang (Improved Version)

Delivery language: **English**  
Target audience: **non-specialist classmates + teacher**  
Target length: **8 minutes**  
Presenter: **Zhan ZHAO**

---

## Slide 1 — Title and hook (~30 s)

Good morning everyone. Today I will analyze the SGLang paper by Zheng et al. Instead of focusing only on technical details, I will focus on one practical question: **how do experienced researchers make a complex systems paper easy to follow and convincing?**

---

## Slide 2 — What is this paper about? (~45 s)

SGLang is a system that helps Large Language Models run faster in real applications. In many AI tasks, the model repeatedly reads the same long context. SGLang avoids this repeated work by reusing previously computed memory.

For non-specialists, you can imagine this: instead of rereading chapter one every time you start chapter two, the system keeps a smart bookmark.

---

## Slide 3 — Key findings and significance (~45 s)

The paper reports two headline results:
- up to **6.4x higher throughput**
- up to **3.7x lower latency**

Why does this matter? It means lower compute cost for developers and faster responses for users. So this is not only a technical improvement; it also has clear economic and user-experience value.

---

## Slide 4 — Writing strategy 1: Start from pain (~60 s)

The first strategy is to define the bottleneck in a way that readers can immediately feel.

**Evidence from paper:** The authors show shared prefixes across tasks and explain why repeated computation is wasteful.

**Why this works:** Before introducing algorithms, they make the problem concrete and relatable.

---

## Slide 5 — Writing strategy 2: Layered structure (~60 s)

The second strategy is structural clarity. The paper separates the system into two layers: a frontend language and a backend runtime.

**Evidence from paper:** The authors explicitly state this architecture and keep each section focused.

**Why this works:** Readers first understand what users need, then how the backend solves it.

---

## Slide 6 — Writing strategy 3: Build trust with ablations (~60 s)

The third strategy is rigorous evidence. The authors do ablation studies: they remove one component at a time and measure performance changes.

**Evidence from paper:** Turning off major components causes measurable degradation.

**Why this works:** The argument changes from “we are fast” to “we are fast for identifiable reasons.”

---

## Slide 7 — Reflection, takeaways, and conclusion (~2 min 40 s total on one slide)

**Block A — Impact on my own research design (~55 s)**  
This paper changes how I plan my own experiments. Previously, I focused mostly on final comparisons. After reading this paper, I see that I also need component-level evidence.

My updated plan:
1. define one clear bottleneck early,
2. design modular methods,
3. include ablation studies as core evidence.

**Block B — Writing skills I will reuse (~55 s)**  
Three skills I will apply in my own writing:
1. **Problem-first storytelling** with concrete pain points.
2. **Strong signposting** with clear section boundaries.
3. **Evidence chains** using ablations, not only final metrics.

**Block C — Summary (~50 s)**  
In short, SGLang is both a strong systems contribution and a strong writing example. The paper persuades readers by combining a relatable problem, clear structure, and rigorous proof.

This is the key lesson I will transfer to my own research communication.

---

## Slide 8 — Q&A (~20 s)

Thank you for listening. I welcome questions on either:
- the SGLang system itself, or
- the writing strategies used in the paper.

---

## Timing cheat sheet

| Slide | Time |
|---|---|
| 1 | 0:00-0:30 |
| 2 | 0:30-1:15 |
| 3 | 1:15-2:00 |
| 4 | 2:00-3:00 |
| 5 | 3:00-4:00 |
| 6 | 4:00-5:00 |
| 7 | 5:00-7:40 (reflection + takeaways + conclusion) |
| 8 | 7:40-8:00 |

---

## Video submission checklist (Assessment 1)

Course baseline (see `pre1/materials/pre1AssessmentRubrics.md`): **8 minutes**, non-specialist audience, **visual aids required**, article intro + findings + significance + reflection with evidence from the paper.

**Before you record**

- [ ] Rehearse with the on-screen **timer** in `slides4pre1.html` (8:00 countdown; optional overtime indicator).
- [ ] Confirm all **figures load** (network access to arXiv HTML images, or download PNGs locally and update `src` if you record offline).
- [ ] Use **fullscreen** (e.g. F11) so only slides + timer appear, unless your teacher wants face-in-corner.
- [ ] **Do not read** the script word-for-word; rubric penalizes reading aloud from scripts.

**Deliverables you still create locally**

- [ ] Export or capture **video file** per Moodle instructions (filename and format as specified by lecturer).
- [ ] Keep `presentation_notes.md` as speaker support, not as on-screen text during recording.

**Content coverage (tick when your take covers it)**

- [ ] Brief introduction to the article  
- [ ] Key findings  
- [ ] Significance  
- [ ] Impact on your research design + writing skills learned, with **evidence tied to the paper** (figures / ablation / structure)
