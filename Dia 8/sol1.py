def myPuzzle(displayList:list):
    cont = 0
    #recorremos la lista
    for i in range(len(displayList)):
        output = displayList[i].split(" | ")
        output = output[1].split(" ")
        #recorremos la salida
        for j in range(len(output)):
            if len(output[j]) == 2 or len(output[j]) == 3 or len(output[j]) == 4 or len(output[j]) == 7:
                #aumentamos el contador
                cont += 1
    return cont

def getList():
    with open("Dia 8\list.txt") as f:
        return [str(line.strip()) for line in f]



#Imprimimos el resultado
print(myPuzzle(getList()))

