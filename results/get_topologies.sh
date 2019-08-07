#!/bin/bash

if (($# != 2)); then
  echo "usage: ./get_topologies.sh <FIRST> <NUMBER_OF_NODES>"
  exit 1
fi

INIT=$1
for i in $(seq $INIT $INIT)
do
  if [ ! -e testbed/result_$i.tgz ]
  then
    wget ftp://twonet.cs.uh.edu:8080/result_$i.tgz
    mv result_$i.tgz testbed/result_$i.tgz
  fi
  if [ -e testbed/result_$i.tgz ]
  then
    python process_topology.py testbed/result_$i.tgz
    mv topology ../topologies/topology_$2
  else
    echo "File result_$i.tgz not downloaded!"
  fi
done
