import sys
import os.path
import math

#sys.argv[1] => NS ou N

class Task:
    def __init__(self):
        self.th = []
        self.dr = []
        self.count = 0
        self.UpTh = 0.0
        self.DownTh = 0.0
        self.UpDr = 0.0
        self.DownDr = 0.0
        self.AvgTh = 0.0
        self.AvgDr = 0.0

    def average_and_error(self):
        self.th.sort()
        self.dr.sort()

        if self.count == 0:
            return

        th_temp = 0.0
        dr_temp = 0.0
        std_dev_th = 0.0
        std_dev_dr = 0.0
        for i in range(self.count):
            th_temp += self.th[i]
            dr_temp += self.dr[i]
            print(i,self.dr[i],self.th[i])
        self.AvgTh = th_temp/self.count
        self.AvgDr = dr_temp/self.count
        for i in range(self.count):
            std_dev_th += (self.th[i] - self.AvgTh)**2
            std_dev_dr += (self.dr[i] - self.AvgDr)**2
        std_dev_th = math.sqrt(std_dev_th/self.count)
        std_dev_dr = math.sqrt(std_dev_dr/self.count)
        self.UpTh = self.AvgTh + 1.96*(std_dev_th/math.sqrt(self.count))
        self.DownTh = self.AvgTh - 1.96*(std_dev_th/math.sqrt(self.count))
        self.UpDr = self.AvgDr + 1.96*(std_dev_dr/math.sqrt(self.count))
        self.DownDr =  self.AvgDr - 1.96*(std_dev_dr/math.sqrt(self.count))



def get_path_size(nodes,source,destination):
    if(os.path.isfile('./routesantigas'+sys.argv[1]+'/dual_{0}_{1}_{2}.txt'.format(nodes,source,destination))):
        routes = open('./routesantigas'+sys.argv[1]+'/dual_{0}_{1}_{2}.txt'.format(nodes,source,destination))
        arquivo = routes.readlines()
        lenline = arquivo[1].split(' ')
        return int(lenline[4])/2
    else:
        return 0

def get_routes(taskNum, iden):
    tasks = open('Formated_Tasks.txt',"r")
    tarefa = list();
    for line2 in tasks:
        linha2 = line2.split(" ")
        if linha2[0] == taskNum:
            len = get_path_size(linha2[2],linha2[3],linha2[4])
    tasks.close()
    return len

def insert_list(lista,len,th,dr):
    if len == 0:
        return
    lista[len].th.append(th)
    lista[len].dr.append(dr)
    lista[len].count += 1




if sys.argv[1] == 'NS':
    baseFileName = 'throughputCollectNS'
elif sys.argv[1] == 'N':
    baseFileName = 'throughputCollect'

fileNum = 10

lista = []
for i in range(10):
    lista.append(Task())

while(fileNum <= 100):
    file = open(baseFileName + '{0}'.format(fileNum) + '.txt',"r")
    fileNum += 10
    for line in file:
        linha = line.split(' ')
        taskNum = linha[0]
        #print(taskNum)
        length = get_routes(taskNum, sys.argv[1])
        #print(length,float(linha[3]),float(linha[5]))
        insert_list(lista,length,float(linha[3]),float(linha[5]))
for i in range(9):
    lista[i].average_and_error()
    print(i , lista[i].AvgTh , lista[i].AvgDr, lista[i].count)


fileTh = open('datafileThroughput'+ sys.argv[1] +'.dat',"w")
fileDr = open('datafileDeliveryRate'+  sys.argv[1] +'.dat',"w")

fileTh.write('# X  Y          Z1        Z2\n')
fileDr.write('# X  Y          Z1        Z2\n')
for i in {1,2,3,4,5,6,7,8}:
    fileTh.write('  {:d}'.format(i) + '  {:08.7f}'.format(lista[i].AvgTh) + '  {:08.7f}'.format(lista[i].UpTh) + '  {:08.7f}\n'.format(lista[i].DownTh))
    fileDr.write('  {:d}'.format(i) + '  {:08.7f}'.format(lista[i].AvgDr) + '  {:08.7f}'.format(lista[i].UpDr) + '  {:08.7f}\n'.format(lista[i].DownDr))
