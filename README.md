# 101_phd
This report is explaining how I'm doing my phd

## Documents
* [On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey](#on-llms-driven-synthetic-data-generation-curation-and-evaluation-a-survey)
* [DataDreamer: A Tool for Synthetic Data Generation and Reproducible LLM Workflows](#datadreamer-a-tool-for-synthetic-data-generation-and-reproducible-llm-workflows)

## On LLMs-Driven Synthetic Data Generation, Curation, and Evaluation: A Survey
Source: [PDF](https://arxiv.org/pdf/2406.15126)

The paper explains how to create synthetic data with LLM's. It also specifies three steps: Data Generation, Data Curation, Data Evaluation.

![Steps to generate synthetic data](img/2406.15126/2406.15126.f2.png)

- Data Generation:
    - Prompt Engineering
    - Multi-Step Generation
- Data Curation:
    - Sample filtering
    - Label enhancement
- Data Evaluation:
    - Direct evaluation
    - Indirect evaluation

## DataDreamer: A Tool for Synthetic Data Generation and Reproducible LLM Workflows
Source: [PDF](https://arxiv.org/pdf/2402.10379)

### 1. Title, Abstract, and Introduction

#### Title:
**DataDreamer: A Tool for Synthetic Data Generation and Reproducible LLM Workflows**

#### Abstract:
Large language models (LLMs) have become essential tools for NLP research in various tasks, including synthetic data generation, evaluation, fine-tuning, and distillation. However, challenges due to model scale, closed-source nature, and lack of standardized tooling hinder open science and reproducibility. This paper introduces **DataDreamer**, an open-source Python library enabling researchers to implement advanced LLM workflows while promoting best practices for reproducibility. The library is available at [GitHub](https://github.com/datadreamer-dev/DataDreamer).

#### Introduction:
Large language models have revolutionized NLP research through the prompt-and-predict paradigm. However, issues such as closed-source accessibility, technical complexity, and prompt sensitivity hinder reproducibility and sharing. **DataDreamer** addresses these challenges by providing a standardized interface for implementing workflows like synthetic data generation, fine-tuning, and alignment while ensuring reproducibility with caching, reproducibility fingerprints, and open science practices.

---

### 2. Section and Sub-Section Headings

#### 1. Introduction
#### 2. LLM Workflows
- **Synthetic Data Generation**
- **LLMs for Task Evaluation**
- **Fine-tuning and Alignment**
- **Self-improving LLMs**

#### 3. Demonstration and Examples
#### 4. DataDreamer
- **Installation**
- **Sessions**
- **Steps**
- **Models**
- **Trainers**
- **Caching and Sharing Workflows**
- **Resumability**
- **Sharing Open Data and Open Models**
- **Efficiency and Optimizations**
- **Configuration and Extensibility**

#### 5. Reproducibility
#### 6. Conclusion

##### Appendices:
- **Instruction-Tuning a LLM**
- **Aligning a LLM**
- **Self-Rewarding LLMs**
- **Augmenting an Existing Dataset**
- **Example Synthetic Data Card**

---

### 3. Mathematical Content

The document contains theoretical frameworks rather than explicit mathematical equations. It discusses concepts like:
- **Reproducibility Fingerprints**: Hash-based uniqueness for workflows.
- **Optimization Techniques**: Multi-GPU processing, quantization, and parameter-efficient fine-tuning.

---

### 4. Conclusions

The paper emphasizes the critical role of reproducibility in NLP research, proposing **DataDreamer** as a solution to simplify LLM workflows and enable sharing and extension. By standardizing interfaces and automating caching and logging, **DataDreamer** lowers technical barriers while promoting open science and sustainability in research.

---

### 5. References

The document includes an extensive reference list on topics like:
- **LLM Optimization**
- **Reproducibility Challenges**
- **Applications in NLP Research**

Let me know if you'd like specific references detailed or checked for familiarity.
