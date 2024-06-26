import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def getFinancialInformation(symbol):
    try:
        url=f"https://finance.yahoo.com/quote/{symbol}?p={symbol}"

        response = requests.get(url=url)
        txtRes = response.text
        soup = BeautifulSoup(txtRes, features="html.parser")
        startName = "Previous Close"
        finalName = "1y Target Est"
        trs = soup.find_all("li")
        flag = False

        names = []
        values = []
        namVal = {}

        for i in range(len(trs)):        
            if trs[i].contents[0].text == startName:
                flag = True

            if flag == True:
                    
                for j in range(len(trs[i].contents)):
                    
                    if j == 0:
                        try: 
                            name = trs[i].contents[j].text
                            names.append(name)
                        except:
                            continue 

                    if j == 2:
                        try: 
                            value = trs[i].contents[j].text
                            values.append(value)
                        except:
                            continue 

                namVal[name] = value
                if name == finalName:
                    flag = False
                    break 

    except:
        pass

    return names,values


def getCompanyList():
    wikiURL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    r = requests.get(wikiURL)
    pageText = r.text
    soup = BeautifulSoup(pageText, features="html.parser")

    tickerSymbols = []
    tbody = soup.find_all("tbody")

    for i in range(len(tbody[0].contents)):
        if i<2:
            continue
        if i%2:
            continue

        symbol = tbody[0].contents[i].contents[1].text
        tickerSymbols.append(symbol.strip("\n"))
        if len(tickerSymbols)==500:
            break
    return tickerSymbols



data = {"symbol":[],
        "metric":[],
        "value":[]}

tickerSymbols = getCompanyList()
for symbol in tickerSymbols:
    names,values = getFinancialInformation(symbol)

    for i in range(len(names)):
            try:
                data["symbol"].append(symbol)
                data["metric"].append(names[i])
                data["value"].append(values[i])
            except:
                continue


df = pd.DataFrame(data)
FILE_PATH="FinancialData.csv"
if os.path.isfile(FILE_PATH):
    df.to_csv(FILE_PATH, mode="a", header=False, columns=["symbol", "metric", "value"])
else:
    df.to_csv(FILE_PATH, columns=["symbol", "metric", "value"])