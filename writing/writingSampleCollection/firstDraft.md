# My First Draft

## Source Information

**Date written:** 2026-02-26

**Context:** Draft for the course writing assignment (Introduction + Literature Review, 1000-1500 words target).

**Status:** Partial but substantial draft. This version includes a full Introduction and a structured Literature Review draft that will be expanded with more domain-specific sources.

---

## Introduction

Large language model based systems are rapidly becoming a core infrastructure for intelligent applications. Recent products such as AI assistants, retrieval augmented chat tools, and multi agent copilots rely on complex generation pipelines rather than a single language model call. This shift has made system level concerns central to research: beyond model quality, practical success now depends on throughput, latency, scheduling, and engineering support for structured workflows. In many real world deployments, user experience is constrained less by model capability itself and more by inefficiencies in how requests are organized, executed, and coordinated across runtime components.

Prior work has already shown that LLM applications often require chained or parallel invocations, prompt templates with repeated prefixes, and dynamic control flow under different task types. These characteristics create substantial optimization opportunities, including cache reuse, request colocation, and runtime level scheduling strategies. Studies in this area suggest that naive request by request serving causes unnecessary overhead and poor end to end performance, especially when workloads combine long context inputs, multi step reasoning, and structured outputs. At the same time, current development practices for LLM applications still place a heavy burden on developers to manually handle orchestration logic while also managing performance constraints.

Despite growing attention to efficient LLM serving, there remains a gap between two lines of work. On one side, system papers focus on backend optimizations for higher throughput and lower latency. On the other side, application oriented work emphasizes prompt engineering, agent behavior, and program like control patterns. The connection between these lines is not always explicit. In particular, existing studies do not fully explain how programming abstractions for LLM workflows should align with runtime optimization mechanisms so that developer intent can be translated into efficient execution without excessive manual tuning.

This study addresses that gap by investigating efficient execution frameworks for structured LLM programs, with a focus on how workflow level abstractions expose optimization opportunities at runtime. I will examine representative systems, including Parrot and SGLang, to compare their assumptions, optimization strategies, and implications for practical LLM application design. The goal is to clarify what design choices are most effective for balancing programmability and performance, and to derive actionable principles for building scalable LLM based applications.

---

## Literature Review

### Move 1: Thematic Overview

Research on efficient LLM applications can be grouped into three related themes. The first theme is workflow aware serving, which treats application level request relationships as first class optimization targets. The second theme is structured language model programming, which introduces high level primitives to express generation flows and control logic. The third theme is runtime acceleration, including cache reuse, scheduling, and decoding optimizations that reduce inference overhead under realistic workloads. Together, these themes reflect an emerging view that LLM applications should be considered programs executed over shared model infrastructure, rather than isolated API calls.

This review focuses on two representative works. Parrot presents a semantic variable abstraction to preserve application level information across multi request workflows and uses this information for data flow aware optimization. SGLang proposes a frontend language and runtime stack that supports structured generation and optimized execution, including techniques such as RadixAttention and faster constrained decoding. Both systems aim to improve end to end performance for complex LLM tasks, but they emphasize different entry points: Parrot starts from service level orchestration, while SGLang starts from language and runtime co design.

### Move 2: Critical Analysis

Parrot argues that existing public LLM services are too request centric, which prevents global optimization across dependent calls. Its core contribution is a semantic variable abstraction that captures prompt regions and data dependencies between requests. By exposing these relationships to the service layer, Parrot enables coordinated scheduling and optimization choices that reflect workflow context rather than local request statistics alone. This approach is compelling because it directly targets the mismatch between application semantics and backend visibility. Reported gains, including significant speedup and throughput improvement, indicate that preserving dependency structure can materially change system performance.

However, Parrot also raises implementation questions. The effectiveness of semantic variable analysis may depend on how consistently application developers annotate workflows and how well those annotations generalize across diverse toolchains. If integration cost is high, adoption may be limited to teams with strong systems expertise. In addition, while Parrot highlights end to end efficiency, less detail is provided on developer ergonomics for day to day programming and debugging compared with language centric frameworks.

SGLang addresses this developer side more directly. It frames LLM applications as structured programs and provides frontend primitives for generation control, combined with runtime optimizations tailored to repeated and constrained execution patterns. Its design reduces friction for expressing complex interactions such as multi turn logic, parallel branches, and format constrained output generation. Empirical results showing notable throughput improvements across multiple task types suggest that language level structure can help runtime systems apply optimizations effectively.

At the same time, SGLang may require users to adopt a new programming interface and mental model, which can introduce migration overhead for existing codebases built around generic API wrappers. Performance gains are substantial in benchmarked settings, but real world outcomes may vary with prompt diversity, workload heterogeneity, and deployment constraints. More comparative evidence is still needed on when language driven approaches outperform service level orchestration approaches, or how these two directions can be integrated.

A cross paper synthesis indicates a shared insight: efficient LLM applications require explicit structure. Whether that structure is represented as semantic variables in a service system or as typed program constructs in a language runtime, both studies challenge the assumption that black box request handling is sufficient. They also suggest that optimization should be driven by workflow semantics, not only token level or batch level statistics.

### Move 3: Research Gaps

Three gaps remain visible in this literature. First, there is limited guidance on abstraction interoperability: it is unclear how service side abstractions and language side abstractions should be aligned to avoid duplicated complexity. Second, current evaluations emphasize aggregate performance metrics, but provide less analysis of developer effort, maintainability, and debugging costs across system designs. Third, many reported results use controlled benchmarks, while evidence from long horizon production workloads with evolving prompts and mixed quality of service targets remains relatively sparse.

These gaps matter because practical adoption depends on both efficiency and usability. A framework that delivers strong throughput gains but imposes high integration cost may be unsuitable for small teams, while highly usable interfaces without robust runtime optimization may fail under scale. A clearer framework for evaluating trade offs between programmability, portability, and performance is still needed.

### Move 4: Conclusion of the Literature Review

Existing research provides strong evidence that workflow aware and structure aware approaches can significantly improve LLM application performance. Parrot demonstrates the value of exposing inter request dependencies to the service layer, while SGLang shows how language runtime co design can make structured execution both expressible and efficient. Together, these works establish a useful foundation for studying efficient LLM program execution.

For my project, the key implication is that I should analyze LLM systems through a dual lens: execution performance and abstraction design. My next step is to extend this review with additional papers on scheduling policies, cache management, and developer tools, then build a comparison framework that explains when each design strategy is most suitable. This will help position my research contribution within a clearer gap and provide stronger justification for methodological choices in the full paper.

---

## Notes

1. This draft currently cites two core papers and will be expanded to include more sources from my target venue set.
2. The Introduction and Literature Review follow the required move structure, but I still need to strengthen citations in the niche and gap sections.
3. Next revision priorities are adding contrastive evidence, tightening claim wording, and improving source synthesis density.
