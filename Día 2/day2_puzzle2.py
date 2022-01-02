def myPuzzleDay2(commands:list):
    horpos = 0 # posicion horizontal
    depth = 0 # profundidad
    aim = 0 # apuntar
    for command in commands:
        aux = command.split(" ") # separo el comando
        if aux[0] == "up": # si el comando es up, disminuyo el apuntador
            aim -= int(aux[1])
        if aux[0] == "down": # si el comando es down, aumento el apuntador
            aim += int(aux[1])
        #si el comando es forward, aumento la posicion horizontal y aumento la profundidad
        if aux[0] == "forward":
            horpos += int(aux[1])
            depth += aim*int(aux[1])
    return horpos * depth #multiplico la posicion horizontal por la profundidad

def getList(): # get list from file
    with open("Day2\day2_puzzle1_list.txt") as f:
        return [str(line.strip()) for line in f]

#print result
print(myPuzzleDay2(getList()))