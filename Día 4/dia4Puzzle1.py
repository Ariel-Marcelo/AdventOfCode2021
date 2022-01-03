def filterInformation(list):
    bingo = []
    aux = []
    for i in range(len(list)): #Se recorre el arreglo para filtrar la informacion
        if list[i] =="":
            bingo.append(aux)
            aux = []
        else:
            separation = list[i].split(" ") #se separa el arreglo
            aux2 = []
            for k in range(len(separation)):
                if separation[k] != "":
                    aux2.append(int(separation[k]))
            aux.append(aux2)
    bingo.append(aux)
    return bingo

def checkBing(bingo, eliminated):
    #Se inspeccionan las filas
    for i in range(len(bingo)):
        if i in eliminated:
            continue
        for j in range(len(bingo[i])):
            if bingo[i][j].count(-1) == 5:
                return i
    #Se inspeccionan las columnas
    for i in range(len(bingo)):
        if i in eliminated:
            continue
        for j in range(5):
            if bingo[i][0][j] == -1 and bingo[i][1][j] == -1 and bingo[i][2][j] == -1 and bingo[i][3][j] == -1 and bingo[i][4][j] == -1:
                return i
    return -1

def changeBingo(bingo, num, eliminated):
    for i in range(len(bingo)):
        if i in eliminated:
            continue
        for j in range(len(bingo[i])):
            for k in range(len(bingo[i][j])):
                if bingo[i][j][k] == num:
                    bingo[i][j][k] = -1

def sumOthers(myWinner:list):
    sum = 0
    for i in range(len(myWinner)):
        for j in range(len(myWinner[i])):
            if myWinner[i][j] != -1:
                sum += myWinner[i][j]
    return sum  

def puzzleDay4():
    nums = [59,91,13,82,8,32,74,96,55,51,19,47,46,44,5,21,95,71,48,60,68,81,80,14,23,28,26,78,12,22,49,1,83,88,39,53,84,37,93,24,42,7,56,20,92,90,25,36,34,52,27,50,85,75,89,63,33,4,66,17,98,57,3,9,54,0,94,29,79,61,45,86,16,30,77,76,6,38,70,62,72,43,69,35,18,97,73,41,40,64,67,31,58,11,15,87,65,2,10,99]
    bingo = filterInformation(getListFromFile())
    eliminated = set()

    for i in range(len(nums)):
        changeBingo(bingo, nums[i], eliminated)
        index = checkBing(bingo, eliminated)
        if index != -1:
            return nums[i] * sumOthers(bingo[index])


def getListFromFile():
    with open("AdventOfCode2021\Día 4\listaPuzzleDia4.txt") as f:
        return [str(line.strip()) for line in f]

#Se imprime el resultado
print(puzzleDay4())