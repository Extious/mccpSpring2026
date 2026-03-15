# Efficient Execution Frameworks for Structured LLM Programs

ZHAO Zhan (趙展)

---

## Introduction

### Move 1 — Establishing a Territory

Intelligent applications have become essential infrastructures of large language model (LLM) based systems. ChatGPT and Microsoft Copilot, as well as open-source multi-agent frameworks, are starting to depend on more complex generation pipelines which involve many consecutive or parallel calls to LLMs, instead of a request-response interaction. According to Zheng et al. (2024), such applications are termed as "language model programs"—multi-step computations which organize model calls with programmatic logic. This change has brought about the central role of system-level issues in research: the practical performance is not only determined by the quality of the models but also by the throughput, latency, scheduling, and engineering support of structured workflows (Yu et al., 2022; Kwon et al., 2023). User experience is no longer limited by model capability, and instead, in a multiplicity of production environments, it is determined by the manner in which requests are arranged, processed, and synchronized across runtime units (Lin et al., 2024).

The studies of using LLM as a serving tool have indicated that such applications more often than not need prompt templates with shared prefixes, dynamic control flow across job types, and structured output formats, such as JSON or code (Zheng et al., 2024). These features generate opportunities such as the use of KV cache, request co-location, and iteration-level scheduling (Kwon et al., 2023; Yu et al., 2022). Research has also shown that naive request-by-request serving injects additional overhead and end-to-end performance degradation, especially in situations where workloads contain both long-context input, multi-step logic, and constrained decoding (Lin et al., 2024; Zheng et al., 2024). In the meantime, the current state of development practices around LLM applications continues to require developers to manually deal with orchestration logic in dealing with performance constraints (Beurer-Kellner et al., 2023; Khattab et al., 2024).

### Move 2 — Identifying a Niche

Even with this development, there has been a gap between two sets of work. System-level studies concentrate on optimizations at the backend, including memory management and batch scheduling of higher throughput and lower latency (Kwon et al., 2023; Yu et al., 2022), whereas programming-level work is concentrated on prompt engineering, agent design, and pattern control programs (Khattab et al., 2024; Beurer-Kellner et al., 2023). The relationship between these directions is not explored entirely. Specifically, the literature is silent on how programming abstractions of LLM workflows should interface with the runtime optimization machinery, to enable intent capture by developers to be converted into a fast execution without significant manual optimization.

### Move 3 — Occupying the Niche

This review explores effective execution models of structured LLM programs, in terms of how workflow-level abstractions reveal optimization opportunities during execution. In particular, the review contributes to the body of research in three ways: (1) comparative analysis of the service-level and language-level abstraction approaches, focusing on Parrot (Lin et al., 2024) and SGLang (Zheng et al., 2024); (2) synthesis of relevant serving and programming systems, which puts these approaches in perspective within the broader field; and (3) identification of three types of underexplored gaps concerning abstraction interoperability, developer-effort assessment, and production workload evidence.

---

## Literature Review

### Move 1 — Thematic Overview

The studies of effective applications of LLM can be divided into three themes. The first is *workflow-conscious serving*, where application-level request relationships are used as the optimization goals (Lin et al., 2024; Yu et al., 2022). The second is *structured language model programming*, which adds high-level primitives to describe the flows of generation and control logic (Zheng et al., 2024; Khattab et al., 2024; Beurer-Kellner et al., 2023). The third is *runtime acceleration*, such as KV cache control, scheduling policies, and decoding optimizations that minimize inference overhead (Kwon et al., 2023). This review examines representative works from each theme, with particular attention to Parrot and SGLang as systems that bridge serving infrastructure and programming abstractions.

### Move 2 — Critical Analysis

Initial research on LLM serving provided a basis for scheduling and memory management methods. Yu et al. (2022) proposed Orca, that is, in place of request-level scheduling, *iteration-level scheduling* is employed where the system can preempt requests inside a batch and eliminate the head-of-line blocking resulting from different output lengths. Orca achieved 36.9× throughput improvement over FasterTransformer on GPT-3 175B. Following this line, Kwon et al. (2023) suggested vLLM with *PagedAttention*, a memory management algorithm based on operating system virtual memory, which caches KV in non-contiguous pages, resulting in 2–4× throughput improvement compared to existing systems. Both Orca and vLLM use individual requests as the unit of optimization, and they do not use any application-level information regarding the dependencies between requests.

Parrot (Lin et al., 2024) builds on serving-level optimization by stating that request-wise design does not allow global optimization between dependent LLM calls. The article finds three specific inefficiencies in the existing services: excessive overhead in successive requests, misaligned scheduling objectives, and unnecessary re-computation from prompt commonality. Its fundamental contribution is a *semantic variable* abstraction, representing prompt regions and data dependencies, allowing coordinated scheduling and cross-request optimization with reported speedups of up to 11.7×. But the success of Parrot would hinge on the consistency with which developers annotate their processes, and the article does not discuss much about the cost of integration or its ease of use by developers compared to more language-centered solutions.

A similar body of research concerns the programming aspect of LLM applications. Beurer-Kellner et al. (2023) proposed a query language LMQL, which uses a combination of natural language prompting with scripting and output constraints, achieving 26–85% cost savings by producing efficient inference procedures that minimize expensive model calls. Khattab et al. (2024) presented DSPy, which compiles declarative pipeline specifications into an optimized chain of prompts, where developers can specify *what* a pipeline should do but not *how* to prompt each step. Pipelines compiled by DSPy were faster than hand-constructed few-shot prompting in a variety of benchmarks. Both LMQL and DSPy improve developer productivity, but do not engage with serving-level runtime mechanisms like batch scheduling or KV cache management.

