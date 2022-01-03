import numpy as np
def getExpandedArr(newArr:list):
    expArr = np.asarray(newArr)
    gg = [0, len(newArr[0]), len(newArr[0])*2, len(newArr[0])*3]
    d = 4
    for k in range(d):
        arrAux = expArr[:, gg[k]:gg[k]+len(newArr[0])].copy()
        arrTwo = arrAux.copy()
        for i in range(len(arrTwo)):
            for j in range(len(arrTwo[i])):
                if arrTwo[i][j] == 9:
                    arrTwo[i][j] = 1
                    continue
                arrTwo[i][j] = arrTwo[i][j] + 1
        #add arrTwo to arr
        expArr = np.concatenate((expArr, arrTwo), axis=1)
    
    #I must add the new rows.
    gg = [0,len(newArr),len(newArr)*2,len(newArr)*3]
    for k in range(d):
        arrAux = expArr[gg[k]:gg[k]+len(newArr), :].copy()
        arrTwo = arrAux.copy()
        for i in range(len(arrTwo)):
            for j in range(len(arrTwo[i])):
                if arrTwo[i][j] == 9:
                    arrTwo[i][j] = 1
                    continue
                arrTwo[i][j] = arrTwo[i][j] + 1
        #add arrTwo to arr
        expArr = np.concatenate((expArr, arrTwo), axis=0)
    # for m in range(len(expArr)):
    #     print(expArr[m])

    return expArr, 2*d+2

def mypuzzle(arr:list):
    newArr = []
    for i in range(len(arr)):
        newArr.append([int(x) for x in arr[i]])
    print(len(newArr), len(newArr[0]))
    newArr,d = getExpandedArr(newArr)
    memo = {(len(newArr)-1,len(newArr[0])-1):newArr[len(newArr)-1][len(newArr[0])-1]}
    lastI = len(newArr)-1
    lastJ = len(newArr[0])-1



    def dfs(i,j): 

        if (i,j) in memo:
            return memo[(i,j)]
            passed.discard((i,j))
        
        minRisk = 1000000000000000000
        # if i<lastI:
        #     if (i+1,j) not in passed:
        #         minRisk = min(minRisk,dfs(i+1,j))
        # if j<lastJ:
        #     if (i,j+1) not in passed:
        #         minRisk = min(minRisk,dfs(i,j+1))
        # if i>0:
        #     if (i-1,j) not in passed:
        #         minRisk = min(minRisk,dfs(i-1,j))
        # if j>0:
        #     if (i,j-1) not in passed:
        #         minRisk = min(minRisk,dfs(i,j-1))

        # if i != lastI and j != lastJ and i != 0 and j != 0:
        #     minRisk = min(dfs(i+1,j),dfs(i,j+1),dfs(i-1,j),dfs(i,j-1))
        # elif i == 0 and j != lastJ:
        #     minRisk = min(dfs(i,j+1),dfs(i-1,j),dfs(i,j-1))

        if i < lastI:
            minRisk = min(minRisk,dfs(i+1,j))
        if j < lastJ:
            minRisk = min(minRisk,dfs(i,j+1))
        
        memo[(i,j)] = minRisk+newArr[i][j]
        return minRisk+newArr[i][j]

    dfs(250,250)
    return dfs(0,0) - newArr[0][0] -1 - d



def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "Day15\day15_puzzle_list.txt"


print(mypuzzle(getList(fileName)))
