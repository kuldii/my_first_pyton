import csv

fileName = "text_4_var_12"
varian = 12
allData = []

with open("assets/data/4/"+fileName, newline='') as csvfile:
    readerCsv = csv.reader(csvfile, delimiter=',')
    
    totalIncome = 0
    avgIncome = 0.0
    
    for dataInARow in readerCsv:
        del dataInARow[5]
        totalIncome += int(dataInARow[4].strip().replace("₽", ""))
        allData.append(dataInARow)
    
    avgIncome = totalIncome / len(allData)
    
    filteredAllData = []

    for indexData in range(len(allData)):
        if(int(allData[indexData][4].strip().replace("₽", "")) >= avgIncome and int(allData[indexData][3]) > (25 + (varian%10))):
            filteredAllData.append((int(allData[indexData][0]),allData[indexData][1] + " " + allData[indexData][2], int(allData[indexData][3]),allData[indexData][4]))
    
    allData = sorted(filteredAllData, key=lambda person: person[0], reverse=False)

with open("assets/result/4/"+fileName+"_result.csv", 'w', newline='') as csvfile:
    writerCsv = csv.writer(csvfile, delimiter=',')
    writerCsv.writerow(['id'] + ['name'] + ['age'] + ['salary'])
    for data in allData:
        writerCsv.writerow([data[0]] + [str(data[1])] + [data[2]] + [data[3]])