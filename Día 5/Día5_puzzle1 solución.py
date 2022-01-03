

"""
Created on Mon Jan  2 09:02:57 2022

@author: Jefferson

"""
def mypuzzleday5(lines:int):
    mydict = {}
    for lin in lines:
        aux1 = lin.split(" -> ")
        partOne = aux1[0].split(",")
        partTwo = aux1[1].split(",")
        x1 = int(partOne[0])
        y1 = int(partOne[1])
        x2 = int(partTwo[0])
        y2 = int(partTwo[1])

        if x1 == x2:
            if y1 <= y2:
                for i in range(y1, y2+1):
                    if (x1,i) not in mydict:
                        mydict[(x1,i)] = 1
                    else:
                        mydict[(x1,i)] += 1
            else:
                for i in range(y2, y1+1):
                    if (x1,i) not in mydict:
                        mydict[(x1,i)] = 1
                    else:
                        mydict[(x1,i)] += 1
        elif y1 == y2:
            if x1 <= x2:
                for i in range(x1, x2+1):
                    if (i,y1) not in mydict:
                        mydict[(i,y1)] = 1
                    else:
                        mydict[(i,y1)] += 1
            else:
                for i in range(x2, x1+1):
                    if (i,y1) not in mydict:
                        mydict[(i,y1)] = 1
                    else:
                        mydict[(i,y1)] += 1
    
    sum = 0
    for key in mydict:
        if mydict[key] >= 2:
            sum += 1
    return sum
            




def getList():
    with open("Day5\day5_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

#print the result
print(mypuzzleday5(getList()))