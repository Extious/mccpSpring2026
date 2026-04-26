# Recording script — Poster voiceover (2-3 minutes)

**Presenter:** Zhan ZHAO  
**Language:** English  
**Target length:** about 2:15-2:45 (stay under 3:00 for MCCP6020 Assessment 2)

**Recording tip:** Do not read word-for-word on camera; use bullets as memory cues. Glance at the poster, not the script.

---

## Cue outline (optional on note card)

1. Hook + title (15-20 s)
2. Problem (25-30 s)
3. Method - three bullets (45-50 s)
4. Results - one headline + point to Figs. 5-6 (20-25 s)
5. Ablation - one sentence + Fig. 8 (15-20 s)
6. Close + invite questions (10-15 s)

---

## Full script (spoken)

Hello everyone. My name is Zhan ZHAO. This poster is about **SGLang**, a system that makes large language model programs run faster in real applications.

Think of a busy help desk that keeps rereading the same long policy manual before every answer. That is what many AI services do today: they repeat expensive work on shared instructions. The result is higher latency, higher cost, and worse user experience.

SGLang addresses this with three coordinated ideas. First, a **frontend language** that expresses structured, multi-step AI workflows cleanly. Second, **RadixAttention**, which stores intermediate memory in a radix tree so the runtime can detect shared prefixes and reuse computation instead of recomputing it. Third, a **cache-aware scheduler** that prefers requests that can reuse more cached work, which improves throughput when many programs arrive together.

On the poster you can see the published evidence on Llama-class models: **up to about six times higher throughput** and **up to about four times lower latency** compared with strong serving baselines. The charts summarize normalized throughput and latency across representative workloads.

The paper also strengthens the scientific story with **ablation studies**. When key parts are removed—such as tree-structured reuse or cache-aware scheduling—performance drops in a predictable way. That shows the gains come from identifiable design choices, not from a single lucky benchmark.

Overall, SGLang reframes LLM serving as a **reuse and scheduling** problem. For practice, that means we can improve speed and cost **without changing the model weights**, which matters for production AI.

Thank you. I would be glad to take questions—from a systems perspective or in plain language.

---

## Timing checkpoints

- After ~0:45 you should be finishing the problem paragraph.  
- After ~1:45 you should be pointing at Figs. 5-6.  
- After ~2:30 you should be closing or already on "thank you."

