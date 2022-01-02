def sol(scanning:list):
    cont = 0
    for i in range(3,len(scanning)): # empieze desde el tercer elemento
        if scanning[i] > scanning[i-3]: # siempre comparamos de 3 en 3
            cont+=1
    return cont

def getList(): # retorne una lista con todos los elementos de la entrada
    with open("Día 2\ent.txt") as archivo:
        return [int(line.strip()) for line in archivo]

#Print solution
print(sol(getList()))