from rag.search_phone import get_all_phones
from rag.llm import ask_llm


def best_phone(question):

    phones = get_all_phones()

    context = ""

    for p in phones:

        context += f"""
Name: {p['name']}
Battery: {p['battery']}
Camera: {p['camera']}
Price: {p['price']}
Chipset: {p['chipset']}

"""

    prompt = f"""
You are a Samsung phone expert.

Use only the information below.

Samsung Phones:

{context}

Question:
{question}
"""

    return ask_llm(prompt)