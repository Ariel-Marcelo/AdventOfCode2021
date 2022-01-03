def puzzleDay14(arr:list):
    template = 'KBKPHKHHNBCVCHPSPNHF' #Se establece la plantilla
    logs = {}
    for i in range(len(arr)):
        logs[arr[i][:2]] = arr[i][6]
    
    aList = []
    for i in template:
        aList.append(i)

    memo = {}

    def recursiveFunction(letters:str, cont, level):
        if (letters, level)  in memo:
            return memo[(letters, level)].copy()
                
        if cont == 40:
            return {logs[letters]: 1}

        temp = {}
        tempTwo = {}        
        temp = recursiveFunction(letters[0]+logs[letters], cont+1, level+1)
        tempTwo = recursiveFunction(logs[letters]+letters[1], cont+1, level+1)
        for key, value in tempTwo.items():
            if key in temp:
                temp[key] += value
            else:
                temp[key] = value
        
        if logs[letters] in temp:
            temp[logs[letters]] += 1
        else:
            temp[logs[letters]] = 1

        memo[(letters, level)] = temp.copy()
        return temp

    newDict = {}
    for i in range(1,len(aList)):
        gg = recursiveFunction(aList[i-1]+aList[i], 1, 1)

        for key, value in gg.items():
            if key in newDict:
                newDict[key] += value
            else:
                newDict[key] = value

    for k in range(len(aList)):
        if aList[k] in newDict:
            newDict[aList[k]] += 1
        else:
            newDict[aList[k]] = 1

    values = list(newDict.values())

    return max(values) - min(values)

def getListFromFile(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "AdventOfCode2021\Día 14\listaPuzzleDia14.txt"

print(puzzleDay14(getListFromFile(fileName)))