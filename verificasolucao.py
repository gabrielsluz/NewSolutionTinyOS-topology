import sys

def min(path1, path2):
    if len(path1) < len(path2):
        return len(path1)
    else:
        return len(path2)

def comparaCaminhos(path1, path2):
    for i in range(1,min(path1,path2)-1):
        if path1[i] == path2:
            return 0
    return 1



routes = open(str(sys.argv[1]),"r")
linha = 0
id = 0
caminho1 = []
caminho2 = []


for line in routes:
    linha = linha + 1
    if linha == 2:
        lenstr = line.split(":")
        hops = int(float(lenstr[1]))
        if hops % 2 != 0:
            print("INVALIDA")
    if linha == 4:
        sourcestr = line.split("=")
        sourcestr2 = sourcestr[1].split(";")
        source = int(float(sourcestr2[0]))
    if linha > 8:
        string = line.split("{")
        if len(string) > 1:
            numerostr  = string[1].split("}")
            numeros = numerostr[0].split(",")
            if int(float(numeros[0])) == source:
                id += 1
            if id == 1:
                caminho1.append(int(float(numeros[0])))
                caminho1.append(int(float(numeros[1])))
            else:
                caminho2.append(int(float(numeros[0])))
                caminho2.append(int(float(numeros[1])))
if comparaCaminhos(caminho1,caminho2) & (len(caminho1)%2 == len(caminho2)%2):
    print("VALIDA")
else:
    print("INVALIDA")

routes.close()
