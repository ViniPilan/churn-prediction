# Resolvendo problema de saída de clientes com Data Science

## Sumário
1. Sobre o problema de negócio abordado
    - Introdução
    - Sobre valores - quantificando o problema
    - A solução proposta: desempenho, desempenho esperado e Lift

2. Desenvolvimento da solução
    - Coleta e acesso aos dados
    - Pre processamento e processamento das informações
    - Colocando o modelo para funcionar - deploy em nuvem

3. Conclusão e considerações

4. Sobre o autor

## Sobre o problema de negócio abordado
### Introdução
Prever a sáida de cleintes de uma empresa é algo fundamental para se alcançar melhores resultados. Ter o **conhecimento de que determinado cliente pode estar prestes a sair da empresa permite que a mesma busque reconquistá-lo**, de modo a mantê-lo presente consumindo seus produtos e serviços.

**A perda de um cliente para a concorrência pode ser um grande prejuízo** individual, já que a empresa perde um comprador, mas também pode acarretar prejuízos coletivos como efeito manada de evasão (clientes saem porque outros saíram) por exemplo. Além do mais, um cliente sempre será uma forma forte de propaganda e isso deve ser sempre levado em consideração: resumidamente, cliente contente pode fazer propaganda positiva da empresa para outros e clientes descontentes podem fazer propaganda negativa.


![main](Images/main_resized.jpg)


Quanto mais se entende esse cenário, mais se compreende também a importância de prever a saída de clientes. Dessa forma, enxergar que um cliente está prestes a sair (com uma estimativa disso em termos probabilísticos também) é de grande relevância e isso pode ser feito com a Ciência de Dados. 

Para o problema em questão, iremos imaginar um cenário de uma empresa de crédito.


### Sobre valores - quantificando o problema
O saldo médio mensal de clientes que saem está estimado (com 95% de confiança) entre 7381.18 e 7803.58 dólares. Isso nos dá uma média de 7592.38 dólares mensais. 

Considerando a amostra de valores disponíveis para este estudo (e considerando o maior erro de proporção possível caso essa amostra não seja de qualidade), temos que a proporção de clientes que saíram está entre 16.29% e 24.45%. 

<span style="color:#bd7a1c">
<p><strong>Probabiidade de saída de um cliente:</strong> aproximadamente 25%</p>

<p><strong>Saldo mensal estimado de um cliente que saiu:</strong> cerca de 7.600 dólares</p>
</span>

Se considerarmos que a amostra é do período de um ano, temos no pior cenário (maior taxa de saída) que:

![saida](Images/estimativa_saida.jpg)

Nessas condições:
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

Vale ressaltar que esses valores são esperados se o modelo for utilizado em um cenário de distribuição amostral semelhante ao que foi utilizado nesse projeto. Por essa razão, deve-se treinar novamente este ou um novo modelo se os dados forem extraídos de outra população. 

#### LIFT esperado

Supondo que seja possível enviar benefícios para aqueles clientes que estão prestes a sair como tentativa de mantê-los na empresa e, supondo também, que **a cada 10 pessoas que recebem tais benefícios, 30% mudam de ideia e decidem não ficar**. Temos então:

- Se for considerado o **acaso** como solução do problema, teriamos então 50% de acerto do modelo. Para cada 100 pessoas que sairiam, ele acertaria 50 e, dessas 50, **15 mudariam de ideia (30% dos acertos positivos)**.
- Se for considerado o **modelo desenvolvido** como solução do problema (e considerando o *pior caso para falso negativo de 28%*) teriamos que a cada 100 pessoas que sairiam, ele acertaria 72 delas e, aproximadamente, **21 delas mudariam de ideia (30% dos acertos positivos).**

Portanto, é possível ver que o modelo teria **6% a mais de eficiência que o acaso** mesmo no *pior caso possível de erro estimado*. Para o abandono calculado de 25% (37.961.900 dólares a menos em cada mês), uma queda de 6% **diminuiria o abandono para 19% (28.851.044 dólares)**. Isso seria uma diferença de: **37.961.900 - 28.851.044 =  9.110.856 dólares** (9,11 milhões de dólares no PIOR caso).

