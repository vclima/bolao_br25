# Bolão Brasileirão 2025

## 🏆 Resultados Atuais

**Última Atualização:** 2025-07-25 00:12:59

| Time | Real | Victor | Julio | Luca |
|------|------|------|------|------|
| Cruzeiro | 1 | 14°(7p) | 17°(4p) | 11°(10p) |
| Flamengo | 2 | 2°(20p) | 1°(19p) | 1°(19p) |
| Palmeiras | 3 | 5°(18p) | 4°(19p) | 2°(19p) |
| Red Bull Bragantino | 4 | 17°(7p) | 16°(8p) | 15°(9p) |
| Botafogo | 5 | 3°(18p) | 7°(18p) | 5°(20p) |
| Bahia | 6 | 4°(18p) | 6°(20p) | 7°(19p) |
| Mirassol | 7 | 20°(7p) | 18°(9p) | 19°(8p) |
| Fluminense | 8 | 6°(18p) | 10°(18p) | 13°(15p) |
| Atlético-MG | 9 | 10°(19p) | 9°(20p) | 8°(19p) |
| Internacional | 10 | 1°(11p) | 2°(12p) | 3°(13p) |
| Corinthians | 11 | 7°(16p) | 3°(12p) | 6°(15p) |
| São Paulo | 12 | 9°(17p) | 8°(16p) | 9°(17p) |
| Ceará | 13 | 13°(20p) | 11°(18p) | 18°(15p) |
| Grêmio | 14 | 11°(17p) | 15°(19p) | 14°(20p) |
| Vitória | 15 | 18°(17p) | 19°(16p) | 20°(15p) |
| Vasco da Gama | 16 | 16°(20p) | 14°(18p) | 17°(19p) |
| Santos | 17 | 12°(15p) | 13°(16p) | 4°(7p) |
| Juventude | 18 | 15°(17p) | 12°(14p) | 12°(14p) |
| Fortaleza | 19 | 8°(9p) | 5°(6p) | 10°(11p) |
| Sport | 20 | 19°(19p) | 20°(20p) | 16°(16p) |
| **TOTAL** | | **310** | **302** | **300** |

### 🏅 Classificação Final (pontuação normalizada 0-100)

🥇 **Victor**: 55 pontos
🥈 **Julio**: 51 pontos
🥉 **Luca**: 50 pontos

### 📈 Histórico de Desempenho

![Gráfico de Performance](performance_chart.png)

| Rodada | Victor | Luca | Julio |
|-------|-------|-------|-------|
| R14 | 57 | 46 | 51 |
| R15 | 55 | 45 | 51 |
| R16 | 54 | 48 | 50 |
| R16 | 55 | 50 | 51 |

**Tendência (últimas 2 medições):**
- **Victor**: 📈 +1
- **Luca**: 📈 +2
- **Julio**: 📈 +1

## 📖 Sobre o Projeto

Script em Python que captura em tempo real a classificação do Campeonato Brasileiro 2025 e compara com as previsões dos jogadores para calcular a pontuação do bolão.

## 📁 Arquivos

- **`scrape_brasileirao_simple.py`** - Script principal que captura dados e compara previsões
- **`bolao.json`** - Previsões dos jogadores em formato JSON
- **`requirements.txt`** - Dependências Python (matplotlib para gráficos)
- **`performance_chart.png`** - Gráfico visual gerado automaticamente
- **`score_history.json`** - Histórico de pontuações (gerado automaticamente)
- **`update_bolao.bat`** - Script de automação para Windows (execução + Git)

## 🚀 Como Usar

### Execução Manual
```bash
python scrape_brasileirao_simple.py
```

Ou com um arquivo de previsões customizado:
```bash
python scrape_brasileirao_simple.py minhas_previsoes.json
```

Para forçar atualização (ignorar checagem de mudanças):
```bash
python scrape_brasileirao_simple.py force
```

### Execução Automatizada (Windows)
Use o arquivo `update_bolao.bat` para execução automatizada com Git:

```batch
# Execução normal
update_bolao.bat

# Forçar atualização
update_bolao.bat -f
```

O script `.bat` automaticamente:
- 🐍 **Ativa o ambiente conda** (qt) se disponível
- 📊 **Executa o scraper** e atualiza dados
- 📝 **Faz commit e push** das alterações para o Git
- 🔄 **Funciona fora do VS Code** com detecção automática do ambiente Python

**Requisitos para o `.bat`:**
- Windows com conda/anaconda instalado, OU Python no PATH do sistema
- Git configurado (`git config --global user.name` e `user.email`)
- Repositório Git inicializado e conectado ao GitHub

## ⚡ Funcionalidades

