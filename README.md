# ✅ PROJECT-18

The Super Brinquedos, a well-established and recognized toy store, recently embarked on a modernization journey by seeking our expertise to boost its Business Analytics platform. With Children's Day imminent, the company saw a strategic opportunity to increase its sales. In this context, the Commercial Manager requested the creation of a Dashboard to assess the store's current performance and develop data-driven strategies based on historical data. Our initial approach involved integrating data from the Super Brinquedos' ERP system. We used direct database queries and converted this data into CSV files, which served as the basis for developing a prototype of the dashboard. These data encompass fundamental information, including details on available products, salesperson data, and sales transaction history.

Our main goal was to create an interactive and informative dashboard aligned with the requirements outlined in the initial document. Leveraging our solid expertise in visualization construction, we proposed a variety of charts and layouts to facilitate the necessary analyses. Additionally, we explored the possibility of incorporating external data and identifying new insights to further enrich the analysis. The developed dashboard aims to uncover valuable insights, such as the correlation between specific products and periods of the year, cross-selling and up-selling opportunities, as well as emerging trends in consumer behavior. These findings focus on providing Super Brinquedos with a significant competitive advantage, enabling the company to adapt agilely to market changes and customer demands.

Keywords: PowerBI, PowerQuery, DAX, Google Cloud Plataform, Business Analytics, Python Language, Data Visualization, Data Analysis.

# ✅ PROCESS

In this project, we adopted a comprehensive and multidisciplinary approach to address the proposed challenges. Firstly, we utilized the Python programming language, leveraging the versatility and power of the Pandas library to conduct the initial data analysis. With Python, we could perform complex data manipulation and processing operations, as well as combine the original datasets, such as product data (dim_produto), sales (dim_vendas), and transactions (fato_vendas), essential to understand Super Brinquedos' scenario.

However, we recognized the importance of a more detailed analysis of the characteristics of the variables present in the tables. For this purpose, we turned to Excel, a widely known tool for its data manipulation and visualization capabilities. With Excel, we could thoroughly explore each variable, identifying patterns, trends, and possible relationships between the data, adding even more depth to our analysis.

Finally, we imported the pre-processed datasets from the previous stages into PowerBI. This data visualization tool allowed us to create interactive and dynamic dashboards, where we could explore the insights discovered during the earlier project phases. With the help of DAX and M languages, we could develop customized calculations and specific measures to meet Super Brinquedos' analytical needs, providing a comprehensive and actionable view of the data.

Additionally, throughout the project, we adopted an iterative and collaborative approach, involving the Super Brinquedos team in every step of the process. This ensured that the proposed solutions were aligned with the company's specific needs and objectives, ensuring their effectiveness and relevance. In summary, the project involved a combination of data analysis, spreadsheet manipulation, and interactive visualization, culminating in customized and action-oriented solutions to help Super Brinquedos make informed decisions and drive its success in the toy market.

# ✅ CONCLUSION

QUESTION 1: 

The first analysis aimed to identify the top-selling products, using the variables "valor_total" and "dim_produto_id." We found that the three main products are items number 26, 77, and 92. It's worth noting that, when considering the "quantidade" variable as well, we noticed that although product number 26 leads in sales in terms of total value, its quantity sold is nearly 19% lower than the second-place product, item 77.

This suggests that product number 26 may have a higher unit profit margin compared to product 77. In fact, the profit margin of product 26 is 50.51%, while that of product 77 is 50.13%. Theoretically, this difference may offset the disparity in the quantity of units sold. Thus, even if a product doesn't have high sales volume, it can still be considered a sales leader due to various factors such as higher profit margin, unit price, specific demand, product lifecycle, and marketing strategies.

