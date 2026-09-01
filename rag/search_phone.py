from rag.db import get_connection

def get_phone(phone_name):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT *
    FROM phones
    WHERE name LIKE %s
    """

    cursor.execute(query, (f"%{phone_name}%",))
    result = cursor.fetchone()

    conn.close()

    return result


# phone = get_phone("S24")
# print(phone)