import sys
import os.path


if sys.argv[1] == 'N':
    base_file_name = 'latencyCollect'
    output_name = 'latencyNfinal.txt'
elif sys.argv[1] == 'NS':
    base_file_name = 'latencyCollectNS'
    output_name = 'latencyNSfinal.txt'

fileNum = 10
output = open(output_name+'teste',"a")

while(fileNum <= 100):
    file = open(base_file_name + '{0}'.format(fileNum) + '.txt',"r")
    print(fileNum)
    for line in file:
        linha = line.split(" ")
        if len(linha) > 2:
            linha2 = linha[2].split(".")
            if linha2[0] != '0':
                output.write('{0}   {1}'.format(linha[0],linha2[0]) + '.' + '{0}'.format(linha2[1]))
    fileNum += 10
    file.close()
