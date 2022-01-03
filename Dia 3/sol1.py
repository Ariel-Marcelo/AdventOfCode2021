def myPuzzleDay3(report: list):
    tam = len(report[0])
    mydict = {0:0, 1:0}
    gama = ""
    #empezamos la comparacion
    for i in range(0, tam):
        for j in range(len(report)):
            if report[j][i] == "0":
                mydict[0] += 1
            else:
                mydict[1] += 1
        if mydict[0] > mydict[1]:
            gama += "0"
        else:
            gama += "1"
        #reseteo
        mydict = {0:0, 1:0}
    
    #create epsilon
    epsilon = ""
    #recorremos gama 
    for i in gama:
        if i == "0":
            epsilon += "1"
        else:
            epsilon += "0"
    
    decGamma = int(gama, 2)
    decEpsilon = int(epsilon, 2)
    #respuesta
    return decGamma * decEpsilon

#prueba para el sistema
aux = ["00100",
        "11110",
        "10110",
        "10111",
        "10101",
        "01111",
        "00111",
        "11100",
        "10000",
        "11001",
        "00010",
        "01010"]

def getList():
    with open("Ejercicio 3\list.txt") as f:
        return [str(line.strip()) for line in f]
        
#prueba
print(myPuzzleDay3(aux))

#Imprimimos los resultados
print(myPuzzleDay3(getList()))
