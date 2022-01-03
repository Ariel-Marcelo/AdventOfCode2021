entrada = []
with open("Día 6\ent.txt") as archivo:
    for line in archivo:
        entrada = line.split(",")

for a in range (256): # 80 iteraciones
  for i in range(len(entrada)): # para cada elemento de la lista
    actual = int(entrada[i]) # obtenemos el valor del elemento
    if actual > 0: # si el valor es mayor que 0
        entrada[i] = actual  - 1 # restamos 1 al valor
    else: # si no
        entrada[i] = 6 # el valor es 6
        entrada.append(8) # añadimos 8 al final de la lista

print(len(entrada))        