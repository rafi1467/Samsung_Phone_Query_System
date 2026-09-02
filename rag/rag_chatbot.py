from rag.search_phone import get_phone
from rag.llm import ask_llm


def chatbot(question):

    question_lower = question.lower()

    if "s24" in question_lower:
        phone = get_phone("S24")

    elif "s23" in question_lower:
        phone = get_phone("S23")

    elif "s22" in question_lower:
        phone = get_phone("S22")

    else:
        return "Phone not found"

    context = f"""
    Name: {phone['name']}
    Display: {phone['display_size']}
    Chipset: {phone['chipset']}
    Storage: {phone['storage']}
    Battery: {phone['battery']}
    Charging: {phone['charging']}
    Camera: {phone['camera']}
    Price: {phone['price']}
    """

    prompt = f"""
    Answer only using the phone information below.

    Phone Information:
    {context}

    User Question:
    {question}
    """

    return ask_llm(prompt)