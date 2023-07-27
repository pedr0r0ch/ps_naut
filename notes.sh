#!/bin/sh
data=$(date)
echo "script notes is runing !"
echo "$1" >> ~/notes
echo "Date: $data" >> ~/notes
