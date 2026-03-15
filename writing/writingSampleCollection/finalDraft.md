# Efficient Execution Frameworks for Structured LLM Programs

ZHAO Zhan (趙展)

---

## Introduction

### Move 1 — Establishing a Territory

Large language model (LLM) based systems now serve as critical infrastructure for intelligent applications. Products such as ChatGPT, Microsoft Copilot, and open-source multi-agent frameworks increasingly rely on complex generation pipelines involving multiple chained or parallel LLM calls, rather than a single request-response interaction. Zheng et al. (2024) characterize these applications as "language model programs"—multi-step computations that coordinate model calls with programmatic logic. This shift has made system-level concerns central to research: practical success depends not only on model quality but also on throughput, latency, scheduling, and engineering support for structured workflows (Yu et al., 2022; Kwon et al., 2023). In many production settings, user experience is constrained less by model capability and more by how requests are organized, executed, and coordinated across runtime components (Lin et al., 2024).

Research on LLM serving has shown that these applications frequently require prompt templates with shared prefixes, dynamic control flow across task types, and structured output formats such as JSON or code (Zheng et al., 2024). These characteristics create optimization opportunities including KV cache reuse, request co-location, and iteration-level scheduling (Kwon et al., 2023; Yu et al., 2022). Studies have demonstrated that naive request-by-request serving introduces unnecessary overhead and degrades end-to-end performance, particularly when workloads combine long-context inputs, multi-step reasoning, and constrained decoding (Lin et al., 2024; Zheng et al., 2024). Meanwhile, development practices for LLM applications still place a heavy burden on developers to manually handle orchestration logic while managing performance constraints (Beurer-Kellner et al., 2023; Khattab et al., 2024).

### Move 2 — Identifying a Niche

Despite this progress, a gap persists between two lines of work. System-level research focuses on backend optimizations such as memory management and batch scheduling for higher throughput and lower latency (Kwon et al., 2023; Yu et al., 2022), while programming-oriented work emphasizes prompt engineering, agent design, and program-like control patterns (Khattab et al., 2024; Beurer-Kellner et al., 2023). The connection between these directions is not fully explored. In particular, existing studies do not adequately explain how programming abstractions for LLM workflows should align with runtime optimization mechanisms, so that developer intent can be translated into efficient execution without extensive manual tuning.

### Move 3 — Occupying the Niche

This review investigates efficient execution frameworks for structured LLM programs, focusing on how workflow-level abstractions expose optimization opportunities at runtime. Specifically, this review makes three contributions: (1) a comparative analysis of service-level and language-level abstraction approaches, centered on Parrot (Lin et al., 2024) and SGLang (Zheng et al., 2024); (2) a synthesis of related serving and programming systems that contextualizes these approaches within the broader field; and (3) identification of underexplored gaps concerning abstraction interoperability, developer-effort evaluation, and production workload evidence.

---

## Literature Review

### Move 1 — Thematic Overview

Research on efficient LLM applications can be organized into three related themes. The first is *workflow-aware serving*, which treats application-level request relationships as optimization targets (Lin et al., 2024; Yu et al., 2022). The second is *structured language model programming*, which introduces high-level primitives to express generation flows and control logic (Zheng et al., 2024; Khattab et al., 2024; Beurer-Kellner et al., 2023). The third is *runtime acceleration*, including KV cache management, scheduling policies, and decoding optimizations that reduce inference overhead (Kwon et al., 2023). This review examines representative works from each theme, with particular attention to Parrot and SGLang as systems that bridge serving infrastructure and programming abstractions.

### Move 2 — Critical Analysis

Early work on LLM serving established foundational scheduling and memory management techniques. Yu et al. (2022) introduced Orca, which replaced request-level scheduling with *iteration-level scheduling*, allowing the system to interleave requests within a batch and avoid the head-of-line blocking caused by varying output lengths. Orca achieved 36.9× throughput improvement over FasterTransformer on GPT-3 175B. Building on this direction, Kwon et al. (2023) proposed vLLM with *PagedAttention*, a memory management technique inspired by operating system virtual memory that stores KV cache in non-contiguous pages, achieving 2–4× throughput gains over existing systems. Both Orca and vLLM treat individual requests as the unit of optimization and do not incorporate application-level information about how requests relate to each other.

Parrot (Lin et al., 2024) extends serving-level optimization by arguing that request-centric design prevents global optimization across dependent LLM calls. The paper identifies three specific inefficiencies in current services: excessive overhead from consecutive requests, misaligned scheduling objectives, and redundant computation from prompt commonality. Its core contribution is a *semantic variable* abstraction that captures prompt regions and data dependencies, enabling coordinated scheduling and cross-request optimization with reported speedups of up to 11.7×. However, Parrot's effectiveness depends on how consistently developers annotate their workflows, and the paper provides limited discussion of integration cost or developer ergonomics compared with language-centric alternatives.

A parallel line of work addresses the programming side of LLM applications. Beurer-Kellner et al. (2023) proposed LMQL, a query language that combines natural language prompting with scripting and output constraints, achieving 26–85% cost savings by generating efficient inference procedures that minimize expensive model calls. Khattab et al. (2024) introduced DSPy, which compiles declarative pipeline specifications into optimized prompt chains, allowing developers to specify *what* a pipeline should achieve rather than *how* to prompt each step. DSPy-compiled pipelines outperformed hand-crafted few-shot prompting across multiple benchmarks. Both LMQL and DSPy improve developer productivity but do not deeply integrate with serving-level runtime mechanisms such as batch scheduling or KV cache management.

