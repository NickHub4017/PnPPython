import os
import socket

HOST, PORT = '', 8888

listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listen_socket.bind((HOST, PORT))
listen_socket.listen(1)
print 'Serving HTTP on port %s ...' % PORT
while True:
    client_connection, client_address = listen_socket.accept()
    filesize = client_connection.recv(4)
    print "filesize is :-"+filesize
    filesize=int(filesize)

    filedata = client_connection.recv(filesize)
    my_bytes = bytearray(filedata)
   # print filedata
    target = open("myfile.c", 'wb')
    target.write(filedata)
    target.close()
    print(os.system("gcc 'myfile.c'"))
    print(os.system("./a.out"))

    #filesize = client_connection.recv(10)





#
#
#     http_response = """\
# HTTP/1.1 200 OK
#
# Hello, World!
# """
#     request = client_connection.recv(10)
#     print "----------------\n";
#     print request

    #client_connection.sendall(http_response)
    client_connection.close()