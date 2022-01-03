def myPuzzleDay3(report: list):

    aux = {int(x) for x in range(0,len(report))}
    tam = len(report[0])
    mydict = {0:0, 1:0}
    oxingG = ""
    co2 = ""
    eliminated = set()
    winner = ""
    i = 0
    for i in range(tam):
        #comprobacion de cantidad eliminada
        if len(eliminated) == len(report)-1:
            aux2 = aux - eliminated
            oxingG = report[list(aux2)[0]]
            break

        for j in range(len(report)):
            if j in eliminated:
                continue

            if report[j][i] == "0":
                mydict[0] += 1
            else:
                mydict[1] += 1
        if mydict[1] >= mydict[0]:
            winner = "1"
        else:
            winner = "0"
        #reseteo
        mydict = {0:0, 1:0}

        #agregamos a eliminated
        for j in range(len(report)):
            if report[j][i] != winner:
                eliminated.add(j)
    
    aux2 = aux - eliminated
    oxingG = report[list(aux2)[0]]

    #reseteo
    eliminated.clear()

    mydict = {0:0, 1:0}
    for i in range(tam):
        if len(eliminated) == len(report)-1:
            aux2 = aux - eliminated
            co2 = report[list(aux2)[0]]
            break

        for j in range(len(report)):
            if j in eliminated:
                continue

            if report[j][i] == "0":
                mydict[0] += 1
            else:
                mydict[1] += 1
        if mydict[0] <= mydict[1]:
            winner = "0"
        else:
            winner = "1"
        mydict = {0:0, 1:0}


        #agregamos a eliminated
        for j in range(len(report)):
            if report[j][i] != winner:
                eliminated.add(j)

    aux2 = aux - eliminated
    co2 = report[list(aux2)[0]]
  
    #respuesta 
    return int(oxingG,2) * int(co2,2)

def getList():
    with open("Ejercicio 3\list.txt") as f:
        return [str(line.strip()) for line in f]

#imprimimos el resultado

print(myPuzzleDay3(getList()))

test = ["00100",
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
        
print(myPuzzleDay3(test))
