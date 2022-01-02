before = None 
count = 0
with open("Día 1\ent.txt", "r") as archivo:
    for linea in archivo:
        actual = (int) (linea)
        if before is not None:
            if before < actual:
                count += 1
        
        before = actual

print(count)