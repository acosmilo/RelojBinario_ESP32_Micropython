import socket

mi_socket = socket.socket()
mi_socket.connect( ('192.168.100.4', 80) )

mi_socket.send('17'.encode())
mi_socket.send('20'.encode())
#mi_socket.send('0'.encode())
respuesta = mi_socket.recv(1024)

print(respuesta)

mi_socket.close()
