import requests
import csv
from bs4 import BeautifulSoup
import pandas as pd

def exchangeCSV():
    URL = 'http://ftp.nasdaqtrader.com/dynamic/SymDir/nasdaqlisted.txt'
    r = requests.get(URL)
    soup = BeautifulSoup(r.content, 'html.parser')
    newSoup = soup.prettify()
    #Wrote to txt then to csv because str to csv is hard
    textFile = open("temp.txt", "w", encoding='utf-')
    textFile.write(newSoup)
    textFile.close()

    file = pd.read_csv("temp.txt", delimiter="|")
    #Creates a list of the stock symbols
    '''
    symbols = file.Symbol.tolist()
    print(symbols)
    '''
    file.to_csv("nasdaq.csv")


#creates a list with the csvfile column
def symbolList():
    with open("nasdaq.csv", "r") as file:
        data = pd.read_csv('nasdaq.csv')
        symbols = data.Symbol.tolist()
        file.close()
        return symbols
symbolList()
