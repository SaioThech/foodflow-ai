# 🍔 FoodFlow AI

### Plataforma fictícia de delivery para desenvolvimento de soluções de Data & AI

> Projeto 100% sintético criado para portfólio de **AI Engineer**. Os dados, clientes, restaurantes, entregadores e pedidos são fictícios e não representam nenhuma empresa real.

## 🎯 Objetivo

Construir uma solução end-to-end inspirada em problemas comuns de marketplaces de delivery: análise operacional, previsão de cancelamento, previsão de tempo de entrega, NLP, RAG e serving de modelos.

## 🧠 Stack e competências

- Python + Pandas + NumPy
- Geração de dados sintéticos reprodutíveis
- EDA e métricas de negócio
- Feature engineering e pipelines de pré-processamento
- Machine Learning com scikit-learn
- Classificação e regressão
- Precision, Recall, F1, ROC-AUC, MAE, RMSE e R²
- NLP com TF-IDF + Logistic Regression
- Transformers com Hugging Face
- Retrieval + RAG com LLM opcional
- API REST com FastAPI
- Docker
- Testes automatizados
- GitHub Actions / CI
- Notebook preparado para Kaggle

## 🏗️ Arquitetura

```text
Dados sintéticos
      ↓
Python + Pandas
      ↓
EDA + Feature Engineering
      ↓
 ┌───────────────┬────────────────┐
 ↓               ↓                ↓
ML cancelamento  ML entrega      NLP
 ↓               ↓                ↓
 └───────────────┴────────────────┘
                 ↓
          Retriever / RAG
                 ↓
             LLM opcional
                 ↓
             FastAPI
                 ↓
           Docker + CI
```

Veja [`docs/architecture.md`](docs/architecture.md).

## 📊 Dados sintéticos

O gerador cria 5.000 clientes, 300 restaurantes, 800 entregadores, 30.000 pedidos, pagamentos e avaliações. Os dados são gerados localmente e não são versionados.

```bash
python data/generate_data.py
```

## 🤖 Machine Learning

### Cancelamento

```bash
python src/train_cancellation.py
python src/evaluate_cancellation.py
```

### Tempo de entrega

```bash
python src/train_delivery_time.py
```

As métricas e modelos são gerados localmente e ignorados pelo Git.

## 🗣️ NLP e Transformers

Baseline:

```bash
python src/sentiment.py
```

Transformers:

```bash
pip install -r requirements-optional.txt
python src/nlp/huggingface_sentiment.py
```

## 🔎 RAG + LLM

A primeira etapa recupera avaliações relevantes com TF-IDF. A segunda etapa pode enviar o contexto recuperado para um modelo generativo opcional.

Somente recuperação:

```bash
python src/rag/qa.py
```

Para geração, instale as dependências opcionais e use `answer_with_retrieval(..., generate=True)`.

## 🌐 API

Depois de gerar os dados e treinar o modelo:

```bash
uvicorn api.main:app --reload
```

Endpoints: `GET /health` e `POST /predict/cancellation`. A documentação fica em `/docs`.

## 🐳 Docker

```bash
docker build -t foodflow-ai .
docker run -p 8000:8000 foodflow-ai
```

## 🧪 Testes e CI

```bash
pytest -q
```

O GitHub Actions valida sintaxe, executa testes, gera dados, roda EDA, treina e avalia os modelos e executa o baseline de NLP.

## 📓 Kaggle

O notebook [`kaggle/01_foodflow_ml.ipynb`](kaggle/01_foodflow_ml.ipynb) apresenta o fluxo de análise e ML em formato pronto para adaptação/publicação no Kaggle.

## 📁 Estrutura

```text
foodflow-ai/
├── .github/workflows/ci.yml
├── api/
├── data/
├── docs/
├── kaggle/
├── models/
├── reports/
├── src/
│   ├── nlp/
│   ├── rag/
│   ├── eda.py
│   ├── sentiment.py
│   ├── train_cancellation.py
│   ├── evaluate_cancellation.py
│   ├── train_delivery_time.py
│   └── predict_cancellation.py
├── tests/
├── Dockerfile
├── requirements.txt
└── requirements-optional.txt
```

## 🚀 Evidências de portfólio

- Dados → `data/generate_data.py`
- Analytics → `src/eda.py`
- Classificação → `src/train_cancellation.py`
- Regressão → `src/train_delivery_time.py`
- NLP → `src/sentiment.py`
- Transformers → `src/nlp/huggingface_sentiment.py`
- RAG → `src/rag/`
- API → `api/main.py`
- MLOps/CI → `.github/workflows/ci.yml`
- Kaggle → `kaggle/01_foodflow_ml.ipynb`
- Artigo técnico → `docs/article.md`

## ⚠️ Dados sintéticos

A empresa **FoodFlow** é fictícia e foi criada exclusivamente para fins educacionais e de portfólio. Nenhum dado privado ou operacional real é utilizado.

## 👩🏽‍💻 Autora

**Saionara Frossard** — AI & Machine Learning | AI Engineer em formação

GitHub: [@SaioThech](https://github.com/SaioThech)
