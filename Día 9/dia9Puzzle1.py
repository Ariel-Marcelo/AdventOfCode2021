def myPuzzle():
    arr = getArr(getList())
    lows = []

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == 0 and j == 0:
                if arr[i][j+1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
            elif i == 0 and j == len(arr[i])-1:
                if arr[i][j-1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
            elif i == len(arr)-1 and j == 0:
                if arr[i][j+1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])
            elif i == len(arr)-1 and j == len(arr[i])-1:
                if arr[i][j-1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])

            elif i == 0:
                if arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j] and arr[i+1][j]>arr[i][j]:
                    lows.append(arr[i][j])
            elif i == len(arr)-1:
                if arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j] and arr[i-1][j]>arr[i][j]:
                    lows.append(arr[i][j])
            elif j == 0:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j+1]>arr[i][j]:
                    lows.append(arr[i][j])
            elif j == len(arr[i])-1:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j-1]>arr[i][j]:
                    lows.append(arr[i][j])
            else:
                if arr[i-1][j]>arr[i][j] and arr[i+1][j]>arr[i][j] and arr[i][j-1]>arr[i][j] and arr[i][j+1]>arr[i][j]:
                    lows.append(arr[i][j])
    
    return sum(lows) + len(lows)




def getList():
    with open("AdventOfCode2021\Día 9\listaPuzzleDia9.txt") as f:
        return [str(line.strip()) for line in f]

def getArr(arr:list):
    newArr = []
    for i in range(len(arr)):
        aux = [int(x) for x in arr[i]]
        newArr.append(aux)
    return newArr


#Print solution
print(myPuzzle())