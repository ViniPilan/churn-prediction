# Predição de saída de clientes

## Sobre o problema de negócio abordado
### Introdução
Prever a sáida de cleintes de uma empresa é algo fundamental para se alcançar melhores resultados. Ter o conhecimento de que determinado cliente pode estar prester a sair da empresa permite que a mesma busque reconquistá-lo, de modo a mantê-lo presente consumindo seus produtos e serviços.

A perda de um cliente para a concorrência pode ser um grande prejuízo individual, já que a empresa perde um comprador, mas também pode acarretar prejuízos coletivos como efeito manada de evasão (clientes saem porque outros saíram) por exemplo. Além do mais, um cliente sempre será uma forma forte de propaganda e isso deve ser sempre levado em consideração: resumidamente, cliente contente pode fazer propaganda positiva da empresa para outros e clientes descontentes podem fazer propaganda negativa.


![main](Images/main_resized.jpg)


Quanto mais se entende esse cenário, mais se compreende também a importância de prever a saída de clientes. Dessa forma, enxergar que um cliente está prestes a sair (com uma estimativa disso em termos probabilísticos também) é de grande relevância e isso pode ser feito com a Ciência de Dados. 

Para o problema em questão, iremos imaginar um cenário de uma empresa de crédito.


### Sobre valores - quantificando o problema
O saldo médio mensal de clientes que saem está estimado (com 95% de confiança) entre 7381.18 e 7803.58 dólares. Isso nos dá uma média de 7592.38 dólares mensais. 

Considerando a amostra de valores disponíveis para este estudo (e considerando o maior erro de proporção possível caso essa amostra não seja de qualidade), temos que a probabilidade de um cliente sair é de 16.29% a 24.45%.

Portanto, se formos imaginar um cenário em que a PIOR probabilidade acontecerá, ou seja, aproximadamente 25% de saída de clientes, tem-se que:
- para um total de 20.000 clientes, 5.000 abandoram a empresa
- se cada um que sai possui saldo mensal médio de 7592.38, **tem-se então 37.961.900 de dólares a menos em cada mês**.


Portanto, além de investir em novos clientes, investir em manter os que já fazem parte da empresa é de grande relevância.

### A solução proposta

O objetivo inicial desse projeto de Ciência de Dados era de construir uma solução aceitável para prever a saída de clientes antes mesmo de ela acontecer e tal objetivo foi cumprido. Através do uso da Estatística, Modelagem e do Machine Learning, foi desenvolvida uma solução e também implementada. 

#### Desempenho observado da solução para os dados utilizados

O modelo apresentou performance agradável com relação aos dados utilizados para teste do mesmo. Basicamente:

- Taxa de acerto médio do modelo: 77%:
    - A cada 100 clientes que saíram da empresa e o modelo não sabia disso, ele acertou de 74 a 77 - Portanto, taxa de falso negativo em média 24%.

    - A cada 100 clientes que não saíram da empresa e o modelo não sabia disso, ele acertou de 75 a 81 - Portanto, taxa de falso positivo em média 22%.
    Como pôde ser observado,


#### Desempenho esperado da solução no mundo real

A partir dos dados observados na testagem do modelo, algumas informações foram **estimadas** (com grau de confiança de 98%) sobre como o modelo se comportaria quando colocado para funcionar no mundo real:
- Taxa de acerto esperado para o modelo no mundo real: de 72% a 82%:
- Taxa de ocorrencia de falso negativo: 18% a 28%
- Taxa de ocorrência de falso positivo: 15% a 27%

Vale ressaltar que esses valores são esperados se o modelo for utilizado em um cenário de distribuição amostral semelhante ao que foi utilizado nesse projeto. Por essa razão, deve-se treinar um novo modelo se os dados forem extraídos de outra população. 

**FALTA FALAR DO LIFT**






## Dados usados no desenvolvimento da solução

### Coleta dos dados

Os dados para desenvolver a solução proposta foram extraídos [deste](https://www.kaggle.com/datasets/shubh0799/churn-modelling) dataset do Kaggle. As características presentes são:

1. **RowNumber:** The number of the row
2. **CustomerId:** The unique customer id
3. **Surname:** Customers Surname
4. **CreditScore:** Their credit score
5. **Geography:** Which Country they belong to
6. **Gender:** Their Gender
7. **Age:** Age
8. **Tenure:** The time of bond with company
9. **Balance:** The amount left with them
10. **NumOfProducts:** The products they own.
11. **HasCrCard:** Do they have a credit card or not
12. **IsActiveMember:** How active member they are
13. **EstimatedSalary:** Their estimated salary
14. **Exited:** Whether they stay in the or leave


### Preparação do conjunto de dados

Será feito todo o pré processamento necessário para melhorar o desempenho da solução que será criada. Dessa forma, o pré processamento inclui:
1. Correção de formato: modelo não aceita variáveis no formato textual
2. Correção de valores nulos: modelo não aceita dados nulos
3. Identificação e remoção de outliers: anomalias atrapalham no desempenho do modelo e devem ser tratadas
4. Feature Engineering: criação de novas varíaveis de acordo com o necessário
5. Identificação de normalidade: processo de verificação de curvas normais
6. Normalização e padronização: de acordo com o conhecimento de cada feature, será realizado o ajuste correto


### Processamento - A análise exploratória dos dados

Será realizado todo o processamento dos dados, verificação de correlações, entendimento dos perfis de análise (clientes que ficam e clientes que saem) e criação do modelo.


## Sobre a solução desenvolvida

### Análise dos resultados
Modelo é viável? Por que?


### Conversão da solução - lift esperado
De acordo com a solução desenvolvida, quais serão as melhorias?

## Publicação da solução
Deploy em nuvem

```
├── Churn_Modelling.csv
├── exploratory-data-analysis.ipynb
├── Images
│   ├── main.jpg
│   └── main_resized.jpg
├── Models
│   └── class_model.pkl
├── readme.md
├── Scalers
│   └── min_max_quantitatives.pkl
└── Scripts
    ├── data_prepare.py
    └── main.py
```