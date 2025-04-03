# 📚 A Systematic Survey of Prompt Engineering in Large Language Models
Source: [PDF](https://arxiv.org/pdf/2402.07927)
> *Pranab Sahoo, Ayush Kumar Singh, Sriparna Saha, Vinija Jain, Samrat Mondal, Aman Chadha*

---

## 🧠 Abstract

Prompt engineering has emerged as an indispensable technique for extending the capabilities of large language models (LLMs) and vision-language models (VLMs) without modifying core model parameters. This survey offers a structured overview of over 29 prompting techniques across application areas—detailing methodology, datasets, models, and strengths/limitations. A taxonomy diagram and comparative table further illuminate the field's landscape and research gaps.

---

## 📌 Introduction

Prompt engineering empowers pre-trained LLMs/VLMs to adapt to a wide range of downstream tasks through tailored instructions—bypassing the need for fine-tuning. The field spans from basic zero-shot and few-shot prompting to advanced frameworks like Chain-of-Thought and Tree-of-Thoughts. This survey fills the gap by categorizing and analyzing prompting methods based on their applications, offering a roadmap for researchers and practitioners.

---

## 🗂 Section and Sub-section Overview

### 2. Prompt Engineering Techniques

- **2.1 New Tasks Without Extensive Training**
  - Zero-Shot Prompting  
  - Few-Shot Prompting

- **2.2 Reasoning and Logic**
  - Chain-of-Thought (CoT)
  - Automatic Chain-of-Thought (Auto-CoT)
  - Self-Consistency
  - Logical CoT (LogiCoT)
  - Chain-of-Symbol (CoS)
  - Tree-of-Thoughts (ToT)
  - Graph-of-Thoughts (GoT)
  - System 2 Attention (S2A)
  - Thread of Thought (ThoT)
  - Chain-of-Table Prompting

- **2.3 Reduce Hallucination**
  - Retrieval-Augmented Generation (RAG)
  - ReAct Prompting
  - Chain-of-Verification (CoVe)
  - Chain-of-Note (CoN)
  - Chain-of-Knowledge (CoK)

- **2.4 User Interaction**
  - Active Prompting

- **2.5 Fine-Tuning and Optimization**
  - Automatic Prompt Engineer (APE)

- **2.6 Knowledge-Based Reasoning and Generation**
  - Automatic Reasoning and Tool-use (ART)

- **2.7 Improving Consistency and Coherence**
  - Contrastive Chain-of-Thought (CCoT)

- **2.8 Managing Emotions and Tone**
  - Emotion Prompting

- **2.9 Code Generation and Execution**
  - Scratchpad Prompting
  - Program of Thoughts (PoT)
  - Structured CoT (SCoT)
  - Chain-of-Code (CoC)

- **2.10 Optimization and Efficiency**
  - Optimization by Prompting (OPRO)

- **2.11 Understanding User Intent**
  - Rephrase and Respond (RaR)

- **2.12 Metacognition and Self-Reflection**
  - Take a Step Back Prompting

---

## 🔬 Theoretical Foundations

While the paper is conceptual, it introduces foundational frameworks like:
- Chain-of-Thought (CoT) reasoning  
- Tree/Graph-based reasoning structures  
- Optimization through natural language (OPRO)  
- Multi-step verification and self-consistency loops  

These methods function algorithmically and heuristically rather than through formal mathematics.

---

## ✅ Conclusion

Prompt engineering is reshaping how we utilize LLMs by offering powerful, parameter-free mechanisms for adaptation. This survey:
- Categorizes 29 techniques by domain
- Highlights their strengths, limitations, and applications
- Introduces a comprehensive taxonomy and summary table

**Future directions**: Hybrid prompting, meta-learning, interpretability, and ethical concerns remain key challenges and opportunities.

---

## 📖 References (Mentally Checked ✅)

- ✅ [Radford et al., 2019] — Zero-Shot, GPT-2  
- ✅ [Brown et al., 2020] — Few-Shot, GPT-3  
- ✅ [Wei et al., 2022] — Chain-of-Thought  
- ✅ [Zhang et al., 2022] — Auto-CoT  
- ✅ [Wang et al., 2022] — Self-Consistency  
- ✅ [Yao et al., 2022–2023] — ReAct, ToT, GoT  
- ✅ [Chen et al., 2022] — PoT  
- ✅ [Li et al., 2023a–d] — Emotion, CoK, SCoT, CoC  
- ✅ [Zhou et al., 2022] — APE  
- ✅ [Paranjape et al., 2023] — ART  
- ✅ [Zheng et al., 2023] — Step Back Prompting  
- ✅ [Lewis et al., 2020] — RAG  
- ✅ [Nye et al., 2021] — Scratchpad  
- ✅ [Dhuliawala et al., 2023] — Chain-of-Verification

Additional refs include:
- [Chia et al., 2023] — CCoT  
- [Weston & Sukhbaatar, 2023] — System 2 Attention  
- [Zhou et al., 2023] — Thread of Thought  

---

> For the full PDF summary or visual taxonomies, feel free to ask!  
