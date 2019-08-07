import sys
import os.path

# System arguments: #1 = Starting output
# %2 = Finishing output
# %3 = Size of topology
#th = throughput
#dr =  delivery rate

output = open(('throughputCollect' + sys.argv[3] + '.txt'),"a")

fileNum = int(sys.argv[1])

empty = 1

while(fileNum <= int(sys.argv[2])):
    if(os.path.isfile('../results/tables/table_{0}.txt'.format(fileNum))):
        file = open('../results/tables/table_{0}.txt'.format(fileNum),"r")
        delivery_rate = list();
        throughput = list();
        for line in file:
            linha = line.split("\t")
            if linha[0] != 'error' and linha[1] != 'error' and linha[2] != 'error':
                if float(linha[2]) == 0 or float(linha[0]) == 0 :
                    th = 0.0
                    dr = 0.0
                else:
                    th = float(linha[1])*118 / float(linha[2])
                    dr =  float(linha[1])/ float(linha[0])
            else:
                th = 0.0
                dr = 0.0
            throughput.append(th)
            delivery_rate.append(dr)
            empty = 0
        if empty == 0:
            throughput.sort()
            delivery_rate.sort()
            somath = 0
            somadr = 0
            num = 0
            for i in range(len(throughput)-2):
                somath += throughput[i]
                somadr += delivery_rate[i]
                num += 1
            if num != 0:
                output.write('{0}   '.format(fileNum) +  '{0}  '.format(somath/num) + '{0}\n'.format(somadr/num))
    fileNum += 1
    del delivery_rate[:]
    del throughput[:]
    print(fileNum)
