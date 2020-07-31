import mysql.connector
import csv
from config import *


def insertDB(symbol):
    # Connect to SQL Server
    conn = mysql.connector.connect(user=user, password=password, host=host, database='HistoricalStock')
    cursor = conn.cursor()

    # Create Table
    cursor.execute("CREATE TABLE {}(time date, open float, high float, low float, close float, volume int);".format(symbol))

    # Insert Data into Table
    with open('file.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row:
                cursor.execute("INSERT INTO {}(time,open,high,low,close,volume) VALUES({},{},{},{},{},{});".format(symbol,"'" + row[0] + "'",row[1],row[2],row[3],row[4],row[5]))
    conn.commit()


# Jacks Personal IP - 50.81.227.140
