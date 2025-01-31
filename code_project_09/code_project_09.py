
import pandas

# Exploratory Analysis
dataset_1 = pandas.read_csv('dim_produto.csv')
dataset_2 = pandas.read_csv('dim_vendedor.csv')
dataset_3 = pandas.read_csv('fato_vendas.csv')
merged_dataset = pandas.merge(pandas.merge(dataset_3, dataset_1, on="dim_produto_id"), dataset_2, on="dim_vendedor_id")

# WHAT ARE THE CHAMPION SALES PRODUCTS?
produtos_campeoes = merged_dataset.groupby('dim_produto_id').agg({'valor_total': 'sum'})
produtos_campeoes = produtos_campeoes.sort_values(by=['valor_total'], ascending=False)
top_produtos = produtos_campeoes.head(3)
#print(top_produtos)

# WHICH PRODUCTS HAVE THE BEST AND WORST MARGIN? ((SALES-COST) / SALES)
soma_vendas_custo = merged_dataset.groupby('dim_produto_id').agg({'valor_total': 'sum', 'custo_venda': 'sum'}).reset_index()
soma_vendas_custo['margem'] = ((soma_vendas_custo['valor_total'] - soma_vendas_custo['custo_venda']) / soma_vendas_custo['valor_total']) * 100
melhor_margem = soma_vendas_custo.sort_values(by='margem', ascending=False).iloc[0]
pior_margem = soma_vendas_custo.sort_values(by='margem', ascending=True).iloc[0]
#print("Produto com a melhor margem:")
#print(melhor_margem)
#print("\nProduto com a pior margem:")
#print(pior_margem)

# WHAT IS THE DEVELOPMENT OF SALES BY VOLUME, SALE VALUE AND MARGIN%?
merged_dataset['data_venda'] = pandas.to_datetime(merged_dataset['data_venda'])
merged_dataset['ano_mes'] = merged_dataset['data_venda'].dt.to_period('M')
evolucao_vendas = merged_dataset.groupby('ano_mes').agg({'quantidade': 'sum', 'valor_total': 'sum', 'custo_venda': 'sum'}).reset_index()
evolucao_vendas['margem'] = ((evolucao_vendas['valor_total'] - evolucao_vendas['custo_venda']) / evolucao_vendas['valor_total']) * 100
#print(evolucao_vendas)

# WHAT IS THE BEST MIX OF PRODUCTS THAT OFFERS ME THE GREATEST SALE VALUE AND MARGIN%?
produtos_valor_total = merged_dataset.groupby('dim_produto_id')['valor_total'].sum().reset_index()
produtos_valor_total = produtos_valor_total.sort_values(by='valor_total', ascending=False)
produtos_valor_total['ordem_valor_total'] = range(1, len(produtos_valor_total) + 1)
produtos_margem = soma_vendas_custo[['dim_produto_id', 'margem']]
produtos_margem = produtos_margem.sort_values(by='margem', ascending=False)
produtos_margem['ordem_margem'] = range(1, len(produtos_margem) + 1)
produtos_em_comum = produtos_valor_total.merge(produtos_margem, on='dim_produto_id', how='inner')
top_20_valor = produtos_em_comum.head(20)
#print("Produtos com o melhor valor total:")
#print(top_20_valor)
#print("""""")
produtos_margem = produtos_margem.sort_values(by='margem', ascending=False)
produtos_margem_top_15 = produtos_margem.head(20)
produtos_valor_total = produtos_valor_total.sort_values(by='valor_total', ascending=False)
top_20_margem = produtos_margem_top_15.merge(produtos_valor_total, on='dim_produto_id', how='inner')
#print("Produtos com a melhor margem:")
#print(top_20_margem)
#print("""""")
produtos_top_20_valor = set(top_20_valor['dim_produto_id'])
produtos_top_20_margem = set(top_20_margem['dim_produto_id'])
produtos_comuns = produtos_top_20_valor.intersection(produtos_top_20_margem)
#print("Produtos em comum entre top_20_valor e top_20_margem:")
#print(produtos_comuns)

# WHAT IS THE PERCENTAGE OF SALE GROWTH MONTH BY MONTH AND YEAR TO DATE?
merged_dataset['data_venda'] = pandas.to_datetime(merged_dataset['data_venda'])
merged_dataset['ano'] = merged_dataset['data_venda'].dt.year
merged_dataset['mes'] = merged_dataset['data_venda'].dt.month
vendas_por_mes = merged_dataset.groupby(['ano', 'mes'])['valor_total'].sum().reset_index()
vendas_por_mes['crescimento_mensal'] = vendas_por_mes['valor_total'].pct_change() * 100
vendas_por_mes['crescimento_anual'] = vendas_por_mes.groupby('ano')['valor_total'].cumsum().pct_change() * 100
print("Porcentagem de crescimento da venda mês a mês e no acumulado do ano:")
print(vendas_por_mes)
