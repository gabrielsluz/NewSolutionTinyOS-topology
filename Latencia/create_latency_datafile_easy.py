import sys
import os.path
import math

#sys.argv[1] => NS ou N

class Task:
    def __init__(self):
        self.latency = []
        self.count = 0
        self.UpLatency = 0.0
        self.DownLatency = 0.0
        self.AvgLatency = 0.0

    def average_and_error(self):
        self.latency.sort()

        if self.count == 0:
            return

        latency_temp = 0.0
        std_dev = 0.0
        for i in range(self.count):
            latency_temp += self.latency[i]
            #print(i,self.latency[i])
        self.AvgLatency = latency_temp/self.count
        for i in range(self.count):
            std_dev += (self.latency[i] - self.AvgLatency)**2
        std_dev = math.sqrt(std_dev/self.count)
        self.UpLatency = self.AvgLatency + 1.96*(std_dev/math.sqrt(self.count))
        self.DownLatency = self.AvgLatency - 1.96*(std_dev/math.sqrt(self.count))


def insert_list(lista,len,latency):
    if len == 0 or latency == 0:
        return
    lista[len].latency.append(latency)
    lista[len].count += 1


listaNS = []
for i in range(11):
    listaNS.append(Task())

listaN = []
for i in range(11):
    listaN.append(Task())

choose = 0

file = open('latencyCollectNS442.txt',"r")

for line in file:
    if line[0] == "-":
        length = int(float(line[1]))
        if length == 0:
            length = 10
        print(length)
    else:
        linha = line.split(' ')
        taskNum = linha[0]
        if choose == 0:
            insert_list(listaNS,length,float(linha[2]))
            choose = 1
        else:
            insert_list(listaN,length,float(linha[2]))
            choose = 0
        print(float(linha[2]))
for i in range(11):
    listaNS[i].average_and_error()
    listaN[i].average_and_error()



fileLt = open('datafileLatencyNoCCANoAckNewNS.dat',"w")

fileLt.write('# X  Y          Z1        Z2\n')
for i in {1,2,3,4,5,6,7,8,9,10}:
    fileLt.write('  {:d}0'.format(i) + '  {:08.7f}'.format(listaNS[i].AvgLatency) + '  {:08.7f}'.format(listaNS[i].UpLatency) + '  {:08.7f}\n'.format(listaNS[i].DownLatency))

fileLt.close()

fileLt = open('datafileLatencyNoCCANoAckNewN.dat',"w")

fileLt.write('# X  Y          Z1        Z2\n')
for i in {1,2,3,4,5,6,7,8,9,10}:
    fileLt.write('  {:d}0'.format(i) + '  {:08.7f}'.format(listaN[i].AvgLatency) + '  {:08.7f}'.format(listaN[i].UpLatency) + '  {:08.7f}\n'.format(listaN[i].DownLatency))
