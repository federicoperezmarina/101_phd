## Synthetic Data Generation with Large Language Models for Text Classification: Potential and Limitations
[PDF](https://arxiv.org/pdf/2310.07849)

### Abstract
The collection and curation of high-quality training data is crucial for developing text classification models with superior performance but often comes at significant cost and time investment. Researchers have recently explored using large language models (LLMs) to generate synthetic datasets as an alternative. However, the effectiveness of LLM-generated synthetic data in supporting model training is inconsistent across different classification tasks. This study examines how model performance varies with the subjectivity of classification. Results suggest subjectivity, at both task and instance levels, negatively affects performance when models are trained on synthetic data. The study concludes with implications for leveraging LLMs for synthetic data generation.

### Introduction
Machine-learning-powered text classification models are widely used in applications like detecting biased or toxic language and filtering spam emails. Their performance heavily relies on the quality of training data, posing challenges for novel tasks or new classification categories due to the complexity and cost of data curation. Recent advancements in LLMs have prompted exploration into generating synthetic data to augment or replace real-world datasets. This study investigates whether LLM-generated synthetic data can match the performance of real-world data for training models, focusing on the impact of task subjectivity.

### Table of Contents
1. Introduction
2. Related Work
   - Generative AI in Synthetic Data Generation
   - Large Language Models
3. Methodology
   - Zero-shot Synthetic Data Generation
   - Few-shot Synthetic Data Generation
4. Evaluation I: Comparison Across Different Types of Tasks
   - Datasets and Tasks
   - Task-level Subjectivity Determination
   - Model Training
   - Evaluation Results
   - Exploratory Analysis: Data Diversity
5. Evaluation II: Comparison Across Different Task Instances
   - Instance-level Subjectivity Determination
   - Evaluation Results
6. Conclusions and Discussions
   - Why Subjectivity Adversely Impacts the Effectiveness of the Synthetic Data?
   - Explaining a Few Exceptions
   - Limitations and Future Work
7. Mathematical Content
8. References

### Mathematical Content
The formula below represents the instance-level annotation agreement as a proxy for subjectivity:

\[
a_i = \frac{\max_{y \in Y} \sum_{k=1}^{K_i} 1(r^k_i = y)}{K_i}
\]

Where:  
- \( Y \): Set of all possible labels.  
- \( K_i \): Total annotators for instance \( i \).  
- \( r^k_i \): Annotation by \( k \)-th annotator for instance \( i \).  

### Conclusions
The study highlights how subjectivity negatively impacts the utility of LLM-generated synthetic data for training text classification models. While models trained on synthetic data struggle with subjective tasks, guiding synthetic data generation with real-world examples can improve effectiveness. The findings encourage exploring strategies to increase data diversity and better reflect real-world data distributions.

### References
- Zhuoyan Li et al., **Towards Better Detection of Biased Language with Scarce, Noisy, and Biased Annotations**, Proceedings of the 2022 AAAI/ACM Conference on AI, Ethics, and Society.
- Saif Mohammad et al., **SemEval-2018 Task 1: Affect in Tweets**, Proceedings of the 12th International Workshop on Semantic Evaluation.
- Dorottya Demszky et al., **GoEmotions: A Dataset of Fine-Grained Emotions**, ACL 2020.