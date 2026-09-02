from rag.rag_chatbot import chatbot

while True:

    q = input("Ask: ")

    if q == "exit":
        break

    print()
    print(chatbot(q))
    print()