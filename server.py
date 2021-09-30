from classes import Message
import socket

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("127.0.0.1", 65432))
        self.server_socket.listen(2)
        print("Listening for a connection to the server...")
        self.connection, address = self.server_socket.accept()
        print(f"You are now connected to {address}")
        print("Welcome to the chat server!")

    def receive_message(self):
        while True:
            data = self.connection.recv(1024)
            self.msg = repr(data)
            print(self.msg.strip("b'"))

    def send_message(self):
        self.connection.sendall(bytes(str(self.msg), "utf-8"))

Server_run = Server()
Server_run.receive_message()
Server_run.send_message()





   



