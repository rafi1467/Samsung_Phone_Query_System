from rag.rag_chatbot import chatbot

while True:

    question = input("Ask: ")

    if question.lower() == "exit":
        break

    answer = chatbot(question)

    print("\n" + answer + "\n")