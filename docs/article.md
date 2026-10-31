# FoodFlow AI: construindo uma solução de AI Engineering de ponta a ponta

## Contexto

O FoodFlow AI é um projeto de portfólio baseado em uma empresa fictícia de delivery. A proposta é demonstrar como problemas de negócio podem ser transformados em uma solução técnica que percorre dados, Machine Learning, NLP, RAG e serving.

## Dados sintéticos

O projeto gera clientes, restaurantes, entregadores, pedidos, pagamentos e avaliações de forma reprodutível. Nenhum dado privado ou operacional real é utilizado.

## Primeiro problema: cancelamento

O primeiro modelo estima a probabilidade de um pedido ser cancelado antes do desfecho. As variáveis usadas incluem horário, categoria, valor, distância, tempo de preparo, trânsito e pagamento.

O pipeline separa variáveis numéricas e categóricas, aplica imputação e transformação e treina um classificador. A avaliação usa Precision, Recall, F1 e ROC-AUC para evitar depender somente de acurácia.

## Segundo problema: tempo de entrega

O projeto também possui um modelo de regressão para estimar o tempo de entrega. Nesse caso, MAE, RMSE e R² ajudam a avaliar o erro em minutos e a capacidade explicativa do modelo.

## NLP e Transformers

As avaliações dos clientes são usadas em um baseline de sentimento com TF-IDF e Logistic Regression. A arquitetura também possui uma etapa opcional com Hugging Face Transformers, mostrando a evolução de um baseline clássico para modelos pré-treinados.

## RAG

O módulo de RAG começa recuperando avaliações relevantes com TF-IDF e similaridade de cosseno. Depois, um modelo generativo opcional recebe a pergunta e as evidências recuperadas para produzir uma resposta fundamentada.

Essa separação é importante: o sistema não precisa pedir ao LLM que memorize as avaliações. Primeiro recuperamos evidências; depois geramos a resposta.

## Engenharia e produção

O projeto inclui testes automatizados, GitHub Actions, API FastAPI e Docker. Assim, o foco deixa de ser apenas treinar um modelo e passa a ser construir um sistema reproduzível.

## Conclusão

O FoodFlow AI representa uma evolução prática: dados → analytics → ML → NLP → Transformers → RAG → API → operação. Essa é a principal narrativa que quero demonstrar como estudante de Inteligência Artificial e candidata a uma trajetória de AI Engineer.

> Observação: resultados numéricos devem ser atualizados a partir da execução do pipeline; o repositório não versiona artefatos gerados localmente.
