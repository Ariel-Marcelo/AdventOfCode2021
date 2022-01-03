def mypuzzle(arr:list):
    newArr = []
    for i in range(len(arr)):
        newArr.append([int(x) for x in arr[i]])
    
    memo = {(len(newArr)-1,len(newArr[0])-1):newArr[len(newArr)-1][len(newArr[0])-1]}
    lastI = len(newArr)-1
    lastJ = len(newArr[0])-1
    #passed = set()


    def dfs(i,j): 
        #passed.add((i,j))
        if (i,j) in memo:
            #passed.discard((i,j))

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

        if i != lastI:
            minRisk = min(minRisk,dfs(i+1,j))
        if j != lastJ:
            minRisk = min(minRisk,dfs(i,j+1))
        
            
        #passed.discard((i,j))
        memo[(i,j)] = minRisk+newArr[i][j]
        return minRisk+newArr[i][j]


    return dfs(0,0) - newArr[0][0] - 1



def getList(fileName:str):
    with open(fileName) as f:
        return [str(line.strip()) for line in f]

fileName = "Day15\day15_puzzle_list.txt"

print(mypuzzle(getList(fileName)))
