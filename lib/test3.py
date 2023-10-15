import math  

try:
    fileName = "text_3_var_12"
    allNumbers = []
    
    with open("assets/data/3/"+fileName, "r") as file:
        allLines = file.readlines()

        for line in allLines:
            allNumbersInARow = line.strip().split(",")
            for indexNumberInARow in range(len(allNumbersInARow)):
                if(str(allNumbersInARow[indexNumberInARow]).lower() == "na"):
                    allNumbersInARow[indexNumberInARow] = float(allNumbersInARow[indexNumberInARow-1]) + float(allNumbersInARow[indexNumberInARow+1]) / 2
                if(math.sqrt(float(allNumbersInARow[indexNumberInARow])) > 50):
                    allNumbers.append(allNumbersInARow[indexNumberInARow])
            
    with open("assets/result/3/"+fileName+"_result", "w") as result:
        for value in allNumbers:
            result.write(str(value) + "\n")
        
except Exception as e:
    print(e)