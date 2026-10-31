"""Optional generative layer for the FoodFlow RAG pipeline.

Install optional dependencies before using this module:
    pip install -r requirements-optional.txt
"""

from transformers import pipeline

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"


def build_generator():
    return pipeline("text-generation", model=MODEL_NAME)


def generate_answer(query: str, context: str) -> str:
    generator = build_generator()
    prompt = (
        "Você é um analista da plataforma FoodFlow. Responda em português, "
        "use somente as evidências fornecidas e deixe claro quando não houver evidência suficiente.\n\n"
        f"Pergunta: {query}\n\nEvidências:\n{context}\n\nResposta:"
    )
    result = generator(prompt, max_new_tokens=180, do_sample=False)[0]["generated_text"]
    return result.split("Resposta:", 1)[-1].strip()