SGLang (Zheng et al., 2024) bridges the gap between programming and serving by co-designing a frontend language with a runtime system. Its key innovations include *RadixAttention*, which uses a radix tree to manage and reuse KV cache across requests sharing common prefixes, and *compressed finite state machine decoding* for efficient constrained output generation. Across agent control, logical reasoning, JSON decoding, and retrieval-augmented generation tasks, SGLang achieved up to 6.4× throughput improvement over state-of-the-art inference engines. Unlike LMQL and DSPy, which primarily target the programming interface, SGLang tightly couples language primitives with runtime mechanisms, enabling the system to exploit multi-call program structure automatically.

A synthesis across these six systems reveals a shared insight: efficient LLM applications require explicit structure, whether represented as iteration-level batching (Yu et al., 2022), paged memory (Kwon et al., 2023), semantic variables (Lin et al., 2024), query constraints (Beurer-Kellner et al., 2023), declarative pipelines (Khattab et al., 2024), or typed program constructs (Zheng et al., 2024). All challenge the assumption that black-box request handling suffices for complex workloads. However, they differ in where optimization decisions are made: serving-level systems such as Orca, vLLM, and Parrot make optimization transparent to developers but require service-side complexity, while programming-level systems such as LMQL, DSPy, and SGLang give developers more control but require adoption of new interfaces and programming paradigms.

### Move 3 — Research Gaps

Three gaps remain in this literature. First, there is limited guidance on *abstraction interoperability*: it is unclear how service-side mechanisms such as Parrot's semantic variables and language-side mechanisms such as SGLang's RadixAttention should be combined to avoid duplicated complexity. Both Lin et al. (2024) and Zheng et al. (2024) demonstrate substantial gains independently, but no study has examined whether these approaches can be integrated. Second, current evaluations emphasize aggregate performance metrics such as throughput and latency, while providing insufficient analysis of *developer effort, maintainability, and debugging costs*. Beurer-Kellner et al. (2023) report API cost savings but not programmer productivity, and none of the reviewed systems include user studies. Third, most reported results rely on controlled benchmarks; evidence from *long-running production workloads* with evolving prompts and mixed quality-of-service requirements remains sparse.

These gaps matter because practical adoption depends on both efficiency and usability. A system that delivers strong throughput gains but imposes high integration cost may be unsuitable for small development teams, while highly usable interfaces without robust runtime optimization may fail at production scale.

### Move 4 — Conclusion of the Literature Review

Existing research provides strong evidence that workflow-aware and structure-aware approaches can significantly improve LLM application performance. Orca and vLLM established foundational serving techniques; Parrot demonstrated the value of exposing inter-request dependencies; LMQL and DSPy showed that programming abstractions can reduce cost and developer burden; and SGLang demonstrated how language-runtime co-design enables both expressibility and efficiency. Together, these works provide a foundation for studying how to build LLM execution frameworks that balance programmability, portability, and performance. My research will extend this analysis by developing a comparison framework that identifies when each design strategy is most suitable and what principles should guide the integration of service-level and language-level optimization approaches.

---

**Word count:** 1,362 (excluding title, headings, and references)

---

## References

Beurer-Kellner, L., Fischer, M., & Vechev, M. (2023). Prompting is programming: A query language for large language models. *Proceedings of the 44th ACM SIGPLAN International Conference on Programming Language Design and Implementation (PLDI '23)*. https://doi.org/10.1145/3591300

Khattab, O., Singhvi, A., Maheshwari, P., Zhang, Z., Santhanam, K., Vardhamanan, S., Haq, S., Sharma, A., Joshi, T. T., Mober, H., Shah, P., Baez, R., Schlegel, M., Wu, N., Pinhanez, C., Khare, S., Potdar, S., & Zaharia, M. (2024). DSPy: Compiling declarative language model calls into state-of-the-art pipelines. *Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)*.

Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C. H., Gonzalez, J., Zhang, H., & Stoica, I. (2023). Efficient memory management for large language model serving with PagedAttention. *Proceedings of the 29th Symposium on Operating Systems Principles (SOSP '23)*, 611–626.

Lin, C., Han, Z., Zhang, C., Yang, Y., Yang, F., Chen, C., & Qiu, L. (2024). Parrot: Efficient serving of LLM-based applications with semantic variable. *Proceedings of the 18th USENIX Symposium on Operating Systems Design and Implementation (OSDI '24)*. https://www.usenix.org/conference/osdi24/presentation/lin-chaofan

Yu, G.-I., Jeong, J. S., Kim, G.-W., Kim, S., & Chun, B.-G. (2022). Orca: A distributed serving system for transformer-based generative models. *Proceedings of the 16th USENIX Symposium on Operating Systems Design and Implementation (OSDI '22)*, 521–538.

Zheng, L., Yin, L., Xie, Z., Sun, C., Huang, J., Yu, C. H., Cao, S., Kober, C., Gonzalez, J., Barrett, C., Sheng, Y., Jordan, M. I., & Stoica, I. (2024). SGLang: Efficient execution of structured language model programs. *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*.
