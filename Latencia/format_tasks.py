import sys
import os.path

def  get_task(linha):
    linha2 = linha.split("\t")
    return linha2[1]

def format_task(task, output):
    split_task = task.split("-")
    i = 0
    if len(split_task) != 3:
        output.write('\n')
        #print(task)
        return
    if split_task[0][0] == 'V':
        i += 1
    if split_task[0][i] == 'N':
        output.write('N ')
        i += 1
    else :
        output.write('NS ')
    while(i < len(split_task[0])):
        output.write('{0}'.format(split_task[0][i]))
        i += 1
    output.write(' {0} '.format(split_task[1]) + '{0}'.format(split_task[2]))
    output.write('\n')



output = open('Formated_Tasks.txt',"a")
fileTasks = open('Tasks.txt',"r")
fileNum = 2004

arquivos = list();

while(fileNum <= 3240):
    if(os.path.isfile('../results/testbed/result_{0}.tgz'.format(fileNum))):
        arquivos.append(fileNum)
    fileNum += 1

i = len(arquivos)-1

for line in fileTasks:
    if i < 0:
        break

    task = get_task(line)

    output.write('{0} '.format(arquivos[i]))
    format_task(task, output)
    #print(arquivos[i])
    i = i -1
