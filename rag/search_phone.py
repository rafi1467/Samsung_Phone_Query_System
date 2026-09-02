from rag.db import get_connection


def get_phone(phone_name):

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    sql = """
    SELECT *
    FROM phones
    WHERE LOWER(name)=LOWER(%s)
    LIMIT 1
    """

    cursor.execute(sql, (phone_name,))
    phone = cursor.fetchone()

    cursor.close()
    conn.close()

    return phone


def get_all_phone_names():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT name FROM phones")

    phones = cursor.fetchall()

    cursor.close()
    conn.close()

    return [p["name"] for p in phones]


def get_all_phones():

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM phones")

    phones = cursor.fetchall()

    cursor.close()
    conn.close()

    return phones