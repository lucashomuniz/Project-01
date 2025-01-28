# ✅ PROJECT-03

The project proposes an **innovative approach** to **statistical analysis**, integrating **parametric** and **non-parametric tests** with automated selection based on analysis objectives. By leveraging an **interactive Dashboard**, the initiative aims to streamline the statistical process, enabling users to perform analyses efficiently and accurately. The proper use and interpretation of **statistical tests** are crucial for extracting **reliable** and **meaningful insights** from data. These tests support **statistical inferences** and informed decisions regarding **differences**, **associations**, or **correlations**. However, selecting the appropriate test can be complex, requiring deep knowledge of **data characteristics** and **test assumptions**.

To address this challenge, the project automates **statistical test selection** and execution through a user-friendly **Dashboard**. This tool simplifies the analysis process, allowing users to choose tests aligned with their objectives and visualize results clearly. The **Dashboard** combines **theoretical knowledge** with practical application, fostering accessibility for researchers, professionals, and students across various fields. This solution promotes **efficient**, **reliable**, and **evidence-based decision-making**, enhancing the accessibility and effectiveness of **data analysis** through **automation** and **interactive visualization**.

Keywords: R Language, Data Analysis, Statistics, Shiny Library, Automation, Parametric and Non-Parametric Statistical Tests, Student`s t-Test, Wilcoxon, Shapiro-Wilk, Kolmogorov-Smirnov

# ✅ PROCESS

This work explores the application and interpretation of key **statistical tests**, encompassing both **parametric** and **non-parametric** approaches. Five essential tests, pivotal in **data analysis**, will be presented. Each test will be briefly described, covering its purpose, application, and the corresponding **null hypothesis (H0)**.

> 1. One-Sample Student t-test (parametric)

The **one-sample t-test** assesses whether the mean of a sample significantly differs from a specified reference value, assuming **normal distribution** and random sampling. It computes a t-value, which represents the difference between the sample mean and the reference value in terms of standard errors, and determines significance using a **p-value**. The **null hypothesis (H0)** states that the population mean equals the reference value, while the **alternative hypothesis (H1)** indicates a significant difference. Commonly applied in quality control and research, this test is a fundamental tool for rigorous hypothesis validation.

![Screenshot 2023-06-14 at 15 14 05](https://github.com/lucashomuniz/Project-3/assets/123151332/db5700bc-9fba-497c-bcca-6c21386abb0a)

> 2. Two-Sample Student t-test (parametric)

The **two-sample t-test** compares the means of two independent samples to determine if they differ significantly. It is widely used to analyze differences between distinct groups, such as treatments or experimental conditions. The test assumes equal population variances (or adjusts for unequal variances) and **normal distribution** of data. The t-value is calculated based on the mean difference relative to sample variability, with statistical significance evaluated via a **p-value**. The **null hypothesis (H0)** posits equal population means, while the **alternative hypothesis (H1)** suggests a significant difference. This test is critical in clinical trials, social studies, and performance comparisons, providing a robust statistical foundation for decision-making.

![Screenshot 2023-06-14 at 15 14 29](https://github.com/lucashomuniz/Project-3/assets/123151332/6a7aaba1-3a3d-48cc-af3c-24be2caef4cd)

> 3. Wilcoxon Test (non-parametric)

The **Wilcoxon Test** is a non-parametric method for comparing two paired or dependent samples, ideal when **parametric test** assumptions, such as normality, are not met. Unlike parametric tests, it relies on data ranks, making it suitable for ordinal data or datasets with outliers. The test evaluates the differences between paired observations, assessing whether these differences are symmetrically distributed around zero. The **null hypothesis (H0)** assumes no systematic trend in the differences, while the **alternative hypothesis (H1)** suggests a significant difference. This test is extensively used in psychology, medicine, and social sciences, where non-normal data is common.

![Screenshot 2023-06-14 at 15 14 47](https://github.com/lucashomuniz/Project-3/assets/123151332/c7113eae-579d-4293-b9aa-59076c0c7be3)

> 4. Shapiro-Wilk Test (non-parametric)

The **Shapiro-Wilk Test** evaluates whether a sample follows a **normal distribution**. It is a key tool for assessing data normality, a crucial assumption for parametric statistical tests. The test calculates a coefficient representing the alignment between the observed data distribution and the expected normal distribution. The **null hypothesis (H0)** assumes normality, while the **alternative hypothesis (H1)** suggests non-normality. A **p-value** below a predefined threshold (e.g., 0.05) indicates that the data deviates from normality. This test is widely employed to ensure the appropriate selection of statistical methods.

![Screenshot 2023-06-14 at 15 15 14](https://github.com/lucashomuniz/Project-3/assets/123151332/8dc0a7a8-c4a0-4c63-a6af-50a9b89f2396)

> 5. Kolmogorov-Smirnov Test (non-parametric)

The **Kolmogorov-Smirnov Test** is a non-parametric test used to assess **normality** or distribution equality. It compares the empirical cumulative distribution of the data with a reference distribution (e.g., normal) or evaluates whether two sample distributions are identical. The test calculates the maximum absolute difference between the cumulative distribution functions of the compared datasets. The **null hypothesis (H0)** assumes equal distributions, while the **alternative hypothesis (H1)** indicates significant differences. This test is widely applied in model fit analysis, normality verification, and distribution comparisons, offering versatility by not relying on strict data assumptions.

![Screenshot 2023-06-14 at 15 15 37](https://github.com/lucashomuniz/Project-3/assets/123151332/f6766dc6-33e7-429e-8054-3fdb45a2a101)

# ✅ CONCLUSION

Statistical tests are essential for **data analysis** and enable **evidence-based decision-making**. By mastering their fundamentals and applications, we can extract valuable insights and draw confident conclusions. This project demonstrates these tests using data generated directly within the **Automation Dashboard**, providing a hands-on approach to their application and interpretation. Each **statistical test** relies on specific assumptions. For example, the **t-test**, a **parametric test**, assumes that the data follow a **normal distribution**. When this assumption is violated, **non-parametric tests**, such as the **Wilcoxon test**, are more suitable.

In **linear regression** analysis and **machine learning** model training, data **normality** is a key requirement. Linear regression assumes that model residuals are **normally distributed**, which can be validated using tests like the **Shapiro-Wilk test**. Ensuring **normality** is critical for obtaining accurate estimates and reliable predictions. Adhering to normality assumptions and selecting the appropriate statistical tests based on the data is crucial for achieving **robust** and **reliable results** in both **statistical analysis** and **predictive modeling**.
