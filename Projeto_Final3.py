from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

# 1. Carregar os dados do Excel
CAMINHO_ENTRADA_PADRAO = Path("pedidos_1000_linguagem_simples.xlsx")
df = pd.read_excel(CAMINHO_ENTRADA_PADRAO)

# 2. Converter colunas para o formato de data
for coluna in ['Data_Pedido', 'Data_Prevista', 'Data_Entrega']:
  df[coluna] = pd.to_datetime(df[coluna])

# 3. Calcular os KPIs principais
df['On_Time'] = df['Data_Entrega'] <= df['Data_Prevista']  # No prazo
df['In_Full'] = df['Qtd_Entregue'] >= df['Qtd_Pedida']  # Quantidade completa
df['OTIF'] = df['On_Time'] & df['In_Full']  # No prazo E completo

# 4. Calcular Dias de Atraso e Lead Time
df['Dias_Atraso'] = (df['Data_Entrega'] - df['Data_Prevista']).dt.days.clip(
    lower=0
)
df['Lead_Time'] = (df['Data_Entrega'] - df['Data_Pedido']).dt.days

# 5. Resumo geral dos KPIs
kpis = pd.Series({
    'On Time (%)': df['On_Time'].mean() * 100,
    'In Full (%)': df['In_Full'].mean() * 100,
    'OTIF (%)': df['OTIF'].mean() * 100,
    'Atraso Médio (dias)': df['Dias_Atraso'].mean(),
    'Lead Time Médio (dias)': df['Lead_Time'].mean(),
    'Total de Pedidos Atrasados': (df['Dias_Atraso'] > 0).sum(),
}).round(2)

print('--- RESUMO DE KPIS ---')
print(kpis)

# 6. Agrupamento por Fornecedor
fornecedores = (
    df.groupby('Fornecedor')
    .agg(
        Pedidos=('Pedido', 'count'),
        OTIF=('OTIF', lambda x: x.mean() * 100),
        Atraso_Medio=('Dias_Atraso', 'mean'),
    )
    .reset_index()
    .sort_values('OTIF', ascending=False)
)

# 7. Agrupamento por Categoria
categorias = (
    df.groupby('Categoria')
    .agg(
        Pedidos=('Pedido', 'count'),
        OTIF=('OTIF', lambda x: x.mean() * 100),
        Atraso_Medio=('Dias_Atraso', 'mean'),
    )
    .reset_index()
)

# 8. Contagem de Justificativas dos Atrasos
justificativas = (
    df[df['Dias_Atraso'] > 0]['Justificativa']
    .value_counts()
    .reset_index(name='Ocorrencias')
)

# 9. Gerar gráfico simples de atrasos por fornecedor
top_atrasos = fornecedores.sort_values('Atraso_Medio', ascending=False).head(5)
plt.barh(top_atrasos['Fornecedor'], top_atrasos['Atraso_Medio'])
plt.title('Top 5 Fornecedores com Maior Atraso Médio')
plt.xlabel('Atraso Médio (dias)')
plt.tight_layout()
plt.show()

# 10. Salvar todos os resultados em um novo Excel
with pd.ExcelWriter('resultado_analise.xlsx') as writer:
  df.to_excel(writer, sheet_name='Base Tratada', index=False)
  fornecedores.to_excel(writer, sheet_name='Fornecedores', index=False)
  categorias.to_excel(writer, sheet_name='Categorias', index=False)
  justificativas.to_excel(writer, sheet_name='Justificativas', index=False)
  kpis.to_excel(writer, sheet_name='KPIs Gerais')

print("\nAnálise concluída! Arquivo 'resultado_analise.xlsx' criado.")