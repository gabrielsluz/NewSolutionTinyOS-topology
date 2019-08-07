#!/bin/bash

if (($# != 1)); then
  echo "usage: ./calculate_route.sh <NUMBER_OF_NODES>"
  exit 1
fi


#$s = Tamanho topologia

if [ ! -d data ]
then
  mkdir data
fi

if [ ! -d outputsN ]
then
  mkdir outputsN
fi

if [ ! -d routesN ]
then
  mkdir routesN
fi

OLDIFS=$IFS
IFS=','

s=$1

for i in 6,17 6,93 11,58 36,20 38,53 43,80 55,26 76,80 79,63 90,44
do
      set -- $i
      if [ ! -e data/data_$s\_$1\_$2.dat ]
      then
        python create_data_file.py -i topologies/topology_$s -o data/data_$s\_$1\_$2.dat -s $1 -d $2
      fi
      if [ -e data/data_$s\_$1\_$2.dat ] && [ ! -e outputsN/output_$s\_$1\_$2.txt ]
      then
        glpsol -m shortest_paths_with_parity.mod -d data/data_$s\_$1\_$2.dat -o outputsN/output_$s\_$1\_$2.txt > glpsol_log.txt
      fi
      if [ -e outputsN/output_$s\_$1\_$2.txt ] && [ ! -e routesN/dual_$s\_$1\_$2.txt ]
      then
        python create_route_file.py -i outputsN/output_$s\_$1\_$2.txt -o routesN/dual_$s\_$1\_$2.txt
      fi
    printf "\n $1 $2 - $s"
done

printf "\n"
