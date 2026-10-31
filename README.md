# 🍔 FoodFlow AI

### Plataforma fictícia de delivery para desenvolvimento de soluções de Data & AI

> Projeto 100% sintético criado para portfólio de **AI Engineer**. Os dados, clientes, restaurantes, entregadores e pedidos são fictícios e não representam nenhuma empresa real.

## 🎯 Objetivo

Construir uma plataforma de dados e Inteligência Artificial inspirada em problemas comuns de marketplaces de delivery: previsão de cancelamento, análise de demanda, tempo de entrega, comportamento de clientes e análise de avaliações.

## 🧠 O que este projeto demonstra

- Geração e organização de dados sintéticos
- Python e Pandas
- Análise exploratória de dados (EDA)
- Engenharia de atributos (feature engineering)
- Machine Learning
- NLP e análise de sentimento
- Previsão de cancelamento de pedidos
- Previsão de tempo de entrega
- LLM/RAG como evolução do projeto
- Boas práticas de engenharia e reprodutibilidade

## 🏗️ Arquitetura planejada

```text
Dados sintéticos
      ↓
Python + Pandas
      ↓
EDA + Feature Engineering
      ↓
Machine Learning ───→ Previsão de cancelamento
      ↓
NLP ────────────────→ Sentimento das avaliações
      ↓
LLM + RAG ──────────→ Assistente FoodFlow AI
      ↓
API + MLOps ────────→ Sistema de IA em produção
```

## 📊 Dados

O gerador cria um cenário fictício de delivery com:

- clientes
- restaurantes
- entregadores
- pedidos
- pagamentos
- avaliações

A geração é determinística por seed, permitindo reproduzir os mesmos dados.

### Relações

```text
customers 1 ─── N orders N ─── 1 restaurants
                    │
                    └────────── N ─── 1 couriers
                    │
                    └────────── 1 ─── 1 payments
                    │
                    └────────── 0/1 ─── reviews
```

## 🚀 Como executar

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Gere os dados:

```bash
python data/generate_data.py
```

Execute a análise:

```bash
python src/eda.py
```

## 🔬 Próximas etapas de AI

1. EDA completa e dashboard de métricas
2. Modelo de classificação para cancelamento
3. Modelo de regressão para tempo de entrega
4. NLP para avaliações
5. Modelo publicado no Hugging Face
6. Assistente com LLM + RAG
7. API de inferência
8. Docker e CI/CD
9. Monitoramento de modelos

## ⚠️ Dados sintéticos

Este projeto não utiliza dados privados, A empresa **FoodFlow** é fictícia e foi criada exclusivamente para fins educacionais e de portfólio.

## 👩🏽‍💻 Autora

**Saionara Frossard** — AI & Machine Learning | AI Engineer em formação

GitHub: [@SaioThech](https://github.com/SaioThech)
