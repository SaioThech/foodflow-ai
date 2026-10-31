# 🧠 FoodFlow AI

### Sistema de Engenharia de Inteligência Artificial para análise de dados e aplicações de ML, NLP e LLM

> Projeto 100% sintético criado para portfólio de **AI Engineer**. Os dados são gerados localmente e não representam uma empresa ou operação real.

## 🎯 Objetivo

Construir um sistema end-to-end que demonstre competências de Engenharia de IA: geração e preparação de dados, análise exploratória, feature engineering, treinamento e avaliação de modelos, NLP, recuperação de informação, RAG, integração com LLMs e serving por API.

## 🧠 Stack técnica

- Python
- Pandas + NumPy
- Scikit-learn
- Feature engineering e pipelines de pré-processamento
- Classificação e regressão
- Precision, Recall, F1, ROC-AUC, MAE, RMSE e R²
- NLP com TF-IDF
- Transformers com Hugging Face
- Retrieval + RAG
- LLM opcional
- FastAPI
- Docker
- Pytest
- GitHub Actions / CI

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
Classificação  Regressão         NLP
 ↓               ↓                ↓
 └───────────────┴────────────────┘
                 ↓
       Retrieval / RAG
                 ↓
            LLM opcional
                 ↓
             FastAPI
                 ↓
          Docker + CI
```

Veja [`docs/architecture.md`](docs/architecture.md).

## 📊 Dados sintéticos

O gerador cria um conjunto controlado de dados para experimentação de Machine Learning e NLP. Os arquivos gerados localmente não são versionados.

```bash
python data/generate_data.py
```

## 🤖 Machine Learning

### Classificação

```bash
python src/train_cancellation.py
python src/evaluate_cancellation.py
```

### Regressão

```bash
python src/train_delivery_time.py
```

Os modelos e relatórios gerados localmente são ignorados pelo Git.

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

A primeira etapa recupera documentos relevantes usando TF-IDF. A segunda etapa pode enviar o contexto recuperado para um modelo generativo opcional.

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

Endpoints principais: `GET /health` e `POST /predict/cancellation`. A documentação fica disponível em `/docs`.

## 🐳 Docker

```bash
docker build -t foodflow-ai .
docker run -p 8000:8000 foodflow-ai
```

## 🧪 Testes e CI

```bash
pytest -q
```

O GitHub Actions valida a sintaxe, executa testes automatizados, gera dados e executa etapas de análise, treinamento, avaliação e NLP. Workflows desse tipo permitem automatizar build e testes a cada alteração do repositório. citeturn965697search0turn965697search1

## 📓 Kaggle

O notebook [`kaggle/01_foodflow_ml.ipynb`](kaggle/01_foodflow_ml.ipynb) apresenta o fluxo de análise e Machine Learning para experimentação.

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

## 🚀 Evidências técnicas

- Dados → `data/generate_data.py`
- Analytics/EDA → `src/eda.py`
- Classificação → `src/train_cancellation.py`
- Regressão → `src/train_delivery_time.py`
- NLP → `src/sentiment.py`
- Transformers → `src/nlp/huggingface_sentiment.py`
- RAG → `src/rag/`
- API → `api/main.py`
- CI → `.github/workflows/ci.yml`
- Notebook → `kaggle/01_foodflow_ml.ipynb`
- Documentação técnica → `docs/article.md`

## ⚠️ Dados sintéticos

O nome **FoodFlow** identifica apenas o ambiente fictício utilizado neste projeto. Nenhum dado privado ou operacional real é utilizado.

## 👩🏽‍💻 Autora

**Saionara Frossard** — AI & Machine Learning | AI Engineer em formação

GitHub: [@SaioThech](https://github.com/SaioThech)
