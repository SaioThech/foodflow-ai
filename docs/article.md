# FoodFlow AI: implementação de um pipeline de Engenharia de IA

## Escopo

FoodFlow AI é um projeto experimental de portfólio. O objetivo técnico é demonstrar um fluxo reproduzível que começa na geração de dados e termina em modelos avaliados e funcionalidades acessíveis por API. Todos os dados são sintéticos.

## Geração e análise de dados

O módulo `data/generate_data.py` cria tabelas estruturadas e registros textuais usando uma semente fixa. O módulo `src/eda.py` calcula estatísticas agregadas, exporta tabelas de análise e gera um gráfico temporal.

## Modelos preditivos

O pipeline de classificação usa Logistic Regression, com imputação de valores ausentes, padronização de variáveis numéricas e One-Hot Encoding de variáveis categóricas. A avaliação registra Accuracy, Precision, Recall, F1 e ROC-AUC.

O pipeline de regressão usa Random Forest Regressor. As métricas MAE, RMSE e R² permitem avaliar o erro de previsão e o ajuste do modelo.

## Processamento de linguagem natural

O baseline de NLP transforma texto em vetores TF-IDF e treina um classificador Logistic Regression. Há também um módulo opcional baseado em Transformers da Hugging Face. Essa etapa opcional requer dependências adicionais e pode exigir download de pesos.

## Recuperação de informação e RAG

O retriever usa TF-IDF e similaridade de cosseno para localizar registros textuais relacionados à consulta. O módulo de QA organiza os resultados em contexto e pode, opcionalmente, encaminhá-los a um modelo generativo. A recuperação funciona sem instalar o modelo generativo.

## API e validação

A API FastAPI disponibiliza health check, previsão de classificação e consulta de recuperação. O projeto inclui testes automatizados e um workflow GitHub Actions que verifica sintaxe, executa os testes, gera os dados, roda a análise exploratória e treina/avalia os modelos.

## Limitações

- Os dados são sintéticos e não permitem concluir como os modelos se comportariam em produção.
- O baseline TF-IDF é uma abordagem lexical; não equivale a busca semântica por embeddings.
- A geração com LLM é opcional e não faz parte do caminho obrigatório de CI.
- Os modelos e relatórios são artefatos locais; os resultados devem ser reproduzidos antes de serem citados em uma apresentação ou candidatura.

## Execução

Consulte o README para instalar dependências e executar o pipeline na ordem correta.
