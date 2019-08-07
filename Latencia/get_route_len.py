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



def get_path_size(nodes,source,destination):
    if(os.path.isfile('./routes'+sys.argv[1]+'/dual_{0}_{1}_{2}.txt'.format(nodes,source,destination))):
        routes = open('./routes'+sys.argv[1]+'/dual_{0}_{1}_{2}.txt'.format(nodes,source,destination))
        arquivo = routes.readlines()
        lenline = arquivo[1].split(' ')
        return int(lenline[4])/2
    else:
        return 0

def get_routes(taskNum):
    tasks = open('Formated_Tasks.txt',"r")
    tarefa = list();
    for line2 in tasks:
        linha2 = line2.split(" ")
        if linha2[0] == taskNum:
            len = get_path_size(linha2[2],linha2[3],linha2[4])
            print(len)
    tasks.close()
    return len

def insert_list(lista,len,latency):
    if len == 0:
        return
    lista[len].latency.append(latency)
    lista[len].count += 1




if sys.argv[1] == 'NS':
    baseFileName = 'latencyNSfinal'
elif sys.argv[1] == 'N':
    baseFileName = 'latencyNfinal'


lista = []
for i in range(10):
    lista.append(Task())

file = open(baseFileName +'.txt',"r")

for line in file:
    linha = line.split(' ')
    taskNum = linha[0]
    print(taskNum)
    length = get_routes(taskNum)
    #print(linha)
    insert_list(lista,length,taskNum)
for i in range(9):
    lista[i].average_and_error()
    print(i)
    for j in range(len(lista[i].latency)):
        print(lista[i].latency[j])
