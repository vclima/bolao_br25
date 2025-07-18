# Bolão Brasileirão 2025

## 🏆 Resultados Atuais

**Última Atualização:** 2025-07-17 21:13:07

| Time | Real | Victor | Julio | Luca |
|------|------|------|------|------|
| Flamengo | 1 | 2°(19p) | 1°(20p) | 1°(20p) |
| Cruzeiro | 2 | 14°(8p) | 17°(5p) | 11°(11p) |
| Red Bull Bragantino | 3 | 17°(6p) | 16°(7p) | 15°(8p) |
| Bahia | 4 | 4°(20p) | 6°(18p) | 7°(17p) |
| Palmeiras | 5 | 5°(20p) | 4°(19p) | 2°(17p) |
| Botafogo | 6 | 3°(17p) | 7°(19p) | 5°(19p) |
| Fluminense | 7 | 6°(19p) | 10°(17p) | 13°(14p) |
| Atlético-MG | 8 | 10°(18p) | 9°(19p) | 8°(20p) |
| Corinthians | 9 | 7°(18p) | 3°(14p) | 6°(17p) |
| Ceará | 10 | 13°(17p) | 11°(19p) | 18°(12p) |
| Mirassol | 11 | 20°(11p) | 18°(13p) | 19°(12p) |
| Grêmio | 12 | 11°(19p) | 15°(17p) | 14°(18p) |
| Santos | 13 | 12°(19p) | 13°(20p) | 4°(11p) |
| Internacional | 14 | 1°(7p) | 2°(8p) | 3°(9p) |
| Vasco da Gama | 15 | 16°(19p) | 14°(19p) | 17°(18p) |
| São Paulo | 16 | 9°(13p) | 8°(12p) | 9°(13p) |
| Vitória | 17 | 18°(19p) | 19°(18p) | 20°(17p) |
| Juventude | 18 | 15°(17p) | 12°(14p) | 12°(14p) |
| Fortaleza | 19 | 8°(9p) | 5°(6p) | 10°(11p) |
| Sport | 20 | 19°(19p) | 20°(20p) | 16°(16p) |
| **TOTAL** | | **314** | **304** | **294** |

### 🏅 Classificação Final

🥇 **Victor**: 314 pontos
🥈 **Julio**: 304 pontos
🥉 **Luca**: 294 pontos

### 🏅 Classificação Final

🥇 **Victor**: 314 pontos
🥈 **Julio**: 304 pontos
🥉 **Luca**: 294 pontos

---

## 📖 Sobre o Projeto

Script em Python que captura em tempo real a classificação do Campeonato Brasileiro 2025 e compara com as previsões dos jogadores para calcular a pontuação do bolão.

## 📁 Arquivos

- **`scrape_brasileirao_simple.py`** - Script principal que captura dados e compara previsões
- **`bolao.json`** - Previsões dos jogadores em formato JSON
- **`requirements.txt`** - Dependências (opcional, para melhorias futuras)

## 🚀 Como Usar

```bash
python scrape_brasileirao_simple.py
```

Ou com um arquivo de previsões customizado:
```bash
python scrape_brasileirao_simple.py minhas_previsoes.json
```

## ⚡ Funcionalidades

- ✅ **Captura em tempo real** da ESPN Brasil e GE Globo
- ✅ Compara classificação real com previsões dos jogadores
- ✅ Calcula pontuação: 20 pontos menos desvio absoluto
- ✅ Mostra comparação lado a lado com pontuações
- ✅ **Atualiza automaticamente este README** com tabela de resultados
- ✅ **Ordena jogadores por pontuação total** (maior primeiro)
- ✅ Exibe classificação final com medalhas
- ✅ Usa apenas bibliotecas nativas do Python

## 🎯 Sistema de Pontuação

Para cada time, os jogadores recebem:
- **20 pontos** para acerto exato da posição
- **19 pontos** para 1 posição de diferença
- **18 pontos** para 2 posições de diferença
- **...e assim por diante**
- **0 pontos** para 20+ posições de diferença

## 🌐 Fontes de Dados

O script tenta automaticamente múltiplas fontes:
1. **ESPN Brasil** (`espn.com.br`) - Fonte principal
2. **GE Globo** (`ge.globo.com`) - Fonte alternativa

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

## ⚙️ Como Funciona

1. **Captura classificação em tempo real** da ESPN Brasil ou GE Globo
2. Carrega previsões dos jogadores do arquivo JSON
3. Para cada time, compara posição prevista vs real
4. Calcula pontuação: `20 - |posição_prevista - posição_real|`
5. Soma pontuação de todos os times para cada jogador
6. Mostra resultados em tabela formatada com classificação
7. **Atualiza automaticamente este README** com tabela de resultados mais recente