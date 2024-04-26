# ✅ PROJECT-18

A Super Brinquedos, uma loja de brinquedos bem estabelecida e reconhecida, recentemente embarcou em uma jornada de modernização ao buscar nossa expertise para impulsionar sua plataforma de Business Analytics. Com a iminência do Dia das Crianças, a empresa enxergou uma oportunidade estratégica para aumentar suas vendas e, nesse contexto, o Gestor Comercial solicitou a criação de um Dashboard que permitisse avaliar o desempenho atual da loja e elaborar estratégias embasadas em dados históricos. Nossa abordagem inicial consistiu na integração dos dados provenientes do sistema ERP da Super Brinquedos. Utilizamos consultas diretas ao banco de dados e convertemos esses dados em arquivos CSV, que serviram como base para o desenvolvimento de um protótipo do painel. Esses dados abrangem informações fundamentais, incluindo detalhes sobre produtos disponíveis, dados dos vendedores e histórico das transações de vendas.

Nosso principal objetivo foi criar um dashboard interativo e informativo, alinhado com os requisitos estabelecidos no documento inicial. Utilizando nossos conhecimentos sólidos em construção de visualizações, propusemos uma variedade de gráficos e layouts que facilitassem as análises necessárias. Além disso, exploramos a possibilidade de incorporar dados externos e identificar novos insights que pudessem enriquecer ainda mais a análise. O dashboard desenvolvido, deve descobrir insights valiosos, como a correlação entre determinados produtos e períodos específicos do ano, oportunidades de cross-selling e up-selling, bem como tendências emergentes no comportamento do consumidor. Essas descobertas tem como foco, proporcionar a Super Brinquedos uma vantagem competitiva significativa, permitindo que a empresa se adaptasse de forma ágil às mudanças do mercado e às demandas dos clientes.

# ✅ PROCESS

Neste projeto, adotamos uma abordagem abrangente e multidisciplinar para solucionar os desafios propostos. Primeiramente, utilizamos a linguagem de programação Python, aproveitando a versatilidade e poder da biblioteca Pandas, para realizar a análise inicial dos dados. Com o Python, pudemos realizar operações complexas de manipulação e processamento de dados, além de combinar os conjuntos de dados originais, como os dados dos produtos (dim_produto), vendas (dim_vendas) e transações (fato_vendas), essenciais para entendermos o cenário da Super Brinquedos.

No entanto, reconhecemos a importância de uma análise mais detalhada das características das variáveis presentes nas tabelas. Para isso, recorremos ao Excel, uma ferramenta amplamente conhecida por sua capacidade de manipulação e visualização de dados. Com o Excel, pudemos explorar detalhadamente cada variável, identificando padrões, tendências e possíveis relações entre os dados, agregando ainda mais profundidade à nossa análise.

Finalmente, importamos os conjuntos de dados pré-processados das etapas anteriores para o PowerBI. Esta ferramenta de visualização de dados nos permitiu criar painéis interativos e dinâmicos, nos quais pudemos explorar os insights descobertos durante as fases anteriores do projeto. Com o auxílio das linguagens DAX e M, pudemos desenvolver cálculos personalizados e medidas específicas para atender às necessidades analíticas da Super Brinquedos, oferecendo uma visão abrangente e acionável dos dados.

Além disso, ao longo do projeto, adotamos uma abordagem iterativa e colaborativa, envolvendo a equipe da Super Brinquedos em todas as etapas do processo. Isso garantiu que as soluções propostas estivessem alinhadas com as necessidades e objetivos específicos da empresa, garantindo sua eficácia e relevância. Em resumo, o projeto envolveu uma combinação de análise de dados, manipulação de planilhas e visualização interativa, culminando em soluções personalizadas e orientadas para a ação, para ajudar a Super Brinquedos a tomar decisões informadas e impulsionar seu sucesso no mercado de brinquedos.

# ✅ CONCLUSION

QUESTION 1: 

A primeira análise visava identificar os produtos mais vendidos, utilizando as variáveis "valor_total" e "dim_produto_id". Descobrimos que os três principais produtos são os itens de número 26, 77 e 92. Vale ressaltar que, ao considerar também a variável "quantidade", percebemos que, embora o produto número 26 seja o líder em vendas em termos de valor total, sua quantidade de unidades vendidas é quase 19% menor do que a do segundo colocado, o produto 77.

Isso sugere que o produto número 26 pode ter uma margem de lucro unitária mais alta em comparação com o produto 77. De fato, a margem de lucro do produto 26 é de 50,51%, enquanto a do produto 77 é de 50,13%. Teoricamente, essa diferença pode compensar a disparidade na quantidade de unidades vendidas. Assim, mesmo que um produto não tenha uma alta quantidade de vendas, ele ainda pode ser considerado líder em vendas devido a diversos fatores, como margem de lucro mais elevada, preço unitário, demanda específica, ciclo de vida do produto e estratégias de marketing.

<img width="1135" alt="image" src="https://github.com/lucashomuniz/PROJECT-18/assets/123151332/91d03a49-cc96-42c4-a3a4-467c77e6c0f4">

QUESTION 2:

