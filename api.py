from fastapi import FastAPI
from pydantic import BaseModel

from rag.search_phone import get_phone
from rag.rag_chatbot import chatbot
from rag.compare_phone import compare_phones

app = FastAPI()


class Question(BaseModel):
    question: str

class CompareRequest(BaseModel):
    phone1: str
    phone2: str

@app.get("/")
def home():
    return {"message": "Samsung Phone Query API Running"}


@app.get("/phone/{phone_name}")
def phone_details(phone_name: str):

    phone = get_phone(phone_name)

    if phone:
        return phone

    return {"error": "Phone not found"}


@app.post("/ask")
def ask_question(data: Question):

    answer = chatbot(data.question)

    return {
        "question": data.question,
        "answer": answer
    }

@app.post("/compare")
def compare(data: CompareRequest):

    result = compare_phones(
        data.phone1,
        data.phone2
    )

    return {
        "comparison": result
    }