The programming and serving gap is addressed by SGLang (Zheng et al., 2024), through the co-design of a frontend language with a runtime system. Its major innovations are *RadixAttention*, a radix tree that manages and shares KV cache between requests that share common prefixes, and *compressed finite state machine decoding* to generate constrained output efficiently. On the tasks of agent control, logical reasoning, JSON decoding, and retrieval-augmented generation, SGLang had a top throughput compared to state-of-the-art inference engines by up to 6.4×. In contrast to LMQL and DSPy, which focus mainly on the programming interface, SGLang combines language primitives with runtime mechanisms so that the system can use the multi-call structure of programs automatically.

An overview of these six systems shows a shared insight: effective LLM applications need to be explicitly structured, be it in the form of iteration-level batching (Yu et al., 2022), paged memory (Kwon et al., 2023), semantic variables (Lin et al., 2024), query constraints (Beurer-Kellner et al., 2023), declarative pipelines (Khattab et al., 2024), or typed program constructs (Zheng et al., 2024). All of them challenge the assumption that black-box request handling suffices for complex workloads. But they also vary in where optimization decisions are made: serving-level systems like Orca, vLLM, and Parrot make optimization transparent to developers but demand service-side complexity, while programming-level systems like LMQL, DSPy, and SGLang provide developers with more control but require adoption of new interfaces and programming paradigms.

### Move 3 — Research Gaps

This literature still has three gaps. First, the guidance regarding *abstraction interoperability* is limited: how service-side mechanisms like Parrot's semantic variables and language-side mechanisms like SGLang's RadixAttention are supposed to be combined to prevent duplicated complexity is not adequately covered. Lin et al. (2024) and Zheng et al. (2024) show significant improvements independently, yet no research has investigated whether these approaches can be integrated. Second, existing evaluations focus on aggregate performance indicators including throughput and latency, but do not offer an adequate analysis of *developer effort, maintainability, and debugging costs*. Beurer-Kellner et al. (2023) report API cost savings but not programmer productivity, and none of the reviewed systems contain any user studies. Third, the vast majority of reported results are based on controlled benchmarks; there is a paucity of evidence from *long-running production workloads* with evolving prompts and mixed quality-of-service demands.

Such gaps are important since practical adoption depends on both efficiency and usability. A system which provides high throughput gains at high integration cost may be unsuitable for small teams, while systems with high usability but lacking robust runtime optimization may not scale to production levels.

### Move 4 — Conclusion of the Literature Review

The current studies demonstrate that workflow-aware and structure-aware strategies have the potential to significantly improve LLM application performance. Orca and vLLM established foundational serving techniques; Parrot has proven the usefulness of exposing inter-request dependencies; LMQL and DSPy have shown that programming abstractions can reduce cost and developer burden; and SGLang has demonstrated that language-runtime co-design enables both expressibility and efficiency. Collectively, these works offer a foundation for studying how to build LLM execution frameworks that balance programmability, portability, and performance. My research will extend this analysis by developing a comparison framework that identifies when each design strategy is most suitable and what principles should guide the integration of service-level and language-level optimization approaches.

---

**Word count:** 1,500 (excluding title, headings, and references)

---

## References

Beurer-Kellner, L., Fischer, M., & Vechev, M. (2023). Prompting is programming: A query language for large language models. *Proceedings of the 44th ACM SIGPLAN International Conference on Programming Language Design and Implementation (PLDI '23)*. https://doi.org/10.1145/3591300

Khattab, O., Singhvi, A., Maheshwari, P., Zhang, Z., Santhanam, K., Vardhamanan, S., Haq, S., Sharma, A., Joshi, T. T., Mober, H., Shah, P., Baez, R., Schlegel, M., Wu, N., Pinhanez, C., Khare, S., Potdar, S., & Zaharia, M. (2024). DSPy: Compiling declarative language model calls into state-of-the-art pipelines. *Proceedings of the Twelfth International Conference on Learning Representations (ICLR 2024)*.

Kwon, W., Li, Z., Zhuang, S., Sheng, Y., Zheng, L., Yu, C. H., Gonzalez, J., Zhang, H., & Stoica, I. (2023). Efficient memory management for large language model serving with PagedAttention. *Proceedings of the 29th Symposium on Operating Systems Principles (SOSP '23)*, 611–626.

Lin, C., Han, Z., Zhang, C., Yang, Y., Yang, F., Chen, C., & Qiu, L. (2024). Parrot: Efficient serving of LLM-based applications with semantic variable. *Proceedings of the 18th USENIX Symposium on Operating Systems Design and Implementation (OSDI '24)*. https://www.usenix.org/conference/osdi24/presentation/lin-chaofan

Yu, G.-I., Jeong, J. S., Kim, G.-W., Kim, S., & Chun, B.-G. (2022). Orca: A distributed serving system for transformer-based generative models. *Proceedings of the 16th USENIX Symposium on Operating Systems Design and Implementation (OSDI '22)*, 521–538.

Zheng, L., Yin, L., Xie, Z., Sun, C., Huang, J., Yu, C. H., Cao, S., Kober, C., Gonzalez, J., Barrett, C., Sheng, Y., Jordan, M. I., & Stoica, I. (2024). SGLang: Efficient execution of structured language model programs. *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*.
