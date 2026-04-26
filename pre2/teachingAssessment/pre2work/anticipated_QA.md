# Anticipated Q&A — Poster (SGLang / LLM serving)

Use this list to prepare spoken answers (specialist and lay versions). Keep lay answers under ~25 seconds.

---

## Lay audience (plain language)

**Q: What problem does this poster describe?**  
A: Many AI services repeat the same long instructions for every request. That wastes time and money. SGLang reduces that waste by reusing work the system has already done.

**Q: Why should I care?**  
A: Faster responses for users and lower cost for anyone running AI at scale—apps, labs, or companies.

**Q: Is this a new AI model?**  
A: No. It is a serving system. The model stays the same; the runtime is smarter about memory and scheduling.

**Q: What is the main result in one sentence?**  
A: On published benchmarks, the system reports up to about six times higher throughput and up to about four times lower latency versus strong baselines.

**Q: How do you know each design choice matters?**  
A: The paper turns off one feature at a time. Performance drops each time, which supports a causal story, not only a final score.

---

## Specialist audience (systems / ML)

**Q: What is RadixAttention in one precise sentence?**  
A: It keeps KV-cache blocks in a radix tree so shared token prefixes can be matched, reused, and evicted with an LRU-style policy tuned for leaves.

**Q: How does this differ from vLLM-style paged attention?**  
A: Paged attention improves memory layout for one request; RadixAttention targets reuse across many calls and workloads with shared prefixes, plus cache-aware scheduling.

**Q: What baselines are used?**  
A: The paper compares against systems such as vLLM and Guidance-class stacks under controlled settings; see the evaluation section for versions.

**Q: What is the cache-aware scheduler doing?**  
A: It prioritizes requests with longer prefix matches to reduce cache thrashing and raise hit rate, especially under batching.

**Q: Limitations or failure modes?**  
A: When outputs are long and sharing is low, speedups shrink; scheduling can interact with fairness; API-only models use different optimizations (speculative execution).

**Q: What would you implement first if you reproduced this?**  
A: Prefix matching + correctness checks on reuse, then measure hit rate, latency, and throughput before adding scheduling tweaks.

---

## Bridge answers (mixed audience)

**Q: What do you mean by "KV cache"?**  
A (short): Intermediate memory from processing earlier tokens. If two requests share an early part of the prompt, recomputing that memory is redundant—reuse saves compute.

**Q: What is an ablation in this context?**  
A: The authors remove one mechanism—tree cache, scheduling, hints—and show the system slows down. That links speed to specific ideas.

---

## If you get stuck

- Restate the claim in one line, then give one figure on the poster (Fig. 5/6 for speed, Fig. 8 for ablations, Fig. 3 for intuition).
- Invite them to the reference: Zheng et al., arXiv:2312.07104.
