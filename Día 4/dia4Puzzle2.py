def filterInformation(arr:list):
    bingoList = []
    aux = []
    for i in range(len(arr)):
        if arr[i] =="":
            bingoList.append(aux)
            aux = []
        else:
            sepp = arr[i].split(" ")
            aux2 = []
            for k in range(len(sepp)):
                if sepp[k] != "":
                    aux2.append(int(sepp[k]))
            aux.append(aux2)
    bingoList.append(aux)
    return bingoList

def checkBing(bingoList:list, eliminated:set):
    #Se chequean las filas
    for i in range(len(bingoList)):
        if i in eliminated:
            continue
        for j in range(len(bingoList[i])):
            if bingoList[i][j].count(-1) == 5:
                return i
    #Se chequean las columnas
    for i in range(len(bingoList)):
        if i in eliminated:
            continue
        for j in range(5):
            if bingoList[i][0][j] == -1 and bingoList[i][1][j] == -1 and bingoList[i][2][j] == -1 and bingoList[i][3][j] == -1 and bingoList[i][4][j] == -1:
                return i
    return -1

def changeBingo(bingoList:list, num:int, eliminated:set):
    for i in range(len(bingoList)):
        if i in eliminated:
            continue
        for j in range(len(bingoList[i])):
            for k in range(len(bingoList[i][j])):
                if bingoList[i][j][k] == num:
                    bingoList[i][j][k] = -1

def sumOthers(myWinner:list):
    sum = 0
    for i in range(len(myWinner)):
        for j in range(len(myWinner[i])):
            if myWinner[i][j] != -1:
                sum += myWinner[i][j]
    return sum  

def puzzleDay4():
    nums = [59,91,13,82,8,32,74,96,55,51,19,47,46,44,5,21,95,71,48,60,68,81,80,14,23,28,26,78,12,22,49,1,83,88,39,53,84,37,93,24,42,7,56,20,92,90,25,36,34,52,27,50,85,75,89,63,33,4,66,17,98,57,3,9,54,0,94,29,79,61,45,86,16,30,77,76,6,38,70,62,72,43,69,35,18,97,73,41,40,64,67,31,58,11,15,87,65,2,10,99]
    bingoList = filterInformation(getListFromFile())
    totalInd = {int(x) for x in range(len(bingoList))}
    eliminated = set()


    for i in range(len(nums)):
        if len(eliminated) < len(totalInd)-1:
            changeBingo(bingoList, nums[i], eliminated)
            index = checkBing(bingoList, eliminated)
            while index != -1:
                eliminated.add(index)
                changeBingo(bingoList, nums[i], eliminated)
                index = checkBing(bingoList, eliminated)


        else:
            changeBingo(bingoList, nums[i], eliminated)
            fin = totalInd - eliminated
            suma = sumOthers(bingoList[list(fin)[0]])
            return suma * nums[i]

    print(eliminated)
    print(totalInd - eliminated)
    print(len(bingoList))
    print(len(nums))
    
        


def getListFromFile():
    with open("AdventOfCode2021\Día 4\listaPuzzleDia4.txt") as f:
        return [str(line.strip()) for line in f]

#Se imprime el resultado
print(puzzleDay4())

