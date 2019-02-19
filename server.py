import socket

s = socket.socket()
host = socket.gethostname()
port = 5050
s.bind((host,port))

s.listen(5)

while True:
    c , addr = s.accept()
    print ('We got that connection from ', addr)
    a = addr[0]
    f = open(a + 'log.txt', 'wb')
    l = c.recv(1024)
    while(l):
        f.write(l)
        l = c.recv(1024)
    f.close()






