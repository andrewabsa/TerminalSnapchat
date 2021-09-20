import socket

IP = "1.42.159.144"
PORT = 2345

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((IP, PORT))

server_socket.listen()

server_socket.close()


