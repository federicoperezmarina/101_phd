# 📚 Chain-of-Thought Prompting Elicits Reasoning in Large Language Models
Source: [PDF](https://arxiv.org/pdf/2201.11903)

## 📝 Title
**Chain-of-Thought Prompting Elicits Reasoning in Large Language Models**  
*Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten Bosma, et al. (Google Research, Brain Team)*

## 📄 Abstract
> We explore how generating a chain of thought—a series of intermediate reasoning steps—significantly improves the ability of large language models to perform complex reasoning. In particular, we show how such reasoning abilities emerge naturally in sufficiently large language models via a simple method called chain-of-thought prompting, where a few chain of thought demonstrations are provided as exemplars in prompting.  
> Experiments on three large language models show that chain-of-thought prompting improves performance on a range of arithmetic, commonsense, and symbolic reasoning tasks. The empirical gains can be striking. For instance, prompting a PaLM 540B with just eight chain-of-thought exemplars achieves state-of-the-art accuracy on the GSM8K benchmark of math word problems, surpassing even finetuned GPT-3 with a verifier.

## 🔍 Introduction (Section 1)
- Language models benefit from scale, but struggle with complex reasoning.
- Prior work relied on fine-tuning with rationales or standard few-shot prompting.
- This paper introduces **Chain-of-Thought (CoT) Prompting** using exemplars with intermediate reasoning steps.
- CoT works **only at large scale** (~100B+ parameters).
- Demonstrated success across arithmetic, commonsense, and symbolic reasoning tasks.
- Highlights improved interpretability, generalization, and ease of use without retraining.

---

## 🧩 Table of Contents

### Sections
- **1. Introduction**
- **2. Chain-of-Thought Prompting**
- **3. Arithmetic Reasoning**
  - 3.1 Experimental Setup
  - 3.2 Results
  - 3.3 Ablation Study
  - 3.4 Robustness of Chain of Thought
- **4. Commonsense Reasoning**
- **5. Symbolic Reasoning**
- **6. Discussion**
- **7. Related Work**
- **8. Conclusions**
- **Acknowledgements**
- **References**
- **Checklist**

---

## 🧠 Theoretical Foundations

Although the paper does not include formal theoretical models, it explores reasoning tasks through:
- Arithmetic decomposition (e.g. `5 + 2×3 = 11`)
- Symbolic logic (e.g. coin flip state tracking, string manipulations)
- Empirical analysis on how scaling affects logical coherence in multi-step reasoning

Key insight: **Reasoning emerges at scale** rather than being explicitly programmed.

---

## ✅ Conclusions (Section 8)

> We have explored chain-of-thought prompting as a simple and broadly applicable method for enhancing reasoning in language models. Through experiments on arithmetic, symbolic, and commonsense reasoning, we find that chain-of-thought reasoning is an emergent property of model scale that allows sufficiently large language models to perform reasoning tasks that otherwise have flat scaling curves. Broadening the range of reasoning tasks that language models can perform will hopefully inspire further work on language-based approaches to reasoning.

### Key Points:
- CoT prompting dramatically improves reasoning performance.
- Works best on models with **100B+ parameters**.
- Generalizes across multiple reasoning domains.
- Requires no fine-tuning—only careful prompting.
- Encourages interpretability through step-by-step thought processes.

---

## 📚 References (Selection of Key Works)

- Brown et al. (2020) — [GPT-3](https://arxiv.org/abs/2005.14165) ✅  
- Devlin et al. (2019) — [BERT](https://arxiv.org/abs/1810.04805) ✅  
- Cobbe et al. (2021) — [GSM8K](https://arxiv.org/abs/2110.14168) ✅  
- Ling et al. (2017) — Rationales for algebraic problems ✅  
- Ouyang et al. (2022) — [InstructGPT](https://arxiv.org/abs/2203.02155) ✅  
- Nye et al. (2021) — Scratchpads for intermediate computation ✅  
- Zelikman et al. (2022) — [STaR: Bootstrapping Reasoning](https://arxiv.org/abs/2203.14465) ✅  

> Many other foundational and contemporary references are cited — mostly focused on prompting, interpretability, and reasoning in NLP.

---

## 📌 Notes

- No training or finetuning required—prompt-only approach.
- CoT can be extended to zero-shot, synthetic data, or smaller models via future research.
- A compelling case for **interpretable, language-based reasoning frameworks** in LLMs.

