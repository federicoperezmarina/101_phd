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
