def puzzleDay14(arr:list):
    template = 'KBKPHKHHNBCVCHPSPNHF' #Se establece la plantilla
    logs = {}
    for i in range(len(arr)):
        logs[arr[i][:2]] = arr[i][6]
    
    aList = []
    for i in template:
        aList.append(i)


    for i in range(10):
        indAux = 1
        aux = aList.copy()
        for j in range(1,len(aList)):
            aux.insert(indAux,logs[aList[j-1]+aList[j]])
            indAux += 2
        aList = aux

    dictionary = {}
    for i in aList:
        if i in dictionary:
            dictionary[i] += 1
        else:
            dictionary[i] = 1

    values = list(dictionary.values()) 
    return max(values) - min(values)
    

def getListFromFile(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "AdventOfCode2021\Día 14\listaPuzzleDia14.txt"

print(puzzleDay14(getListFromFile(fileName)))