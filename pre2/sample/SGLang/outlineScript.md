# Outline and script for poster presentation (2-3 minutes)

Use this file to rehearse your oral poster presentation and Q&A.

---

## Presentation outline

1. **Opening (15-20 s)**  
   Title + one-sentence takeaway.

2. **Problem and gap (25-30 s)**  
   Repeated prefix computation wastes time and memory.

3. **Method (45-55 s)**  
   Frontend DSL + RadixAttention + cache-aware scheduling.

4. **Main result (15-20 s)**  
   6.4x throughput, 3.7x latency reduction.

5. **Impact and close (10-15 s)**  
   Faster user experience and lower serving cost.

---

## Script (about 2 min 20 s)

**Opening**  
"Hello everyone. This poster presents SGLang, a system for faster execution of structured large language model programs. The key message is simple: by reusing repeated computation, we make AI services both faster and cheaper."

**Problem and gap**  
"In real applications like chat agents and multi-step reasoning, many requests share the same long prefix. Existing systems often recompute this shared part again and again. That repeated work wastes GPU memory and time, and users experience higher latency."

**Method**  
"SGLang combines a frontend and a backend design. The frontend is a lightweight language for structured generation workflows. The backend introduces RadixAttention, which stores KV-cache states in a radix tree so shared prefixes can be discovered and reused automatically. In addition, a cache-aware scheduler prioritizes requests with more reusable prefixes, which further increases efficiency."

**Main result**  
"Across multiple workloads, SGLang achieves up to 6.4 times higher throughput and up to 3.7 times lower latency compared with strong baselines."

**Impact and close**  
"In conclusion, SGLang shows that runtime-level cache reuse is a practical path to scalable LLM serving. It reduces infrastructure cost and improves response speed for users. Thank you, and I welcome your questions."

---

## Possible Q&A short answers

- **What is KV cache?**  
  It is the model memory state for processed tokens. Reusing it avoids repeated computation.

- **Why radix tree?**  
  Many requests share prefixes. A radix tree stores shared prefixes efficiently and enables fast matching.

- **What if memory is limited?**  
  The runtime uses eviction policies to retain high-value shared states.

- **How to explain to non-specialists?**  
  AI no longer rereads the same long instructions every time.

---

## Checklist before assessment day

- [ ] Replace `[University Logo]` if needed; presenter: Zhan ZHAO (no supervisor on poster).
- [ ] Figures are linked from arXiv HTML; for offline PDF export, ensure images load or save copies locally.
- [ ] Rehearse to stay within 2-3 minutes.
- [ ] Prepare 3-4 Q&A answers for specialist and non-specialist audiences.
- [ ] Upload soft copy at least 2 hours before assessment and bring printed copy.
