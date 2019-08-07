#!/bin/bash

 if (($# != 1)); then
   echo "usage: ./calculate_routeNS.sh <NUMBER_OF_NODES> <PATH_SIZE>"
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

if [ ! -d outputsN ]
then
  mkdir outputsN
fi

if [ ! -d routesN ]
then
  mkdir routesN
fi

counter=1

while [ $counter -le 10 ]
do
	i=$(( ( RANDOM % $1 )  + 1 ))
	j=$(( ( RANDOM % $1 )  + 1 ))
    if ((i != j && i != 0))
    then
      if [ ! -e data/data_$1\_$i\_$j.dat ]
      then
        python create_data_file.py -i topologies/topology_$1 -o data/data_$1\_$i\_$j.dat -s $i -d $j
      fi
      if [ -e data/data_$1\_$i\_$j.dat ] && [ ! -e outputsN/output_$1\_$i\_$j.txt ]
      then
        glpsol -m shortest_paths_with_parity.mod -d data/data_$1\_$i\_$j.dat -o outputsN/output_$1\_$i\_$j.txt > glpsol_log.txt
      fi
      if [ -e outputsN/output_$1\_$i\_$j.txt ] && [ ! -e routesN/dual_$1\_$i\_$j.txt ]
      then
        python create_route_file.py -i outputsN/output_$1\_$i\_$j.txt -o routesN/dual_$1\_$i\_$j.txt
        counter=$(($counter + 1))

        file="routesN/dual_$1_${i}_$j.txt"

        while IFS= read -r var
        do
          echo "$var"

        done <"$file"
        rm routesN/dual_$1\_$i\_$j.txt
        rm outputsN/output_$1\_$i\_$j.txt
      fi
    fi
    printf "\n $i $j - $1"
done

printf "\n"
