# Base de Conhecimento em Prolog: Mercado de Criptomoedas

Este projeto tem como objetivo construir um mecanismo de busca utilizando Lógica de Primeira Ordem (Prolog). A partir de um dataset real, foi desenvolvido um processo de ETL em Python para transformar os dados em uma base de conhecimento composta por fatos lógicos, permitindo a realização de consultas estruturadas.

---

## Dataset

O dataset utilizado foi o **Cryptocurrency Market Dataset**, disponível no [Kaggle](https://www.kaggle.com/datasets/ashyou09/cryptocurrency-market-dataset).

Foram selecionados 7 atributos, combinando variáveis qualitativas e quantitativas:

* `coin_id`
* `symbol`
* `current_price_usd`
* `market_cap_rank`
* `price_change_24h_percent`
* `all_time_high_usd`
* `total_volume_usd`

A base foi limitada a 500 registros para otimizar e facilitar a execução das consultas no compilador Prolog online.

Durante o ETL, os dados passaram por:

* padronização de strings (minúsculas, sem espaços e remoção de caracteres especiais)
* conversão de tipos numéricos
* remoção de valores nulos ou inválidos

---

## Como executar

### 1. Gerar a base de conhecimento

Execute o script Python:

```bash
python etl.py
```

Isso irá gerar o arquivo `base_conhecimento.pl`, contendo os fatos no formato:

```prolog
crypto(Id, Symbol, Price, Rank, Change24h, ATH, Volume).
```

---

### 2. Executar consultas em Prolog

1. Acesse o compilador online: [SWISH SWI-Prolog](https://swish.swi-prolog.org/)
2. Cole o conteúdo de `base_conhecimento.pl` e `perguntas.pl` na área **Program** (à esquerda)
3. Execute as consultas na área **Query** (canto inferior direito)

---

## Consultas

### Pergunta 1: Ranking de valorização

**Objetivo:** identificar as 10 criptomoedas com maior variação positiva nas últimas 24h.

**Query:**

```prolog
?- ranking_valorizacao(Top10).
```

**Lógica:** construção de lista com `findall`, ordenação com `sort`, inversão com `reverse` e limitação para o top 10 usando `length` e `append`.

---

### Pergunta 2: Desconto em relação ao ATH

**Objetivo:** encontrar criptomoedas cujo preço atual está abaixo de 20% do seu valor máximo histórico.

**Query:**

```prolog
?- desconto_historico(Moeda, Preco, ATH, Razao).
```

**Lógica:** cálculo da razão `Preco / ATH` com restrição condicional `ATH > 0` (para evitar divisão por zero) e filtro lógico `Razao < 0.2`.

---

### Pergunta 3: Média de volume no Top N

**Objetivo:** calcular a média do volume de negociação entre as criptomoedas até um determinado rank.

**Query:**

```prolog
?- media_volume_top(20, Media).
```

**Lógica:** filtragem por rank limitador, agregação dos volumes com `findall` e cálculo da média usando as funções nativas `sum_list` e `length`.
