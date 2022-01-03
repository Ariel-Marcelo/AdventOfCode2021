def mypuzzle(arr:list):
    newArr = []
    maxI = 0
    maxJ = 0
    total = 0
    
    #recorremos el arreglo y guardamos valores
    for i in range(len(arr)):
        aux = arr[i].split(',')
        newArr.append((int(aux[0]), int(aux[1])))
        maxI = max(maxI, newArr[i][0])
        maxJ = max(maxJ, newArr[i][1])
    
    #aniadimos a matriz
    mymatrix = []
    for i in range(maxJ+1):
        mymatrix.append([0]*(maxI+1))
    
    for i in range(len(newArr)):
        mymatrix[newArr[i][1]][newArr[i][0]] = 1
    

    instructions = ["x=655", 
                    "y=447", 
                    "x=327", 
                    "y=223", 
                    "x=163", 
                    "y=111",  
                    "x=81", 
                    "y=55", 
                    "x=40", 
                    "y=27", 
                    "y=13", 
                    "y=6"]

    for bucle in range(1):
        #comparamos 
        if instructions[bucle][0] == 'x':
            contX = 0
            contY = int(instructions[bucle][2:])-1
            for i in range(len(mymatrix)):
                contY = int(instructions[bucle][2:])-1
                for j in range(int(instructions[bucle][2:])+1,len(mymatrix[i])):
                    if contY >= 0:
                        if mymatrix[i][j] == 1:
                            mymatrix[contX][contY] = 1

                    contY -= 1
                contX += 1

        else:
            contX =  int(instructions[bucle][2:])-1
            contY = 0
            for i in range(int(instructions[bucle][2:])+1,len(mymatrix)):
                contY = 0
                for j in range(len(mymatrix[i])):
                    if mymatrix[i][j] == 1:
                        mymatrix[contX][contY] = 1

                    contY += 1
                contX -= 1
        auxArr = []

        if instructions[bucle][0] == 'x':
            for i in range(len(mymatrix)):
                auxArr.append(mymatrix[i][:int(instructions[bucle][2:])])
        else:
            for i in range(0, int(instructions[bucle][2:])):
                auxArr.append(mymatrix[i])
        mymatrix = auxArr

    for i in range(len(mymatrix)):
        total += mymatrix[i].count(1)
    
    #retornamos la respuesta
    return total

def getList():
    with open("Dia 13\list.txt") as f:
        return [str(line.strip()) for line in f]

#imprimimos la respuesta
print(mypuzzle(getList()))