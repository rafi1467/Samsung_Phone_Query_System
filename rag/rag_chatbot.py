from rapidfuzz import process

from rag.search_phone import (
    get_phone,
    get_all_phone_names
)

from rag.llm import ask_llm


def chatbot(question):

    question_lower = question.lower()

    phone = None

    all_phones = get_all_phone_names()

    # Exact and Alias Matching
    for p in all_phones:

        aliases = [
            p.lower(),
            p.lower().replace("samsung ", ""),
            p.lower().replace("samsung galaxy ", "")
        ]

        for alias in aliases:

            if alias in question_lower:

                phone = get_phone(p)
                break

        if phone:
            break

    # Fallback Fuzzy Matching
    if not phone:

        best_match = process.extractOne(
            question,
            all_phones
        )

        if best_match and best_match[1] > 70:

            phone = get_phone(best_match[0])

    if not phone:
        return "Phone not found in database."

    print(f"Matched Phone: {phone['name']}")

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
    You are a Samsung phone assistant.

    Answer ONLY using the information provided below.

    Phone Information:
    {context}

    User Question:
    {question}
    """

    return ask_llm(prompt)