#!/bin/bash

paths=2paths
cca=withcca
ack=withack
routes=routesN

if [ "$routes" == "routesN" ]
then
  test=testN
else
  test=test
fi

OLDIFS=$IFS
IFS=','

for i in 10,4,55 11,4,99 12,4,100 13,55,4 14,55,99 15,55,100 16,99,4 17,99,55 18,99,100 19,100,4 20,100,55 21,100,99

do
  set -- $i
  sudo su
  python create_instance.py -f /home/twonet/Desktop/$routes/dual_$2_$3.txt &&
  make opal &&
  mv build/opal/main.exe build/opal/$test$1-$paths-$cca-$ack-$2-$3.exe
done


IFS=$OLDIFS

#Fix
