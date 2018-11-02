import socket
import sys

# https://www.bogotobogo.com/python/python_network_programming_server_client.php

# creates socket object
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM)

# host = socket.gethostname() # or just use (host = '')
host = 'localhost'
port = 9999

print (host)
print (port)
# sys.exit(1)

s.connect((host, port))

tm = s.recv(1024) # msg can only be 1024 bytes long

s.close()
print("the time we got from the server is %s" % tm.decode('ascii'))