import socket

class Server():
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("127.0.0.1", 65432))
        self.server_socket.listen(2)
        pick = input("Name the chat server: ")
        print(f"{pick} launched... \nWaiting for client to join...")
        self.connection, address = self.server_socket.accept()
        print(f"You are now connected to {address}")
        print(f"Welcome to {pick}!")

    def receive_message(self):
        while True:
            data = self.connection.recv(1024)
            self.msg = repr(data)
            print(self.msg.strip("b'"))

    def send_message(self):
        self.message_to_send = input()
        self.server_socket.send(bytes(str(self.msg), "utf-8"))

Server_run = Server()
Server_run.receive_message()
Server_run.send_message()





   



