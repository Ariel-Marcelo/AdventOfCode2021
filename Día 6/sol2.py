import collections

def sol(entrada: list):
    listaPescados = entrada
    midict = {}

    def fOne(value: int):
        day = 0
        # Parte uno
        day = value+1
        # añadir a diccionario si no está ya
        if day not in midict: # si no está
            midict[day] = 1 # añadimos 1
        else:
            midict[day] += 1 # si está, sumamos 1
        # parte dos
        for i in range(day+7, 256+1, 7): # para cada día
            if i not in midict:
                midict[i] = 1
            else:
                midict[i] += 1

    def fTwo(day: int, numNacimientos: int):
        # Parte uno
        day = day+9
        if day > 256:
            return False
        else:
            # añaadir a diccionario si no está ya
            if day not in midict:
                midict[day] = numNacimientos
            else:
                midict[day] += numNacimientos

        # parte dos
        for i in range(day+7, 256+1, 7): # para cada día
            if i not in midict: # si no está
                midict[i] = numNacimientos  # añadimos el numero de nacimientos
            else:
                midict[i] += numNacimientos # si está, sumamos el numero de nacimientos 

    for i in range(len(listaPescados)): # para cada elemento de la lista
        fOne(listaPescados[i]) # llamamos a la función uno

    result = collections.OrderedDict(sorted(midict.items())) # ordenamos el diccionario
    print(result) 

    for i in range(256+1): # para cada día
        if i in midict: # si está
            fTwo(i, midict[i]) # llamamos a la función fTwo

    aux = 0
    for key, value in midict.items(): # para cada elemento del diccionario
        aux += value

    print(midict)
    return len(listaPescados) + aux


def getEntrada():
  entrada = []
  with open("Día 6\ent.txt") as archivo:
      for line in archivo:
          entrada = [int(x) for x in line.split(",")]

  return entrada

print(sol(getEntrada()))
