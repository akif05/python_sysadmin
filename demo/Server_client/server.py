import time
import socket

# https://www.bogotobogo.com/python/python_network_programming_server_client.php
# creating a socket object
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# get local Host machine name
# host = socket.gethostname() # or just use (host == '')
host = 'localhost'
port = 9999

# bind to pot
s.bind((host, port))

# Que up to 5 requests
s.listen(5)

while True:
    # establish connection
    clientSocket, addr = s.accept()
    print("got a connection from %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientSocket.send(currentTime.encode('ascii'))
    clientSocket.close()