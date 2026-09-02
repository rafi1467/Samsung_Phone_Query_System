from fastapi import FastAPI

from models.request_models import QuestionRequest
from models.compare_request import CompareRequest

from rag.rag_chatbot import chatbot
from rag.compare import compare_phones

app = FastAPI(
    title="Samsung Phone Query API"
)


@app.get("/")
def home():

    return {
        "message": "Samsung Phone Query API Running"
    }


@app.post("/ask")
def ask_question(request: QuestionRequest):

    answer = chatbot(request.question)

    return {
        "question": request.question,
        "answer": answer
    }


@app.post("/compare")
def compare(request: CompareRequest):

    result = compare_phones(
        request.phone1,
        request.phone2
    )

    return {
        "phone1": request.phone1,
        "phone2": request.phone2,
        "comparison": result
    }