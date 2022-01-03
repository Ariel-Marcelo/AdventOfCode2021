"""
Created on Mon Jan  2 10:02:57 2022

@author: Jefferson
"""


def mypuzzle(route:list):
    input = {"(","[","<","{"}
    aux = {")":"(","]":"[",">":"<","}":"{"}  
    score = {"}":1197,")":3,"]":57,">":25137}
    total = 0
    myStack = []
    for i in range(len(route)):
        for j in range(len(route[i])):
            if route[i][j] in input:
                myStack.append(route[i][j])
            else:    
                if len(myStack) == 0:
                    total += score[route[i][j]]
                    break
    
                elif myStack[-1] == aux[route[i][j]]:
                    myStack.pop() 
                else:
                    total += score[route[i][j]]
                    break

        myStack = []
    return total

   
  
def getList():
    with open("Day10\day10_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

# def getList():
#     with open("Day10\\test.txt") as f:
#         return [str(line.strip()) for line in f]


print(mypuzzle(getList()))