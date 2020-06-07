#!/bin/bash
for i in $(adb devices | grep "devices$" | awk '{print $1}')
do
  echo "start: {$i}"
  udid= $i pytest test_grid.py &
done