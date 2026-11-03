# FoodFlow AI — evidências técnicas

## Competências demonstradas

- Geração reproduzível de dados sintéticos com Python e NumPy.
- Manipulação e análise de dados com Pandas.
- Análise exploratória e geração de relatórios.
- Pré-processamento com scikit-learn Pipelines e ColumnTransformer.
- Classificação e regressão supervisionadas.
- Avaliação com métricas adequadas a cada tarefa.
- Classificação de texto com TF-IDF.
- Recuperação lexical e composição de contexto para RAG.
- API REST com FastAPI.
- Testes automatizados e integração contínua com GitHub Actions.
- Empacotamento com Docker.

## Mapa entre competência e implementação

| Área | Implementação |
|---|---|
| Geração de dados | `data/generate_data.py` |
| Análise exploratória | `src/eda.py` |
| Classificação | `src/train_cancellation.py` |
| Avaliação | `src/evaluate_cancellation.py` |
| Regressão | `src/train_delivery_time.py` |
| NLP | `src/sentiment.py` |
| Transformers (opcional) | `src/nlp/huggingface_sentiment.py` |
| Recuperação e RAG | `src/rag/` |
| API | `api/main.py` |
| Testes | `tests/` |
| CI | `.github/workflows/ci.yml` |
| Container | `Dockerfile` |

## Como apresentar o projeto

Descreva somente o que foi executado e medido. Diferencie resultados de dados sintéticos de resultados obtidos em dados reais. Não informe métricas sem anexar a execução correspondente e o conjunto de teste utilizado.
