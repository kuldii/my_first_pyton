fileName = "text_2_var_12"
allSumNumbers = []

with open("assets/data/2/"+fileName, "r") as file:
    allLines = file.readlines()
    for line in allLines:
        sum = 0
        allNumbersInARow = line.strip().split(";")
        for numberInARow in allNumbersInARow:
            sum += int(numberInARow)
        allSumNumbers.append(sum)
    
with open("assets/result/2/"+fileName+"_result", "w") as result:
    for value in allSumNumbers:
        result.write(str(value) + "\n")