- ✅ **Captura em tempo real** da ESPN Brasil e GE Globo
- ✅ Compara classificação real com previsões dos jogadores
- ✅ Calcula pontuação: 20 pontos menos desvio absoluto
- ✅ Mostra comparação lado a lado com pontuações
- ✅ **Atualiza automaticamente este README** com tabela de resultados
- ✅ **Ordena jogadores por pontuação total** (maior primeiro)
- ✅ Exibe classificação final com medalhas
- ✅ **Histórico de desempenho com gráfico visual** usando matplotlib
- ✅ **Detecção automática de mudanças** - só atualiza quando necessário
- ✅ Usa apenas bibliotecas nativas do Python (matplotlib opcional para gráficos)


## 🎯 Sistema de Pontuação

Para cada time, os jogadores recebem:
- **20 pontos** para acerto exato da posição
- **19 pontos** para 1 posição de diferença
- **18 pontos** para 2 posições de diferença
- ...até **1 ponto** para 19 posições de diferença
- **0 pontos** para 20 ou mais posições de diferença

**Pontuação total mínima possível:** 200 pontos
**Pontuação total máxima possível:** 400 pontos

**Pontuação final normalizada:**
`pontuação_normalizada = (pontuação_total - 200) / 2`
O resultado final sempre estará entre 0 e 100.

## 📈 Histórico e Gráficos

O sistema automaticamente:
- **Rastreia mudanças nas pontuações** a cada execução
- **Salva histórico em JSON** (`score_history.json`) apenas quando há mudanças
- **Gera gráfico visual** (`performance_chart.png`) usando matplotlib quando disponível
- **Gera tabela de evolução** no README mostrando últimas 10 medições
- **Indica tendências** comparando as duas últimas medições com emojis:
  - 📈 Subiu pontuação
  - 📉 Desceu pontuação  
  - ➡️ Manteve pontuação

### Gráfico Visual
O sistema gera automaticamente um gráfico de linhas mostrando a evolução das pontuações ao longo das rodadas, com:
- ✨ Cores diferentes para cada jogador
- 📊 Anotações com as pontuações mais recentes
- 🏁 Eixo X mostrando as rodadas do campeonato (R15, R16, etc.)
- 🎯 Escala de 0-100 pontos normalizados
- 📈 Rodada calculada automaticamente pelo maior número de jogos disputados

### Exemplo de Saída do Histórico

| Data/Hora | Victor | Luca | Julio |
|-------|-------|-------|-------|
| 17/07 23:32 | 55 | 44 | 49 |
| 18/07 10:15 | 56 | 45 | 50 |
| 18/07 13:14 | 57 | 46 | 51 |

**Tendência:** Victor 📈 +1, Luca 📈 +1, Julio 📈 +1

## 🌐 Fontes de Dados

O script tenta automaticamente múltiplas fontes confiáveis:
1. **ESPN Brasil** (`espn.com.br`) - Fonte principal
2. **Gazeta Esportiva** (`gazetaesportiva.com`) - Fonte alternativa confiável

## 💻 Exemplo de Saída

```
🏆 BRASILEIRÃO 2025 - BOLÃO RESULTS
Updated: 2025-07-17 21:00:05
================================================================================
Time                 Real    Victor      Julio       Luca
--------------------------------------------------------------------------------
Flamengo             1       2°(19p) 1°(20p) 1°(20p)
Palmeiras            2       5°(17p) 4°(19p) 2°(20p)
São Paulo            3       9°(14p) 8°(15p) 9°(14p)
...
--------------------------------------------------------------------------------
PONTUAÇÃO FINAL:             314         304         294

🏅 CLASSIFICAÇÃO:
1. Victor: 314 pontos
2. Julio: 304 pontos
3. Luca: 294 pontos
```

## 📋 Formato JSON para Previsões

O arquivo de previsões deve seguir esta estrutura:

```json
{
    "NomeJogador": {
        "1": "NomeTime",
        "2": "NomeTime",
        "3": "NomeTime",
        ...
        "20": "NomeTime"
    },
    "OutroJogador": {
        "1": "NomeTime",
        ...
    }
}
```

## 🛠️ Requisitos

- Python 3.6+ (usa apenas bibliotecas nativas)
- matplotlib (opcional, para gráficos visuais)

Para instalar matplotlib:
```bash
pip install matplotlib
```

## ⚙️ Como Funciona

1. **Captura classificação em tempo real** da ESPN Brasil ou GE Globo
2. Carrega previsões dos jogadores do arquivo JSON
3. Para cada time, compara posição prevista vs real
4. Calcula pontuação: `20 - |posição_prevista - posição_real|`
5. Soma pontuação de todos os times para cada jogador
6. Mostra resultados em tabela formatada com classificação
7. **Atualiza automaticamente este README** com tabela de resultados mais recente