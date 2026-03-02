# Presentation Notes (Practice Script)

## Slide 1
Good morning everyone. Today I will present SGLang with a focus on runtime inference backend optimization.

## Slide 2
Imagine a serving backend that keeps recomputing the same prompt prefix for related requests. This leads to wasted GPU compute, memory pressure, and higher latency.

## Slide 3
The paper targets backend bottlenecks directly. Existing engines are general, but they miss KV reuse opportunities, decode structured outputs too slowly, and often schedule requests without cache awareness.

## Slide 4
SGLang has a frontend and a runtime, but my focus is the runtime. RadixAttention keeps reusable KV states in a radix tree and improves reuse across multi-call workflows.

## Slide 5
Another backend gain comes from compressed finite state machines for constrained decoding. The system can decode multiple deterministic tokens in one step instead of one token per step.

## Slide 6
The quantitative evidence is strong: up to 6.4x throughput and up to 3.7x lower latency in reported settings. Cache-aware scheduling and API speculative execution also reduce runtime overhead.

## Slide 7
This matters for production serving. Better backend inference means lower cost, better response time, and more stable scaling for high-concurrency workloads.

## Slide 8
For my own research, I learned to prioritize backend bottleneck analysis and ablation-based validation. My key takeaway is that runtime-aware design can produce large gains without changing model weights.

## Slide 9
Thank you for listening. I am happy to answer your questions.
