from rag.search_phone import get_phone
from rag.llm import ask_llm


def compare_phones(phone1, phone2):

    p1 = get_phone(phone1)
    p2 = get_phone(phone2)

    if not p1:
        return f"{phone1} not found"

    if not p2:
        return f"{phone2} not found"

    prompt = f"""
Compare these Samsung phones.

Phone 1:
Name: {p1['name']}
Chipset: {p1['chipset']}
Display: {p1['display_size']}
Storage: {p1['storage']}
Battery: {p1['battery']}
Camera: {p1['camera']}
Price: {p1['price']}

Phone 2:
Name: {p2['name']}
Chipset: {p2['chipset']}
Display: {p2['display_size']}
Storage: {p2['storage']}
Battery: {p2['battery']}
Camera: {p2['camera']}
Price: {p2['price']}

Give a detailed comparison.
"""

    return ask_llm(prompt)