A segunda análise visava identificar os produtos com as melhores e piores margens de lucro. Utilizando uma fórmula matemática específica, calculamos essa nova variável e identificamos os três principais produtos com as melhores margens, sendo eles os itens 58, 95 e 22, e os três principais produtos com as piores margens, sendo eles os itens 87, 25 e 56.

Teoricamente, a margem de lucro de um produto é influenciada por diversos fatores, com dois deles sendo cruciais, como a fórmula exemplifica: o custo de produção e o preço de venda. Produtos com custos de produção mais baixos tendem a ter margens de lucro mais altas, já que uma proporção menor da receita é consumida pelos custos de fabricação. Além disso, o preço de venda também desempenha um papel essencial na determinação da margem de um produto. Quando um produto é vendido a um preço superior aos seus custos de produção, a margem de lucro tende a ser maior. Contudo, se o preço de venda é próximo ou inferior aos custos de produção, a margem de lucro será baixa ou até mesmo negativa. Portanto, embora seja uma explicação simples e intuitiva, é importante destacar que a interação entre o custo de produção e o preço de venda é fundamental para determinar a lucratividade de um produto.

<img width="1163" alt="image" src="https://github.com/lucashomuniz/PROJECT-18/assets/123151332/c76b42e0-7289-47b2-8229-6597dd6d829b">


QUESTION 3:

A terceira questão abordou a evolução das vendas em termos de volume, valor e margem. Ao analisarmos os dados fornecidos sobre a evolução das vendas ao longo de 2023 para o produto com a melhor margem, observamos os seguintes insights. O volume de vendas, medido pela quantidade de unidades vendidas, apresenta variações mensais, indicando flutuações na demanda pelo produto. Enquanto isso, o valor das vendas reflete essas variações, mostrando montantes diferentes a cada mês e sugerindo mudanças na receita gerada pelas vendas.

No entanto, apesar das oscilações nos volumes e valores das vendas, a margem de lucro permaneceu relativamente estável ao longo do período analisado. Isso sugere uma consistência na rentabilidade do produto, com uma margem de lucro que se manteve em torno de 50% durante todo o ano. Essa estabilidade na margem indica uma gestão eficaz dos custos e uma estratégia de precificação sólida, garantindo uma performance financeira confiável para o produto em questão.

<img width="1177" alt="image" src="https://github.com/lucashomuniz/PROJECT-18/assets/123151332/856173d6-3b09-4c8c-9750-762d0fe3c065">

QUESTION 4:

A quarta questão visava determinar o melhor mix de produtos para otimizar o valor de venda e a margem de lucro. Com base nos resultados obtidos, identificamos os produtos que oferecem o melhor equilíbrio entre valor total de vendas e margem de lucro. Esses produtos se destacam por apresentar tanto um alto valor de vendas quanto uma margem percentualmente elevada. 

Os produtos que se sobressaem nesse aspecto são aqueles que figuram em ambas as listas: os que possuem a melhor margem e também geram um alto valor total de vendas. Esses produtos representam uma combinação favorável entre rentabilidade e receita. Alguns exemplos são os produtos com os IDs 20, 70, 72, 83 e 97.

Esses itens são particularmente interessantes porque não só geram uma receita total de vendas significativa, conforme indicado pelo valor total, mas também mantêm uma margem de lucro substancial. Isso sugere que são produtos populares, com boa demanda, proporcionando à empresa retornos financeiros satisfatórios.

<img width="1175" alt="image" src="https://github.com/lucashomuniz/PROJECT-18/assets/123151332/1fb84ca9-9c54-4666-8248-cf45d3d3accc">

QUESTION 5:

A pergunta era: "Qual foi a variação percentual nas vendas mês a mês e no acumulado do ano?" Com base nos dados disponíveis, podemos examinar as flutuações nas vendas de mês a mês e ao longo de todo o ano de 2023. Em janeiro, as vendas totais atingiram aproximadamente 106.520 unidades monetárias. No mês seguinte, fevereiro, houve uma queda de cerca de 9,85% em relação a janeiro, resultando em vendas totais de aproximadamente 96.029 unidades monetárias.

Em março, observou-se um aumento significativo nas vendas, com um crescimento mensal de aproximadamente 19,40% em relação a fevereiro. No entanto, os meses seguintes apresentaram flutuações, com uma queda de cerca de -15,56% em abril e um aumento de aproximadamente 10,39% em maio em comparação com o mês anterior.

Essas oscilações continuaram nos meses subsequentes, com uma leve queda de aproximadamente -2,61% em junho e uma redução mais expressiva de cerca de -11,27% em julho em relação a junho. Finalmente, em agosto, houve uma queda acentuada de aproximadamente -42,86% em relação a julho.

Ao analisarmos o crescimento das vendas no acumulado do ano, percebemos uma tendência decrescente ao longo do período. O crescimento anual diminuiu gradualmente, passando de cerca de 90,15% em fevereiro para aproximadamente 7,36% em agosto. Isso sugere uma desaceleração no ritmo de crescimento das vendas ao longo do ano de 2023, fornecendo insights valiosos para a formulação de estratégias visando otimizar o desempenho das vendas.

<img width="1177" alt="image" src="https://github.com/lucashomuniz/PROJECT-18/assets/123151332/964eab64-22de-40ee-92e2-5d02992d9332">



