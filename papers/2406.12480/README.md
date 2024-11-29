# The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions
Source: [PDF](https://arxiv.org/pdf/2406.12480)

# 1. Title, Abstract, and Introduction

## Title
The Power of LLM-Generated Synthetic Data for Stance Detection in Online Political Discussions

## Abstract
Stance detection holds great potential for enhancing the quality of online political discussions, as it has shown to be useful for summarizing discussions, detecting misinformation, and evaluating opinion distributions. Usually, transformer-based models are used directly for stance detection, which require large amounts of data. However, the broad range of debate questions in online political discussion creates a variety of possible scenarios that the model is faced with and thus makes data acquisition for model training difficult. 

In this work, we show how to leverage LLM-generated synthetic data to train and improve stance detection agents for online political discussions:
1. We generate synthetic data for specific debate questions by prompting a Mistral-7B model and show that fine-tuning with the generated synthetic data can substantially improve the performance of stance detection.
2. We examine the impact of combining synthetic data with the most informative samples from an unlabeled dataset. 

First, we use the synthetic data to select the most informative samples; second, we combine both these samples and the synthetic data for fine-tuning. This approach reduces labeling effort and consistently surpasses the performance of the baseline model that is trained with fully labeled data. Overall, we show in comprehensive experiments that LLM-generated data greatly improves stance detection performance for online political discussions.

## Introduction
With the recent advent of powerful generative Large Language Models (LLMs) such as ChatGPT, Llama, and Mistral, investigating how synthetic data from LLMs can be leveraged for downstream tasks has become a very important and relevant topic of research. 

It is well known that Natural Language Processing (NLP) tasks based on single-label or multi-label classification such as stance and sentiment detection benefit immensely from large amounts of labeled data. However, in many cases, labeled data is scarce, especially in the realm of online political discussions: gathering labeled data may not be allowed for privacy reasons. Additionally, stance detection for online political discussions often links comments to specific debate questions, making data acquisition even harder due to the variety of questions.

This paper explores how LLM-generated synthetic data can address these challenges, enhancing performance and reducing the effort required for data labeling.

---

# 2. Section and Sub-section Headings**

1. Introduction
2. Background
3. Method
   - Preliminaries
   - Generating Synthetic Data for Stance Detection
   - Synthetic Data-driven Query By Committee (SQBC)
4. Experiments
   - Datasets
   - Experimental Setup
   - Experiments
   - Results
   - Interpreting the Role of the Synthetic Data
5. Discussion
   - Limitations and Future Work
   - Conclusion
6. Broader Impact
7. Visualizations
   - Visualizing the Synthetic Data
   - Visualizing the Query Strategies of the Active Learning Methods
8. Additional Experimental Details
   - Compute and Runtime
   - Translation of the X-Stance Dataset for Synthetic Data Generation
   - Overview of Used Datasets
9. Dataset
   - Chosen Questions and Their Distribution
10. Extended Results

---

# 3. Mathematical Content

- Model Representation:  
  The stance detection model is defined as:
  \[
  f: Q \times X \to Y
  \]
  where:
  - \( Q \): questions
  - \( X \): statements or comments
  - \( Y \): stances (e.g., 0 or 1 for binary classification).

- Synthetic Dataset Construction:
  \[
  D(q)_{\text{synth}} = \{(x^{(m)}_{\text{synth}}, 1)\}^{M/2}_{m=1} \cup \{(x^{(m)}_{\text{synth}}, 0)\}^M_{m=M/2+1}
  \]

- SQBC Scoring:
  \[
  s^{(i)} = \sum_{m \in \text{NN}(i)} y^{(m)}_{\text{synth}} \quad \text{and} \quad s'^{(i)} = |s^{(i)} - k/2|
  \]
  Here, \( \text{NN}(i) \) refers to the k-nearest neighbors.

- Fine-tuning Loss:  
  Cross-entropy loss between predicted labels \( \hat{y}^{(i)} = f(q, x^{(i)}) \) and actual labels \( y^{(i)} \).

---

# 4. Conclusions

In this work, we presented a method to improve stance detection in online political discussions using LLM-generated synthetic data. Key findings include:
1. Fine-tuning with synthetic data improves stance detection models significantly by aligning synthetic data with real data distributions.
2. Using synthetic data for active learning reduces labeling efforts by enabling efficient selection of the most informative samples.
3. Combining synthetic data with these informative samples outperforms models trained solely on fully labeled datasets.

---

# 5. References

- ALDayel, A., & Magdy, W. *Stance detection on social media*.
- Touvron, H., et al. *Llama: Open and efficient foundation language models*.
- Devlin, J., et al. *BERT: Pre-training of deep bidirectional transformers*.
- Vamvas, J., & Sennrich, R. *X-Stance: A multilingual multi-target dataset for stance detection*.

Let me know if you need help with a detailed list of references you've already read!
