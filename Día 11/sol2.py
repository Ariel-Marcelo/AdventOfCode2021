def sol(arr:list):
    newArr = []
    used = set()
    for i in range(len(arr)): # Guardar enteros en newArr
        aux = [int(x) for x in arr[i]]
        newArr.append(aux)
    
    def analisis(i,j):
        #Caso Base
        if (i,j) not in used: # Si no está entre los usados
            if newArr[i][j] < 9: # Si es menor que 9
                newArr[i][j] += 1 # Sumar 1
                return
        
        #recursive case
        if (i,j) not in used: # seguramente es 9
            used.add((i,j)) # Agregar a usados
            newArr[i][j] = 0 # Darle el valor de 0
            #llamar al análisis para todos los vecinos, incluidos los adyacentes 
            if i > 0: # fila superior
                analisis(i-1,j)
            if j > 0: # columna izquierda
                analisis(i,j-1)
            if i < len(newArr)-1: # fila inferior
                analisis(i+1,j)
            if j < len(newArr[0])-1: # columna derecha
                analisis(i,j+1)
            #análisis de llamadas para los adyacentes
            if i > 0 and j > 0:
                analisis(i-1,j-1)
            if i > 0 and j < len(newArr[0])-1:
                analisis(i-1,j+1)
            if i < len(newArr)-1 and j > 0:
                analisis(i+1,j-1)
            if i < len(newArr)-1 and j < len(newArr[0])-1:
                analisis(i+1,j+1)

    for buc in range(1000000): # solo es un número muy alto, para q continue el bucle
        used = set()    
        for i in range(len(newArr)): # para cada fila
            for j in range(len(newArr[0])): # para cada columna
                analisis(i,j) # analisis aumentará en 1 a los vecinos, adyacentes
        #print(newArr)
        if len(used) == len(newArr)*len(newArr[0]): # si todos los elementos fueron usados
            return buc+1 # retornar el número de bucles

def getEntrada():
    with open("Día 11\ent.txt") as f:
        return [str(line.strip()) for line in f]

print(sol(getEntrada()))