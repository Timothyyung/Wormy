#!/bin/bash

nmap 10.42.0.1/24 -oG ips.txt
python iplist.py

while read p; do
    python3 mormy.py $p 1
done < ips.txt

python3 wormy.py