![Screenshot 2025-01-15 at 15 56 59](https://github.com/user-attachments/assets/bb3e52b2-0e2b-4fc3-95ab-26b0e71fccb6)

QUESTION 2:

The second analysis aimed to identify products with the best and worst profit margins. Using a specific mathematical formula, we calculated this new variable and identified the top three products with the best margins, items 58, 95, and 22, and the top three products with the worst margins, items 87, 25, and 56.

Theoretically, a product's profit margin is influenced by various factors, with two being crucial, as the formula exemplifies: production cost and selling price. Products with lower production costs tend to have higher profit margins, as a smaller proportion of revenue is consumed by manufacturing costs. Additionally, selling price also plays an essential role in determining a product's margin. When a product is sold at a price higher than its production costs, the profit margin tends to be higher. However, if the selling price is close to or lower than production costs, the profit margin will be low or even negative. Therefore, although it's a simple and intuitive explanation, it's important to highlight that the interaction between production cost and selling price is crucial in determining a product's profitability.

![Screenshot 2025-01-15 at 15 57 38](https://github.com/user-attachments/assets/2606f316-d49b-4628-a8b2-640d34caf2c7)


QUESTION 3:

The third question addressed the evolution of sales in terms of volume, value, and margin. By analyzing the provided data on the sales evolution throughout 2023 for the product with the best margin, we observed the following insights. The sales volume, measured by the quantity of units sold, exhibits monthly variations, indicating fluctuations in demand for the product. Meanwhile, the sales value reflects these variations, showing different amounts each month and suggesting changes in revenue generated by sales.

However, despite the fluctuations in sales volumes and values, the profit margin remained relatively stable throughout the analyzed period. This suggests consistency in the product's profitability, with a profit margin that remained around 50% throughout the year. This stability in the margin indicates effective cost management and a solid pricing strategy, ensuring reliable financial performance for the product in question.

![Screenshot 2025-01-15 at 15 58 02](https://github.com/user-attachments/assets/1c6100ac-c636-422f-b765-3caf2a481ac3)

QUESTION 4:

The fourth question aimed to determine the best product mix to optimize sales value and profit margin. Based on the obtained results, we identified products that offer the best balance between total sales value and profit margin. These products stand out by presenting both high sales value and a proportionally high margin.

The products that excel in this aspect are those that appear on both lists: those with the best margin and those that also generate high total sales value. These products represent a favorable combination of profitability and revenue. Some examples are products with IDs 20, 70, 72, 83, and 97.

These items are particularly interesting because they not only generate significant total sales revenue, as indicated by the total value but also maintain a substantial profit margin. This suggests that they are popular products with good demand, providing the company with satisfactory financial returns.

![Screenshot 2025-01-15 at 15 58 18](https://github.com/user-attachments/assets/af1da9d5-5257-4c56-9ac5-af8bacaf3ffb)

QUESTION 5:

The question was: "What was the percentage variation in sales month by month and in the year-to-date?" Based on the available data, we can examine the fluctuations in sales from month to month and throughout the entire year of 2023. In January, total sales reached approximately 106,520 monetary units. In the following month, February, there was a decrease of about 9.85% compared to January, resulting in total sales of approximately 96,029 monetary units.

In March, a significant increase in sales was observed, with a monthly growth of approximately 19.40% compared to February. However, the following months showed fluctuations, with a decline of about -15.56% in April and an increase of approximately 10.39% in May compared to the previous month.

These fluctuations continued in the subsequent months, with a slight decrease of approximately -2.61% in June and a more significant reduction of about -11.27% in July compared to June. Finally, in August, there was a steep decline of approximately -42.86% compared to July.

When analyzing the sales growth year-to-date, we observe a decreasing trend over the period. Annual growth gradually decreased, from about 90.15% in February to approximately 7.36% in August. This suggests a slowdown in the pace of sales growth throughout the year 2023, providing valuable insights for formulating strategies to optimize sales performance.

![Screenshot 2025-01-15 at 15 58 39](https://github.com/user-attachments/assets/b1127ec0-6f89-41ab-a692-6d82f14c48d4)

