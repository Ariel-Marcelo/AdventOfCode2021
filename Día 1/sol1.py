before = None 
count = 0
with open("Día 1\ent.txt", "r") as archivo:
    for linea in archivo:
        actual = (int) (linea)
        if before is not None: # si no es el primer elemento de la lista
            if before < actual: # si el anterior es menor que el actual
                count += 1 # aumentamos el contador
        
        before = actual # actualizamos el anterior

print(count)