import requests
from bs4 import BeautifulSoup

try:
    url="https://finance.yahoo.com/quote/AAPL?p=AAPL"

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

    #print(names)
    #print(values)
    print(namVal)

except:
    pass