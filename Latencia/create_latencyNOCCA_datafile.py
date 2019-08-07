import sys
import math

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
    if len == 0:
        return
    lista[len].latency.append(latency)
    lista[len].count += 1



index = 0

lista = []
for i in range(7):
    lista.append(Task())

file = open('latencyNoCCANoAck.txt',"r")
for line in file:
    if line[0] != "s" and line[0] != "n":
        index += 1
        print(line[0])
    elif line[0] == "s" and sys.argv[1] == 'NS':
        linha = line.split(' ')
        insert_list(lista,index,float(linha[2]))
    elif line[0] == "n" and sys.argv[1] == 'N':
        linha = line.split(' ')
        print(linha[2])
        insert_list(lista,index,float(linha[2]))
for i in range(7):
    lista[i].average_and_error()


fileLt = open('datafileLatencyNoCCA'+ sys.argv[1] +'.dat',"w")

fileLt.write('# X  Y          Z1        Z2\n')
for i in {1,2,3,4,5,6}:
    fileLt.write('  {:d}'.format(i) + '  {:08.7f}'.format(lista[i].AvgLatency) + '  {:08.7f}'.format(lista[i].UpLatency) + '  {:08.7f}\n'.format(lista[i].DownLatency))
