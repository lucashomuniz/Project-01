# ✅ PROJECT-03

The project proposes an **innovative approach** to **statistical analysis**, integrating **parametric** and **non-parametric tests** with automated selection based on analysis objectives. By leveraging an **interactive Dashboard**, the initiative aims to streamline the statistical process, enabling users to perform analyses efficiently and accurately. The proper use and interpretation of **statistical tests** are crucial for extracting **reliable** and **meaningful insights** from data. These tests support **statistical inferences** and informed decisions regarding **differences**, **associations**, or **correlations**. However, selecting the appropriate test can be complex, requiring deep knowledge of **data characteristics** and **test assumptions**.

To address this challenge, the project automates **statistical test selection** and execution through a user-friendly **Dashboard**. This tool simplifies the analysis process, allowing users to choose tests aligned with their objectives and visualize results clearly. The **Dashboard** combines **theoretical knowledge** with practical application, fostering accessibility for researchers, professionals, and students across various fields. This solution promotes **efficient**, **reliable**, and **evidence-based decision-making**, enhancing the accessibility and effectiveness of **data analysis** through **automation** and **interactive visualization**.

Keywords: R Language, Data Analysis, Statistics, Shiny Library, Automation, Parametric and Non-Parametric Statistical Tests, Student`s t-Test, Wilcoxon, Shapiro-Wilk, Kolmogorov-Smirnov

# ✅ PROCESS

This work explores the application and interpretation of key **statistical tests**, encompassing both **parametric** and **non-parametric** approaches. Five essential tests, pivotal in **data analysis**, will be presented. Each test will be briefly described, covering its purpose, application, and the corresponding **null hypothesis (H0)**.

**1. One-Sample Student t-test (parametric)**
The one-sample t-test checks if a sample mean is significantly different from a reference value, assuming normal data distribution and random sampling. It computes a t-value measuring how many standard errors lie between the sample mean and the reference value, and uses a p-value to determine statistical significance. The null hypothesis (H0) holds that the population mean equals the reference value, while the alternative hypothesis (H1) indicates a significant difference. Commonly employed in areas like quality control and surveys, it is a key statistical method for validating hypotheses with rigor.

![Screenshot 2023-06-14 at 15 14 05](https://github.com/lucashomuniz/Project-3/assets/123151332/db5700bc-9fba-497c-bcca-6c21386abb0a)

**2. Two-Sample Student t-test (parametric)**
The two-sample t-test compares the means of two independent samples to determine if they significantly differ. Commonly used to analyze differences between distinct groups (e.g., treatments, conditions), it assumes equal variances (or adjusts for unequal variances) and normality. A t-value quantifies the difference relative to sample variability, with significance assessed via a p-value. The null hypothesis (H0) posits equal population means, while the alternative hypothesis (H1) suggests a meaningful difference. Essential in clinical trials, social studies, and performance comparisons, it provides a robust statistical foundation for decision-making.

![Screenshot 2023-06-14 at 15 14 29](https://github.com/lucashomuniz/Project-3/assets/123151332/6a7aaba1-3a3d-48cc-af3c-24be2caef4cd)

**3. Wilcoxon Test (non-parametric)**
The Wilcoxon Test evaluates paired or dependent samples when assumptions of parametric tests, such as normality, are not met. It ranks data rather than using raw values, making it suitable for ordinal data or datasets with outliers. The test examines the symmetry of paired differences around zero. The null hypothesis (H0) asserts no systematic difference, while the alternative hypothesis (H1) suggests a significant difference. Widely used in psychology, medicine, and social sciences, it is ideal for datasets violating parametric assumptions.

![Screenshot 2023-06-14 at 15 14 47](https://github.com/lucashomuniz/Project-3/assets/123151332/c7113eae-579d-4293-b9aa-59076c0c7be3)

**4. Shapiro-Wilk Test (non-parametric)**
O **Shapiro-Wilk Test** é um teste não paramétrico que verifica se uma amostra segue uma distribuição normal. É amplamente utilizado para avaliar a **normalidade** dos dados, uma suposição fundamental para a aplicação de testes estatísticos paramétricos. O teste calcula um coeficiente que mede a concordância entre a distribuição dos dados observados e a distribuição normal esperada. A **hipótese nula (H0)** postula que a amostra segue uma distribuição normal, enquanto a hipótese alternativa (H1) indica uma violação dessa normalidade. Um **p-valor** abaixo de um nível de significância pré-definido (como 0,05) sugere que os dados não são normalmente distribuídos. Este teste é essencial em diversas áreas, garantindo que as análises subsequentes utilizem o método estatístico mais adequado.

![Screenshot 2023-06-14 at 15 15 14](https://github.com/lucashomuniz/Project-3/assets/123151332/8dc0a7a8-c4a0-4c63-a6af-50a9b89f2396)

**5. Kolmogorov-Smirnov Test (non-parametric)**
O **Kolmogorov-Smirnov Test** é um teste não paramétrico utilizado para verificar a **normalidade** ou a igualdade de distribuições. Ele compara a distribuição empírica dos dados com uma distribuição de referência, como a normal, ou avalia se duas distribuições amostrais são iguais. O teste baseia-se na maior diferença absoluta entre as funções de distribuição cumulativa das amostras ou entre a amostra e a distribuição de referência. A **hipótese nula (H0)** assume que as distribuições comparadas são iguais, enquanto a hipótese alternativa (H1) indica diferenças significativas entre elas. Este teste é amplamente aplicado em análises de ajuste de modelos, verificação de suposições de normalidade e comparação de distribuições em estudos estatísticos. Ele é particularmente útil por não depender de suposições fortes sobre a natureza dos dados, tornando-se uma ferramenta versátil em diversas áreas de pesquisa.

![Screenshot 2023-06-14 at 15 15 37](https://github.com/lucashomuniz/Project-3/assets/123151332/f6766dc6-33e7-429e-8054-3fdb45a2a101)

# ✅ CONCLUSION

These tests play a crucial role in statistical analysis and help us make evidence-based decisions. By understanding its fundamentals and application, we can gain valuable insights into the data and draw confident conclusions. In this work, all these tests will be carried out with data generated in the Automation Dashboard itself, allowing a practical understanding of its use and interpretation.

In the context of statistical tests, it is essential to understand the assumptions underlying each type of test. The t-test, a parametric test, requires the assumption that the numerical values in the model follow a normal distribution. When data are not normally distributed, non-parametric tests such as the Wilcoxon test are recommended.

For linear regression analyzes and training machine learning models, data normality is crucial. Linear regression assumes that the model residuals follow a normal distribution, which can be verified by normality tests, such as the Shapiro-Wilk test. Ensuring data normality is important to obtain accurate estimates and reliable predictions.

When performing statistical analysis and predictive modeling, it is critical to consider the normality assumptions of the data and choose the appropriate type of statistical test based on these assumptions. This helps to get robust and reliable results.
