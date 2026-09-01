from rag.search_phone import get_phone

question = input("Ask: ")

phone_name = input("Phone Model (e.g. S24, S23, S22): ")

phone = get_phone(phone_name)

if phone:

    answer = f"""
Phone Name: {phone['name']}

Display: {phone['display_size']}

Chipset: {phone['chipset']}

Storage: {phone['storage']}

Battery: {phone['battery']}

Charging: {phone['charging']}
"""

    print(answer)

else:
    print("Phone not found")