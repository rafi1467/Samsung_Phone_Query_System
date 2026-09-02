from rag.best_phone import best_phone

while True:

    q = input("Ask: ")

    if q.lower() == "exit":
        break

    print()
    print(best_phone(q))
    print()