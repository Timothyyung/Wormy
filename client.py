import socket

s = socket.socket()
host = socket.gethostname()
port = 5050

s.connect((host,port))

f = open('/home/scott/Desktop/file.log', 'rb')

l = f.read(1024)

while(l):
    print ('Sending...')
    s.send(l)
    l = f.read(1024)
f.close

s.close
