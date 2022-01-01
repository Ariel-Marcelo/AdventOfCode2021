def sol(scanning:list):
    cont = 0
    for i in range(3,len(scanning)): # empieze desde el tercer elemento
        if scanning[i] > scanning[i-3]: # siempre comparamos de 3 en 3
            cont+=1
    return cont

def getList(): # retorne una lista con todos los elementos de la entrada
    with open("Ejercicio 1\ent2.txt") as f:
        return [int(line.strip()) for line in f]

#Print solution
print(sol(getList()))