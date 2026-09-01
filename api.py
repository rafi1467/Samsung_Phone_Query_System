from fastapi import FastAPI
from rag.search_phone import get_phone

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Samsung Phone Query API Running"}


@app.get("/phone/{phone_name}")
def phone_details(phone_name: str):

    phone = get_phone(phone_name)

    if phone:
        return phone

    return {"error": "Phone not found"}


@app.get("/review/{phone_name}")
def generate_review(phone_name: str):

    phone = get_phone(phone_name)

    if not phone:
        return {"error": "Phone not found"}

    review = f"""
Samsung Phone Review

Model: {phone['name']}

Display:
{phone['display_size']}

Performance:
Powered by {phone['chipset']} which delivers strong performance for daily use, multitasking, and gaming.

Storage:
{phone['storage']}

Battery:
{phone['battery']}

Charging:
{phone['charging']}

Overall Verdict:
{phone['name']} is a premium Samsung smartphone with excellent display quality,
strong performance, good battery life, and fast charging capabilities.
"""

    return {
        "phone": phone["name"],
        "review": review
    }