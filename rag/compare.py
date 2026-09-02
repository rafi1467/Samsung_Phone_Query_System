from rag.search_phone import get_phone
from rag.llm import ask_llm


def compare_phones(phone1_name, phone2_name):

    phone1 = get_phone(phone1_name)
    phone2 = get_phone(phone2_name)

    if not phone1:
        return f"{phone1_name} not found."

    if not phone2:
        return f"{phone2_name} not found."

    context = f"""
Phone 1
Name: {phone1['name']}
Display: {phone1['display_size']}
Chipset: {phone1['chipset']}
Storage: {phone1['storage']}
Battery: {phone1['battery']}
Charging: {phone1['charging']}
Camera: {phone1['camera']}
Price: {phone1['price']}

Phone 2
Name: {phone2['name']}
Display: {phone2['display_size']}
Chipset: {phone2['chipset']}
Storage: {phone2['storage']}
Battery: {phone2['battery']}
Charging: {phone2['charging']}
Camera: {phone2['camera']}
Price: {phone2['price']}
"""

    prompt = f"""
You are a Samsung phone comparison assistant.

Compare these two phones.

Mention:

1. Display
2. Performance
3. Camera
4. Battery
5. Price
6. Which phone is better overall

Use only the information below.

{context}
"""

    return ask_llm(prompt)