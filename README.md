# 🍔 FoodFlow AI

### Plataforma fictícia de delivery para desenvolvimento de soluções de Data & AI

> Projeto 100% sintético criado para portfólio de **AI Engineer**. Os dados, clientes, restaurantes, entregadores e pedidos são fictícios e não representam nenhuma empresa real.

## 🎯 Objetivo

Construir uma solução end-to-end inspirada em problemas comuns de marketplaces de delivery: análise operacional, previsão de cancelamento, NLP de avaliações e uma base arquitetural para RAG e serving de modelos.

## 🧠 Stack e competências demonstradas

- Python + Pandas + NumPy
- Geração de dados sintéticos reprodutíveis
- EDA e métricas de negócio
- Feature engineering e pipelines de pré-processamento
- Machine Learning com scikit-learn
- Avaliação com Precision, Recall, F1 e ROC-AUC
- NLP com TF-IDF + Logistic Regression
- Inferência opcional com Hugging Face Transformers
- Retrieval para arquitetura RAG
- API REST com FastAPI
- Docker
- Testes automatizados
- GitHub Actions / CI

## 🏗️ Arquitetura

```text
Dados sintéticos
      ↓
Python + Pandas
      ↓
EDA + métricas
      ↓
ML ───────────────→ Previsão de cancelamento
      ↓
NLP ───────────────→ Sentimento das avaliações
      ↓
Retriever ─────────→ Contexto para RAG
      ↓
FastAPI ───────────→ Serving de inferência
      ↓
Docker + CI ───────→ Operação reproduzível
```

Veja também [`docs/architecture.md`](docs/architecture.md).

## 📊 Dados sintéticos

O gerador cria:

- 5.000 clientes
- 300 restaurantes
- 800 entregadores
- 30.000 pedidos
- pagamentos associados aos pedidos
- avaliações de clientes

Os dados são gerados localmente e não são versionados no GitHub.

### Gerar os dados

```bash
python data/generate_data.py
```

## 🤖 Machine Learning

O primeiro modelo prevê a probabilidade de cancelamento usando informações disponíveis antes do desfecho do pedido, como horário, categoria, valor, distância, tempo de preparo, trânsito e forma de pagamento.

```bash
python src/train_cancellation.py
python src/evaluate_cancellation.py
```

As métricas são gravadas em `reports/cancellation_metrics.json` localmente.

## 🗣️ NLP

Baseline de sentimento:

```bash
python src/sentiment.py
```

Versão opcional com Hugging Face:

```bash
pip install -r requirements-optional.txt
python src/nlp/huggingface_sentiment.py
```

## 🔎 RAG

A camada `src/rag/` recupera avaliações semanticamente relevantes usando TF-IDF e similaridade de cosseno. Ela foi estruturada para receber posteriormente um LLM e produzir respostas fundamentadas nas evidências recuperadas.

```bash
python src/rag/qa.py
```

## 🌐 API

Depois de gerar os dados e treinar o modelo:

```bash
uvicorn api.main:app --reload
```

Endpoints principais:

- `GET /health`
- `POST /predict/cancellation`
- documentação automática em `/docs`

## 🐳 Docker

```bash
docker build -t foodflow-ai .
docker run -p 8000:8000 foodflow-ai
```

## 🧪 Testes

```bash
pytest -q
```

O GitHub Actions também executa testes, geração dos dados, EDA, treinamento do modelo e baseline de NLP.

## 📁 Estrutura

```text
foodflow-ai/
├── .github/workflows/ci.yml
├── api/
├── data/
│   ├── generate_data.py
│   └── README.md
├── docs/
├── models/
├── reports/
├── src/
│   ├── nlp/
│   ├── rag/
│   ├── eda.py
│   ├── sentiment.py
│   ├── train_cancellation.py
│   ├── evaluate_cancellation.py
│   └── predict_cancellation.py
├── tests/
├── Dockerfile
├── requirements.txt
└── requirements-optional.txt
```

## 🚀 Próximas evoluções

- publicar um modelo no Hugging Face
- transformar o retriever em RAG completo com LLM
- criar notebook pronto para Kaggle
- adicionar modelo de previsão de tempo de entrega
- incluir monitoramento e tracking de experimentos
- disponibilizar uma demonstração web

## ⚠️ Dados sintéticos

A empresa **FoodFlow** é fictícia e foi criada exclusivamente para fins educacionais e de portfólio. Nenhum dado privado ou operacional real é utilizado.

## 👩🏽‍💻 Autora

**Saionara Frossard** — AI & Machine Learning | AI Engineer em formação

GitHub: [@SaioThech](https://github.com/SaioThech)
