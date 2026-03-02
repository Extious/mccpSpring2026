# Presentation Outline: SGLang

**Paper:** Zheng, L., Yin, L., Xie, Z., Sun, C., Huang, J., Yu, C. H., Cao, S., Kozyrakis, C., Stoica, I., Gonzalez, J. E., Barrett, C., & Sheng, Y. (2024). *SGLang: Efficient Execution of Structured Language Model Programs*. arXiv:2312.07104v2.

**Presentation Duration:** 8 minutes

---

## Opening (~1 minute)
- Hook: backend inference often recomputes shared prompt work
- Audience bridge: compare it to rereading the same pages before every task
- Transition: from runtime bottlenecks to backend optimizations

## Section 1: Introduction to the Article (~1.5 minutes)
- Topic: runtime inference efficiency for structured multi-call LLM workloads
- Gap: existing engines miss KV reuse, decode slowly, and schedule without workflow awareness
- Core objective: improve latency and throughput at the backend runtime level

## Section 2: Key Findings (~2 minutes)
- Finding 1: RadixAttention enables automatic KV cache reuse
- Finding 2: compressed finite state machine speeds constrained decoding
- Finding 3: cache-aware scheduling and API speculative execution reduce runtime overhead
- Evidence: up to 6.4x throughput and up to 3.7x lower latency

## Section 3: Significance (~1.5 minutes)
- Makes high-concurrency LLM serving more practical
- Shows runtime backend design is as important as prompt or model design
- Demonstrates system-level optimization gains without changing model weights

## Section 4: Impact on My Research (~1.5 minutes)
- Research lesson: inference bottlenecks should guide architecture and experiment setup
- Writing lesson: clear bottleneck framing, ablation logic, and hardware-aware evidence
- Reflection: prioritize backend metrics and reproducible runtime evaluation

## Closing (~0.5 minutes)
- Key message: runtime-aware inference backend design unlocks major performance gains
- Thank audience and invite questions
