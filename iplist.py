#!usr/bin/env python


iplist = {}
with open('./ips.txt') as infile:
    line = infile.readline()
    while line:
        lines = line.split()
        if(lines[0] == 'Host:'):
            if(lines[1]  not in iplist.keys()):
                iplist[lines[1]] = 1
        line = infile.readline()

f = open('./ips.txt','w')
ips = ''
for key in iplist.keys():
    ips += key + '\n'

f.write(ips)

