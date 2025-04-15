# Self-Consistency Improves Chain of Thought Reasoning in Language Models
Source: [PDF](https://arxiv.org/pdf/2203.11171)

## 📄 Title
**SELF-CONSISTENCY IMPROVES CHAIN OF THOUGHT REASONING IN LANGUAGE MODELS**

## 🧠 Abstract
Chain-of-thought prompting combined with pre-trained large language models has achieved encouraging results on complex reasoning tasks. In this paper, we propose a new decoding strategy, **self-consistency**, to replace the naive greedy decoding used in chain-of-thought prompting. It first samples a diverse set of reasoning paths and then selects the most consistent answer by marginalizing out the sampled paths. Our evaluation shows that self-consistency significantly improves performance on benchmarks like GSM8K (+17.9%), SVAMP (+11.0%), AQuA (+12.2%), StrategyQA (+6.4%) and ARC-challenge (+3.9%).

## 🚀 Introduction
Language models have excelled in many NLP tasks but still struggle with reasoning. Chain-of-thought (CoT) prompting helps by guiding models through intermediate steps. This paper introduces **self-consistency**, which samples multiple reasoning paths and selects the answer with the highest agreement—akin to human reasoning. Unlike other methods, it’s unsupervised, requires no fine-tuning, and works out-of-the-box with pre-trained models.

---

## 🧩 Section Outline

- **1. INTRODUCTION**
- **2. SELF-CONSISTENCY OVER DIVERSE REASONING PATHS**
- **3. EXPERIMENTS**
  - 3.1 EXPERIMENT SETUP
  - 3.2 MAIN RESULTS
  - 3.3 WHEN CHAIN-OF-THOUGHT HURTS PERFORMANCE
  - 3.4 COMPARISON TO EXISTING APPROACHES
  - 3.5 ADDITIONAL STUDIES
- **4. RELATED WORK**
- **5. CONCLUSION AND DISCUSSION**
- **REPRODUCIBILITY STATEMENT**
- **ETHICS STATEMENT**
- **REFERENCES**

---

## 🧮 Mathematical Foundations

**Answer selection via majority vote:**
```math
\text{argmax}_a \sum_{i=1}^{m} \mathbf{1}(a_i = a)


## Conclusion
Self-consistency is a simple, effective decoding strategy that improves reasoning accuracy in large language models across various tasks. It enables models to produce more reliable answers, offers insight into their reasoning, and improves confidence calibration. While more computationally expensive, it requires no extra training and can be useful even with few sampled paths. It also shows promise for future applications in training and evaluation workflows.

One limitation of self-consistency is that it incurs more computational cost. In practice, using as few as 5–10 paths can yield most of the benefits without the full cost of 40 samples. It can also be extended to help generate better training data for supervised fine-tuning.

## References
🧠 Brown et al., 2020 – Language models are few-shot learners (GPT-3)
🧠 Wei et al., 2022 – Chain-of-Thought Prompting
🧠 Chowdhery et al., 2022 – PaLM
🧠 Cobbe et al., 2021 – Training verifiers for math problems
🧠 Kojima et al., 2022 – Zero-shot CoT
🧠 Adiwardana et al., 2020 – Towards human-like chatbots (Meena)
🧠 Holtzman et al., 2020 – The curious case of neural degeneration (nucleus sampling)
🧠 Li & Jurafsky, 2016 – Diverse decoding strategies
Fan et al., 2018 – Hierarchical story generation
Gao et al., 2021 – Better few-shot learners with prompt engineering
Elazar et al., 2021 – Improving model consistency
Nye et al., 2021 – Dual-system reasoning for coherence
Xu et al., 2021 – Commonsense QA with reasoning chains

