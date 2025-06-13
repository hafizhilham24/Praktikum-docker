#!/bin/bash
awk '{sum+=$3; count++} END {print sum/count}' data.txt
