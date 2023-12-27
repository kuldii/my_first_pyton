import math  

fileName = "text_3_var_12"
varian = 12
allNumbers = []

with open("assets/data/3/"+fileName, "r") as file:
    allLines = file.readlines()
    for line in allLines:
        allNumbersInARow = line.strip().split(",")
        for i in range(len(allNumbersInARow)):
            if(str(allNumbersInARow[i]).lower() == "na" and str(allNumbersInARow[i-1]).lower() != "na" and str(allNumbersInARow[i+1]).lower() != "na"):
                allNumbersInARow[i] = (float(allNumbersInARow[i-1]) + float(allNumbersInARow[i+1])) / 2
            if(math.sqrt(float(allNumbersInARow[i])) >= (50+varian)):
                allNumbers.append(allNumbersInARow[i])
        
with open("assets/result/3/"+fileName+"_result", "w") as result:
    for value in allNumbers:
        result.write(str(value) + "\n")