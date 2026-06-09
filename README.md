# Mission Control AI 

Sistema de monitoramento de missão espacial desenvolvido em Python para a Global Solution 2026.1 da FIAP.

O programa analisa ciclos de monitoramento de uma missão espacial, classifica o nível de risco de cada ciclo, identifica tendências e gera um relatório final no terminal.

### INTEGRANTES
- Sergio Augusto Amaral - RM: 570184
- Giovanni Merlotti - RM: 573721
- Gabriel Freitas - RM: 572943
---

## Como executar

Não são necessárias bibliotecas externas — apenas Python 3.

```bash
python mission_control.py
```

---

## Estrutura dos dados

A missão é representada pela matriz `dados_missao`. Cada linha é um ciclo e cada coluna é uma variável monitorada:

```
[temperatura, comunicacao, bateria, oxigenio, estabilidade]
```

| Posição | Variável     | Unidade |
|---------|--------------|---------|
| 0       | Temperatura  | °C      |
| 1       | Comunicação  | %       |
| 2       | Bateria      | %       |
| 3       | Oxigênio     | %       |
| 4       | Estabilidade | %       |

---

## Regras de alerta

Cada variável é classificada como **NORMAL**, **ATENÇÃO** ou **CRÍTICO**:

| Variável     | ATENÇÃO              | CRÍTICO     | NORMAL        |
|--------------|----------------------|-------------|---------------|
| Temperatura  | < 18°C ou 30–35°C    | > 35°C      | 18–30°C       |
| Comunicação  | 30–59%               | < 30%       | ≥ 60%         |
| Bateria      | 20–49%               | < 20%       | ≥ 50%         |
| Oxigênio     | 80–89%               | < 80%       | ≥ 90%         |
| Estabilidade | 40–69%               | < 40%       | ≥ 70%         |

---

## Pontuação e classificação

Cada classificação gera uma pontuação por ciclo:

| Classificação | Pontos |
|---------------|--------|
| NORMAL        | 0      |
| ATENÇÃO       | 1      |
| CRÍTICO       | 2      |

A soma das 5 variáveis define a situação do ciclo:

| Pontuação | Situação           |
|-----------|--------------------|
| 0 – 2     | MISSÃO ESTÁVEL     |
| 3 – 5     | MISSÃO EM ATENÇÃO  |
| 6 – 10    | MISSÃO CRÍTICA     |

---

## Funções

| Função                          | O que faz                                              |
|---------------------------------|--------------------------------------------------------|
| `analisar_temperatura()`        | Classifica a temperatura e retorna pontuação           |
| `analisar_comunicacao()`        | Classifica a comunicação e retorna pontuação           |
| `analisar_bateria()`            | Classifica a bateria e retorna pontuação               |
| `analisar_oxigenio()`           | Classifica o oxigênio e retorna pontuação              |
| `analisar_estabilidade()`       | Classifica a estabilidade e retorna pontuação          |
| `classificar_ciclo()`           | Define a situação geral do ciclo pela pontuação total  |
| `gerar_recomendacao()`          | Gera recomendações automáticas com base nos alertas    |
| `analisar_tendencia()`          | Compara o primeiro e o último ciclo                    |
| `identificar_area_mais_afetada()` | Encontra a área com maior risco acumulado            |
| `analisar_ciclos()`             | Percorre todos os ciclos e exibe os resultados         |
| `gerar_relatorio_final()`       | Exibe o resumo consolidado da missão                   |

---

## Missão simulada

- **Nome:** Aether  
- **Equipe:** Stig4 Space 
- **Ciclos:** 7

```python
dados_missao = [
    [22, 95, 91, 98, 93],  # Ciclo 1 - Início da missão
    [26, 83, 76, 95, 88],  # Ciclo 2 - Estabilização
    [32, 67, 55, 90, 72],  # Ciclo 3 - Queda parcial de comunicação
    [37, 44, 35, 85, 52],  # Ciclo 4 - Alerta de energia
    [41, 25, 17, 76, 32],  # Ciclo 5 - Risco operacional máximo
    [35, 58, 28, 83, 48],  # Ciclo 6 - Tentativa de recuperação
    [30, 72, 43, 88, 65],  # Ciclo 7 - Recuperação em progresso
]
```
