from rag.compare import compare_phones

phone1 = input("First Phone: ")
phone2 = input("Second Phone: ")

result = compare_phones(
    phone1,
    phone2
)

print("\n")
print(result)