#!/bin/bash
awk '{if(NR==1 || $2>max) max=$2} END {print max}' data.txt
