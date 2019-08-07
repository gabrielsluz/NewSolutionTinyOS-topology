#!/bin/bash

 if (($# != 1)); then
   echo "usage: ./calculate_routeNS.sh <NUMBER_OF_NODES>"
   exit 1
 fi

#$1 = Tamanho topologia


if [ ! -d data ]
then
  mkdir data
fi

if [ ! -d outputs ]
then
  mkdir outputs
fi

if [ ! -d routes ]
then
  mkdir routes
fi



for l in 1 2 3 4 5 6 7 8 9 10
do
	i=$(( ( RANDOM % $1 )  + 1 ))
	j=$(( ( RANDOM % $1 )  + 1 ))
    if ((i != j && i != 0))
    then
      if [ ! -e data/data_$1\_$i\_$j.dat ]
      then
        python create_data_fileNS.py -i topologies/topology_$1 -o data/data_$1\_$i\_$j.dat -s $i -d $j
      fi
      if [ -e data/data_$1\_$i\_$j.dat ] && [ ! -e outputs/output_$1\_$i\_$j.txt ]
      then
        glpsol -m NewSolution.mod -d data/data_$1\_$i\_$j.dat -o outputs/output_$1\_$i\_$j.txt > glpsol_log.txt
      fi
      if [ -e outputs/output_$1\_$i\_$j.txt ] && [ ! -e routes/dual_$1\_$i\_$j.txt ]
      then
        python create_route_fileNS.py -i outputs/output_$1\_$i\_$j.txt -o routes/dual_$1\_$i\_$j.txt
        python verificasolucao.py routes/dual_$1\_$i\_$j.txt
      fi
    fi
    printf "\n $i $j - $1"
done

printf "\n"
