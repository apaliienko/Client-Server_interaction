import sys
from socket import *


serverHost = 'localhost'
serverPort = 50007

message = [b'Message']

if len(sys.argv)>1:
    serverHost = sys.argv[1]
    if len(sys.argv) > 2:
        message = (x.encode() for x in sys.argv[2:])

socketobj = socket(AF_INET, SOCK_STREAM)
socketobj.connect((serverHost, serverPort))

for line in message:
    socketobj.send(line)
    data = socketobj.recv(1024)
    print('Client received:', data)

socketobj.close()
