import socket
import os

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8888)
print 'connecting to %s port %s' % server_address
sock.connect(server_address)
try:

    # Send data
    message = 'This is the message.  It will be repeated.'
    #print >>sys.stderr, 'sending "%s"' % message
    statinfo = os.stat('foo.txt')
    filesize=statinfo.st_size
    sock.sendall(str(filesize))



    file=open("foo.txt", "rb")
    byte = file.read(filesize)
    sock.send(byte)




finally:
    #print >>sys.stderr, 'closing socket'
    sock.close()