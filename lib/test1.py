fileName = "text_1_var_12"
allWords = dict()

with open("assets/data/1/"+fileName, "r") as file:
    allLines = file.readlines()
    for line in allLines:
        allWordsInARow = line.strip().replace(","," ").replace("."," ").replace("?"," ").replace("!"," ").strip().split(" ")
        for wordInARow in allWordsInARow:
            if(wordInARow in allWords):
                allWords[wordInARow] += 1
            else:
                allWords[wordInARow] = 1
    allWords = dict(sorted(allWords.items(), reverse=True))
    
with open("assets/result/1/"+fileName+"_result", "w") as result:
    for key, value in allWords.items():
        result.write(key + " : " + str(value) + "\n")