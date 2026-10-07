# Análise de Desempenho de Pedidos de Compras 📦📊

> **Projeto de Conclusão de Curso Python – CPDI (2026)**
>
> **Autora:** Larissa Ferreira de Oliveira
>
> **Orientador:** Prof. Pedro Henrique

---

## 📌 Visão Geral do Projeto

No setor de Compras, a falta de estruturação e centralização dos dados de pedidos dificulta o acompanhamento de prazos, a avaliação de fornecedores e a identificação de gargalos logísticos.

Este projeto desenvolve uma **solução end-to-end de análise de dados aplicada à Gestão de Compras**, utilizando **Python** e **Pandas** para a automação do tratamento de dados, aplicação de regras de negócio e cálculo dos principais indicadores de desempenho (KPIs), fornecendo uma base tratada e enriquecida para consumo visual no **Power BI**.

---

## 🚀 Fluxo da Solução (Pipeline de Dados)

```
[ Excel (Dados Brutos) ] 
       ↓
[ Python + Pandas (Limpeza, Tratamento & Regras de Negócio) ] 
       ↓
[ KPIs & Agrupamentos (OTIF, Lead Time, Atrasos) ] 
       ↓
[ Exportação Excel Tratado (resultado_analise.xlsx) ] 
       ↓
[ Power BI (Dashboard Interativo & Insights) ]
```

---

## 📊 Indicadores de Desempenho (KPIs)

| Indicador | Regra de Negócio |
| :--- | :--- |
| **On Time (%)** | $\text{Data Entrega} \le \text{Data Prevista}$ |
| **In Full (%)** | $\text{Qtd Entregue} \ge \text{Qtd Pedida}$ |
| **OTIF (%)** | Entrega no prazo **E** completa simultaneamente ($\text{On Time} \land \text{In Full}$) |
| **Dias de Atraso** | $\max(0, \text{Data Entrega} - \text{Data Prevista})$ |
| **Lead Time (dias)** | $\text{Data Entrega} - \text{Data do Pedido}$ |

---

## 📈 Resultados da Simulação

A análise processou uma base com **1.000 pedidos simulados**, obtendo os seguintes resultados consolidados:

* **On Time:** $68,20\%$
* **In Full:** $80,50\%$
* **OTIF Geral:** $54,60\%$ *(Meta de referência: $85,00\%$)*
* **Atraso Médio:** $3,32$ dias
* **Lead Time Médio:** $16,60$ dias
* **Total de Pedidos Atrasados:** $318$ pedidos

---

## 🛠️ Tecnologias e Bibliotecas Utilizadas

* **Linguagem:** Python 3.x
* **Manipulação e Análise de Dados:** `pandas`
* **Visualização Exploratória:** `matplotlib`
* **Manipulação de Planilhas:** `openpyxl` / `pathlib`
* **Visualização Executiva:** Power BI
* **Versionamento:** Git / GitHub

---

## 📁 Estrutura do Repositório

```
├── data/
│   ├── pedidos_1000_linguagem_simples.xlsx   # Base bruta de dados simulados
│   └── resultado_analise.xlsx                # Base tratada e enriquecida pós-Python
├── scripts/
│   └── analise_compras.py                    # Script principal de ETL e cálculo de KPIs
├── dashboards/
│   └── dashboard_compras.pbix                # Dashboard interativo no Power BI
├── README.md                                 # Documentação principal do projeto
└── .gitignore                                # Arquivos ignorados pelo Git
```

---

## ⚙️ Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina. Instale as bibliotecas necessárias executando:

```bash
pip install pandas matplotlib openpyxl
```

### Passo a Passo

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/analise-desempenho-compras.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd analise-desempenho-compras
   ```
3. Execute o script principal de análise:
   ```bash
   python scripts/analise_compras.py
   ```
4. O script gerará o arquivo `resultado_analise.xlsx` contendo as abas:
   * `Base Tratada`
   * `Fornecedores`
   * `Categorias`
   * `Justificativas`
   * `KPIs Gerais`

---

## 💡 Recomendações de Negócio

* **Monitoramento Prioritário:** Acompanhar de perto fornecedores com indicador OTIF crítico (abaixo do patamar de $85\%$).
* **Revisão de Prazos:** Reavaliar o lead time de categorias de materiais com recorrência sistemática de atrasos.
* **Ações em Logística:** Investigar gargalos de transporte/logística, identificados como principal causa das justificativas de atraso.

---

## 🔮 Trabalhos Futuros

- [ ] Conexão direta com banco de dados relacional (ex: PostgreSQL/SQL Server).
- [ ] Atualização automática do relatório no Power BI Service via *Gateway*.
- [ ] Análise financeira detalhada (impacto monetário de atrasos e faltas).
- [ ] Aplicação de modelos preditivos para previsão de risco de atrasos.

---

⚠️ **Aviso sobre os dados:** *Todos os dados utilizados neste projeto são fictícios e possuem finalidade exclusivamente demonstrativa e educacional.*