#!/bin/bash

nmap 10.42.0.1/24 -oG ips.txt
python iplist.py

echo $1

while read p; do
    if [ $1 != $p ]
    then
	echo $1 
	echo $p	
        python3 mormy.py $p 1
	sleep 5
    fi
done < ips.txt

python3 wormy.py
