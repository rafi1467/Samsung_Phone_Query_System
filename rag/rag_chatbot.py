from rapidfuzz import process

from rag.search_phone import (
    get_phone,
    get_all_phone_names
)

from rag.smart_queries import (
    get_cheapest_phone,
    get_best_battery_phone
)

from rag.llm import ask_llm


def chatbot(question):

    q = question.lower()

    # Smart Queries

    if "cheapest" in q or "lowest price" in q:

        return get_cheapest_phone()

    if "best battery" in q or "battery life" in q:

        return get_best_battery_phone()

    phone = None

    all_phones = get_all_phone_names()

    # Alias Matching

    for p in all_phones:

        aliases = [
            p.lower(),
            p.lower().replace("samsung ", ""),
            p.lower().replace("samsung galaxy ", "")
        ]

        for alias in aliases:

            if alias in q:

                phone = get_phone(p)
                break

        if phone:
            break

    # Fuzzy Matching

    if not phone:

        best_match = process.extractOne(
            question,
            all_phones
        )

        if best_match and best_match[1] > 70:

            phone = get_phone(best_match[0])

    if not phone:
        return "Phone not found in database."

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

Answer only using the information below.

Phone Information:

{context}

Question:
{question}
"""

    return ask_llm(prompt)