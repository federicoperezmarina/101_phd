# 📄 Automatic Chain of Thought Prompting in Large Language Models
Source: [PDF](https://arxiv.org/pdf/2210.03493)

## 🧠 Abstract

Large language models (LLMs) can perform complex reasoning by generating intermediate reasoning steps. Providing these steps for prompting demonstrations is called *chain-of-thought (CoT)* prompting. CoT prompting has two major paradigms:

- **Zero-Shot-CoT**: Uses a simple prompt like “Let’s think step by step”.
- **Manual-CoT**: Uses hand-crafted task-specific demonstrations.

This paper proposes **Auto-CoT**, a method to automatically construct demonstrations using diverse question sampling and LLM-generated reasoning chains. Auto-CoT consistently matches or outperforms Manual-CoT across 10 public reasoning benchmarks with GPT-3.

---

## 📚 Introduction

CoT prompting helps LLMs decompose problems into intermediate steps. However:

- Manual-CoT is more accurate but labor-intensive.
- Zero-Shot-CoT is flexible but prone to errors.
- **Auto-CoT** combines the best of both:
  - Automatically selects diverse questions using clustering.
  - Generates reasoning chains via Zero-Shot-CoT.
  - Uses heuristics to filter low-quality examples.

---

## 🧩 Paper Structure

### 1. Introduction  
### 2. Related Work  
- 2.1 Chain-of-thought Prompting  
- 2.2 In-Context Learning  

### 3. Challenge of Auto-CoT  
- 3.1 Retrieval-Q-CoT Fails due to Misleading by Similarity  
- 3.2 Errors Frequently Fall into the Same Cluster  
- 3.3 Diversity May Mitigate Misleading by Similarity  

### 4. Auto-CoT: Automatic Chain-of-Thought Prompting  
- 4.1 Question Clustering  
- 4.2 Demonstration Sampling  

### 5. Experiments  
- 5.1 Experimental Setup  
- 5.2 Competitive Performance of Auto-CoT  
- 5.3 Visualization of Question Clustering  
- 5.4 General Effectiveness Using the Codex LLM  
- 5.5 Effect of Wrong Demonstrations  
- 5.6 More Challenging Streaming Setting  

### 6. Conclusion  
### References  
### Appendix A & B  

---

## 🔣 Algorithms

### Heuristics for Valid Demonstrations:
- Max question length: **≤ 60 tokens**
- Max rationale steps: **≤ 5**

### Algorithm 1: Question Clustering
- Use Sentence-BERT embeddings.
- Apply k-means clustering.
- Sort cluster members by distance to cluster center.

### Algorithm 2: Demonstration Construction
- For each cluster:
  - Select closest valid question.
  - Generate rationale with Zero-Shot-CoT.
  - Validate using heuristics.

---

## ✅ Results Summary

| Model         | MultiArith | GSM8K | AddSub | AQuA | CSQA | SVAMP | StrategyQA | Coin |
|---------------|------------|-------|--------|------|------|--------|-------------|------|
| Zero-Shot     | 22.7       | 12.5  | 77.0   | 22.4 | 72.6 | 58.8   | 54.3        | 53.8 |
| Zero-Shot-CoT | 78.7       | 40.7  | 74.7   | 33.5 | 64.6 | 63.7   | 54.8        | 91.4 |
| Manual-CoT    | 91.7       | 46.9  | 81.3   | 35.8 | 73.5 | 68.9   | 65.4        | 97.2 |
| **Auto-CoT**  | **92.0**   | **47.9**|**84.8**|**36.5**|**74.4**|**69.5**|**65.4**|**99.9**|

---

## 🧾 Conclusion

Auto-CoT removes the need for manual chain-of-thought demonstrations by:
- Sampling diverse questions via clustering.
- Generating rationales automatically using a “Let’s think step by step” prompt.
- Filtering for simplicity and clarity with heuristics.

**Key takeaway:**  
> *LLMs can perform high-quality CoT reasoning without human-crafted examples.*

---

## 📚 References (Selected & Canonical)

- [✔] Brown et al., 2020 – *GPT-3: Language Models are Few-Shot Learners*  
- [✔] Wei et al., 2022 – *Chain-of-Thought Prompting*  
- [✔] Kojima et al., 2022 – *Zero-Shot Reasoning with LLMs*  
- [✔] Zelikman et al., 2022 – *STAR: Self-training with Reasoning*  
- [✔] Zhou et al., 2022 – *Least-to-Most Prompting*  
- [✔] Wang et al., 2022 – *Self-Consistency Decoding*  
- [✔] Reimers & Gurevych, 201
