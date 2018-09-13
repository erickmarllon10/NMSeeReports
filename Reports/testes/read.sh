#!/bin/bash

for arq in `cat /home/see/Indra/NMSeePlusv4.0/TempGraphId/Linux/cpu_utilization.txt `; do
  graphid=$arq
  echo $graphid
done
