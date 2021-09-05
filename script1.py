import csv
import pandas as pd
import mysql.connector as msql
from mysql.connector import Error

readFile = pd.read_csv("medicene.tsv", delimiter="\t")
readFile = readFile.fillna(0)
readFile.head()
print(readFile)

try:
    conn = msql.connect(host="localhost", database="medicene", user="root",  password="password")

    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

        cursor.execute(
            "CREATE TABLE tad(Reg varchar(255),Brand varchar(255),Ingrediants varchar(255),Dosage_Form varchar(255),Packing varchar(255),Trade_Price float,Retail_Price float);")

        for i, row in readFile.iterrows():

            sql = "INSERT INTO medicene.tad VALUES (%s,%s,%s,%s,%s,%s,%s);"
            cursor.execute(sql, tuple(row))
            print('records inserted')
            conn.commit()



        query = "SELECT * FROM medicene.tad"
        cursor.execute(query)

        result = cursor.fetchall()



except Error as e:
    print("Error", e)