Lembrando que esses 9,11 milhões são o conjunto do saldo mensal (dinheiro que o cliente coloca no banco por mês) de todos os clientes por mês.


## Dados usados no desenvolvimento da solução
Para mais informações sobre essa sessão, acesse o notebook da análise exploratória dos dados na pasta *Notebooks*.

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


### Preparação do conjunto de dados - o pré processamento

Foi feito todo o pré processamento necessário para melhorar o desempenho da solução. Dessa forma, o pré processamento incluiu:
1. Correção de formato: modelo não aceita variáveis no formato textual
2. Correção de valores nulos: modelo não aceita dados nulos
3. Identificação e remoção de outliers: anomalias atrapalham no desempenho do modelo e devem ser tratadas
4. Feature Engineering: criação de novas varíaveis de acordo com o necessário
5. Identificação de normalidade: processo de verificação de curvas normais
6. Normalização e padronização: de acordo com o conhecimento de cada feature, será realizado o ajuste correto


### Processamento - A análise exploratória dos dados

Foi realizado todo o processamento dos dados, verificação de correlações, entendimento dos perfis de análise (clientes que ficam e clientes que saem) e criação do modelo.

### Colocando a solução para funcionar - o deploy na nuvem
Para que fosse possível facilitar o acesso ao modelo, foi desenvolvida uma API em flask e o deploy do modelo na plataforma *heroku*. Para utilizar o modelo, basta que seja feita uma **solicitação POST** para o seguinte endereço:

https://vinipilan-churn-model.herokuapp.com/predict

O modelo deve receber via essa solicitação um data frame contendo um cliente ou mais no formato json. As colunas desse data frame são as seguintes (obrigatóriamente nessa ordem):
- CreditScore
-  Gender_Male
-  Age
-  Balance
-  NumOfProducts
-  HasCrCard
-  IsActiveMember
-  EstimatedSalary
-  Geography_France
-  Geography_Germany
-  Geography_Spain
-  Surname_freq

Ao realizar tal request, será devolvido um data frame (no formato json) com a predição e a probabilidade estimada de saída do cliente enviado. Exemplo:
```
[{'CreditScore': 0.5706695005,
  'Gender_Male': 1,
  'Age': 0.4,
  'Balance': 0.32960506,
  'NumOfProducts': 0.0,
  'HasCrCard': 1,
  'IsActiveMember': 0,
  'EstimatedSalary': 0.3742518722,
  'Geography_France': 1,
  'Geography_Germany': 0,
  'Geography_Spain': 0,
  'Surname_freq': 0.1016949153,
  'Prediction': 0,
  'Prediction_prob': 0.22}]
```

## Conclusão e considerações

Para o problema abordado foi desemvolvida uma solução utilizando Data Science e Machine Learning. Como foi apresentado nesse documento, a solução apresenta ganho significativo para a empresa e, por ser facilmente implementada, é também bastante viável.

A implementação via nuvem (com API) feita possibilita que essa solução seja utilizada em larga escala. Vale ressaltar que os dados foram retirados de um data set do kaggle e por isso eles foram considerados como uma amostra pouco representativa. Dessa forma, foi estimado o pior erro possível estimado para criar as conclusões de desempenho. 

Para uso eficiente da solução, ela deve ser construída com dados referentes a empresa. A solução feita aqui é apenas uma demonstração de conhecimento para portifólio.

## Sobre o autor
Me chamo Vinícius de Paula Pilan e sou estudante da área de dados. Busco alcançar autoridade nessa área e me tornar um cientista de dados profissional.

Tenho conhecimento teórico e prático sobre os principais conceitos de estatística, modelagem e ciência de dados. Meu currículo completo, minhas certificações, experiências, meus projetos e formas de contato podem ser acessadas através do meu site:

https://sites.google.com/view/vinicius-pilan/

Atualmente, sou estudante de Ciência da Computação na universidade estadual paulista UNESP, no campus de Bauru, e busco uma oportunidade para me desenvolver profissionalmente.