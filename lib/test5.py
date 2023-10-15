# Need to install first (if some packages have not been installed previously)
# >> python3 -m pip install beautifulsoup4
# or
# >> pip install beautifulsoup4
# 
# >> python3 -m pip install lxml
# or
# >> pip install lxml

from bs4 import BeautifulSoup
import csv

try:
    fileName = "text_5_var_12"
    with open("assets/data/5/"+fileName, encoding="utf-8", mode="r") as htmlFile:
        reader = htmlFile.read()
        htmlParse = BeautifulSoup(reader, 'lxml') 
        tableBody = htmlParse.find('table')
        tableRows = tableBody.find_all('tr')
        allData = []

        for row in tableRows:
            tableCols = row.find_all('td') or row.find_all('th')
            data = (tableCols[0].text, tableCols[1].text, tableCols[2].text, tableCols[3].text, tableCols[4].text)
            allData.append(data)
        
        with open("assets/result/5/"+fileName+"_result.csv", 'w', newline='') as csvfile:
            writerCsv = csv.writer(csvfile, delimiter=',')
            for data in allData:
                writerCsv.writerow([data[0]] + [str(data[1])] + [data[2]] + [data[3]] +  [data[4]])
        
except Exception as e:
    print(e)