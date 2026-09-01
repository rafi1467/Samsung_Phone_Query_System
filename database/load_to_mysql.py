import pandas as pd
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="samsung_phone_db"
)

cursor = conn.cursor()

df = pd.read_csv("data/samsung_phones.csv")

for _, row in df.iterrows():

    sql = """
    INSERT INTO phones
    (
        name,
        display_size,
        chipset,
        storage,
        battery,
        charging
    )
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (
        row["name"],
        row["display_size"],
        row["chipset"],
        row["storage"],
        row["battery"],
        row["charging"]
    )

    cursor.execute(sql, values)

conn.commit()

print("Data Inserted Successfully")

cursor.close()
conn.close()