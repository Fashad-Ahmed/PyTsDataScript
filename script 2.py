import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

readFile = pd.read_csv("medicene.tsv", delimiter="\t")

try:
    conn = msql.connect(host="localhost", database="medicene", user="root",  password="password")

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        # query = "ALTER TABLE tad ADD Difference float ;"
        # cursor.execute(query)
        # result = cursor.fetchall()
        # print(result)

        for i in readFile['Retail Price']:
            for j in readFile['Trade Price']:
                wap = i - j
                wap = str(wap)
                print(wap)
                sql = "INSERT(Difference) VALUES(" + wap + ");"
                cursor.execute(sql)
                result = cursor.fetchall()
                cursor.commit()
                print(result)
except Error as e:
    print("Error", e)
