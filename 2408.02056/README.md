# MedSyn: LLM-based Synthetic Medical Text Generation Framework

## 1. Title, Abstract, and Introduction

### Title
**MedSyn: LLM-based Synthetic Medical Text Generation Framework**

### Abstract
Generating synthetic text addresses the challenge of data availability in privacy-sensitive domains such as healthcare. This study explores the applicability of synthetic data in real-world medical settings. We introduce MedSyn, a novel medical text generation framework that integrates large language models with a Medical Knowledge Graph (MKG). We use MKG to sample prior medical information for the prompt and generate synthetic clinical notes with GPT-4 and fine-tuned LLaMA models. We assess the benefit of synthetic data through application in the ICD code prediction task. Our research indicates that synthetic data can increase the classification accuracy of vital and challenging codes by up to 17.8% compared to settings without synthetic data. Furthermore, to provide new data for further research in the healthcare domain, we present the largest open-source synthetic dataset of clinical notes for the Russian language, comprising over 41k samples covering 219 ICD-10 codes.

### Introduction
The introduction discusses the scarcity of textual medical data, especially in non-English languages, due to privacy and ethical considerations. It highlights the imbalance in medical datasets where rare diseases are underrepresented, affecting machine learning models' performance. The authors present synthetic medical text generation as a viable solution. The document describes how LLMs like GPT-4 and LLaMA can generate synthetic data but require external guidance to ensure accuracy. The MedSyn framework integrates LLMs with a Medical Knowledge Graph to address these challenges, with a focus on Russian-language datasets.

---

## 2. Section and Sub-section Headings

1. **Introduction**  
2. **Related Work**  
   - 2.1 Medical Knowledge Graphs  
   - 2.2 LLMs in Medical Domain  
3. **Method**  
   - 3.1 Medical Knowledge Graph  
   - 3.2 Instruction-Following Dataset  
   - 3.3 Fine-Tuning  
   - 3.4 Generation Task  
   - 3.5 Symptoms Sampling  
   - 3.6 Synthetic Dataset  
4. **Experiments**  
   - 4.1 Datasets and Tasks  
   - 4.2 Models  
   - 4.3 Evaluation  
   - 4.4 Results  
      - Prompt Following  
      - Generating Data Out of the Training Set  
      - Synthetic Upsampling  
      - RuMedTop3 Upsampling  
   - 4.5 Human Assessment  
5. **Discussion**  
6. **Conclusion**

---

## 3. Mathematical Content

The mathematical content includes a weighting formula for sampling ICD-10 codes:

\[
w(C) = J_3\left(N_C^{symp}\right) \cdot J_3\left(N_C^{exmp}\right)
\]

Where:  
- \( J(x) = \log(1 + x) \), applied three times.  
- \( N_C^{exmp} \): Number of examples for category \( C \).  
- \( N_C^{symp} \): Number of unique symptoms within \( C \).

This formula is used to achieve a uniform distribution of ICD codes during synthetic dataset generation.

---

## 4. Conclusions

The MedSyn framework demonstrates potential in generating high-quality synthetic clinical notes indistinguishable from real medical notes. Its use increases ICD-code classification accuracy by 17.8% in challenging classes. Synthetic data from MedSyn is particularly valuable in low-resource settings and facilitates the expansion of clinical decision-support systems. The open-source framework and dataset promise further advancements in medical natural language processing tasks.

---

## 5. References

The document includes a comprehensive list of references. Let me know if you'd like a specific subset or assistance with identifying the ones you've already read.
