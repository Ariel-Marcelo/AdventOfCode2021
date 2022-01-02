def myPuzzleDay2(commands:list):
    horpos = 0 # posicion horizontal
    depth = 0 # profundidad
    for command in commands:
        aux = command.split(" ") # separo el comando
        if aux[0] == "up": # si el comando es up, resto la profundidad
            depth -= int(aux[1])
        if aux[0] == "down": # si el comando es down, sumo la profundidad
            depth += int(aux[1])
        if aux[0] == "forward": # si el comando es forward, aumento la posicion horizontal
            horpos += int(aux[1])
    return horpos * depth # multiplico la posicion horizontal por la profundidad

def getList(): # obtengo la lista de comandos
    with open("Day2\day2_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

#Print the result
print(myPuzzleDay2(getList()))