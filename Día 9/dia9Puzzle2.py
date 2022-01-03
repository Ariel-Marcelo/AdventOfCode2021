def puzzleDay9():
    arr = getArray(getListFromFile())
    lows = []
    lowsIndex = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == 0 and j == 0:
                if arr[i][j+1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif i == 0 and j == len(arr[i])-1:
                if arr[i][j-1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif i == len(arr)-1 and j == 0:
                if arr[i][j+1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif i == len(arr)-1 and j == len(arr[i])-1:
                if arr[i][j-1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))

            elif i == 0:
                if arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif i == len(arr)-1:
                if arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif j == 0:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j+1]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            elif j == len(arr[i])-1:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j-1]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
            else:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j]:
                    lows.append(arr[i][j])
                    lowsIndex.append((i,j))
    return lowsIndex

def puzzleTwoCuencas(lowsIndex:list):
    arr = getArray(getListFromFile())
    logs = []
    def getNewLocations(position:tuple):
        i = position[0]
        j = position[1]
        if i == 0 and j == 0:
            #derecha
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))

            #abajo
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))

        elif i == 0 and j == len(arr[i])-1:
            #izquierda
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
                
            #abajo
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
                
        elif i == len(arr)-1 and j == 0:
            #derecha
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
                
            #arriba
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

        elif i == len(arr)-1 and j == len(arr[i])-1:
            #izquierda
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))

            #arriba
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

        elif i == 0:
            #derecha
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
            #abajo
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
            #izquierda
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
        
        elif i == len(arr)-1:
            #derecha
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
            #arriba
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))
            #izquierda
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
        
        elif j == 0:
            #abajo
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
            #derecha
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
            #arriba
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

        elif j == len(arr[i])-1:
            #abajo
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
            #izquierda
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
            #arriba
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

        else:
            #derecha
            if arr[i][j+1]>arr[i][j] and arr[i][j+1] != 9:
                if (i,j+1) not in logs:
                    logs.append((i,j+1))
                    getNewLocations((i,j+1))
            #down
            if arr[i+1][j]>arr[i][j] and arr[i+1][j] != 9:
                if (i+1,j) not in logs:
                    logs.append((i+1,j))
                    getNewLocations((i+1,j))
            #izquierda
            if arr[i][j-1]>arr[i][j] and arr[i][j-1] != 9:
                if (i,j-1) not in logs:
                    logs.append((i,j-1))
                    getNewLocations((i,j-1))
            #arriba
            if arr[i-1][j]>arr[i][j] and arr[i-1][j] != 9:
                if (i-1,j) not in logs:
                    logs.append((i-1,j))
                    getNewLocations((i-1,j))

    lenBasins = []
    for i in range(len(lowsIndex)):
        
        getNewLocations(lowsIndex[i])
        lenBasins.append(len(logs)+1)
        logs = []
    
    lenBasins.sort()
    return lenBasins[-1] * lenBasins[-2] * lenBasins[-3]
   



def getListFromFile():
    with open("AdventOfCode2021\Día 9\listaPuzzleDia9.txt") as f:
        return [str(line.strip()) for line in f]

def getArray(arr:list):
    newArr = []
    for i in range(len(arr)):
        aux = [int(x) for x in arr[i]]
        newArr.append(aux)
    return newArr

print(puzzleTwoCuencas(puzzleDay9()))