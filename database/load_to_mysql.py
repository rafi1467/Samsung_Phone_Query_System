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

df = df.fillna("")

for _, row in df.iterrows():

    sql = """
    INSERT INTO phones
    (
        name,
        display_size,
        chipset,
        storage,
        battery,
        charging, 
        camera,
        price
    )
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
    """

    values = (
    str(row["name"]),
    str(row["display_size"]),
    str(row["chipset"]),
    str(row["storage"]),
    str(row["battery"]),
    str(row["charging"]),
    str(row["camera"]),
    str(row["price"])
    )

    cursor.execute(sql, values)

conn.commit()

print("Data Inserted Successfully")

cursor.close()
conn.close()