import sys
import os.path

# System arguments: #1 = Starting output
# %2 = Finishing output
# %3 = Size of topology

fileNum = int(sys.argv[1])

soma = 0
num = 0
source = 0
empty = 1

output = open(('latencyCollect' + sys.argv[3] + '.txt'),"a")

while(fileNum <= int(sys.argv[2])):
    if(os.path.isfile('../results/outputs/out_{0}.txt'.format(fileNum))):
        file = open('../results/outputs/out_{0}.txt'.format(fileNum),"r")
        test_num = list();
        for line in file:
            linha = line.split("\t")
            for i in range(len(linha)):
                linha2 = linha[i].split(" ")
                if len(linha2) > 1:
                    if linha2[0] == 'SOURCE_NODE':
                        source = 1
                    elif linha2[0] == 'RELAY_NODE':
                        source = 0
                    elif linha2[0] == '79':
                        soma += float(linha2[1])
                        num += 1
                    elif linha2[0] == 'TEST_NUMBER' and source == 1:
                        if num != 0:
                            print(soma/num,num)
                            test_num.append(soma/num)
                            soma = 0
                            num = 0
                        else:
                            test_num.append(0.0)
            if source == 1:
                empty = 0

        if empty == 0:
            test_num.sort()
            soma2 = 0
            num2 = 0
            for i in range(len(test_num)):
                if i > 0 and test_num[i] > 0.0:
                    soma2 += test_num[i]
                    num2 += 1
                    print(test_num[i],num2)
            if num2 != 0:
                output.write('{0} - '.format(fileNum) + '{0}\n'.format(soma2/num2))
    fileNum += 1
    num = 0
    soma = 0
    source = 0
    del test_num[:]
    print(fileNum)
