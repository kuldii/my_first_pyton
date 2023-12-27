from bs4 import BeautifulSoup
import csv

fileName = "text_5_var_12"
allData = []

with open("assets/data/5/"+fileName, encoding="utf-8", mode="r") as htmlFile:
    reader = htmlFile.read()
    htmlParse = BeautifulSoup(reader, 'lxml') 
    tableRows = htmlParse.find_all('tr')

    for row in tableRows:
        tableCols = row.find_all('td') or row.find_all('th')
        allData.append([data.text for data in tableCols])
    
with open("assets/result/5/"+fileName+"_result.csv", 'w', newline='') as csvfile:
    writerCsv = csv.writer(csvfile, delimiter=',')
    writerCsv.writerows(allData)