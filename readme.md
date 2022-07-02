# Predição de saída de clientes

## O problema abordado

Prever a rotatividade da empresa é algo fundamental para se alcançar melhores resultados. Ter o conhecimento de que determinado cliente pode estar prester a sair da empresa permite que a mesma busque reconquistá-lo, de modo a mantê-lo presente consumindo seus produtos e serviços.

A perda de um cliente para a concorrência pode ser um grande prejuízo individual, já que a empresa perde um comprador, mas também pode acarretar prejuízos coletivos como efeito manada de evasão (clientes saem porque outros saíram) por exemplo. Além do mais, um cliente sempre será uma forma considerável de propaganda e isso deve ser sempre levado em consideração: resumidamente, cliente contente pode fazer propaganda positiva da empresa para outros e clientes descontentes podem fazer propaganda negativa.

Quanto mais se entende esse cenário, entendende-se também a importância de prever a saída de clientes. Dessa forma, enxergar que um cliente está prestes a sair (com uma estimativa disso em termos probabilísticos também) é de grande relevância e isso pode ser feito com a Ciência de Dados. 

![main](Images/main_resized.jpg)

Supondo que se tenha os dados registrados sobre clientes e a relação deles com os produtos/serviços da empresa, pode-se visualizar o quanto o cliente gera de receita para a empresa em um determinado período de tempo. 

Se um cliente gera Y reais, em média, de receita mensal para a empresa, em um ano teria-se Y x 12 reais. No cenário em que em um ano a empresa perde 10% de seus clientes já existentes e o número total é de 3000 clientes, então **todo ano perde-se cerca de 300 x Y x 12 reais, que poderiam ser recebidos pela empresa**. 

Portanto, além de investir em novos clientes, deve-se também investir em manter os que já faziam parte da empresa.

### A solução proposta ??

Desenvolver um modelo preditivo capaz de estimar se determinado cliente vai ou não sair da empresa para que se tenha esse conhecimento e para que se possa tomar medidas que o mantenham na empresa.

A ideia é desenvolver um sistema que periodicamente calcule tal probabilidade e informe isso, informando também as principais características desses clientes.

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