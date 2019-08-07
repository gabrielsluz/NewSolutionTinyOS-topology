import sys
#sys.argv[1] = input file


file = open(sys.argv[1],"r")
outputNS = open('latencyNSfinal.txt',"a")
outputN = open('latencyNfinal.txt',"a")

choose = 'NS'

for line in file:
    linha = line.split(" ")
    if len(linha) > 2:
        if choose == 'NS':
            linha2 = linha[2].split(".")
            outputNS.write('{0}   {1}'.format(linha[0],linha2[0]) + '.' + '{0}'.format(linha2[1]))
            choose = 'N'
        else:
            linha2 = linha[2].split(".")
            outputN.write('{0}   {1}'.format(linha[0],linha2[0]) + '.' + '{0}'.format(linha2[1]))
            choose = 'NS'
