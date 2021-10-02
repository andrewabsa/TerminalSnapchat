import socket
from classes import Username

class Client():
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Attempting connection...")
        self.client_socket.connect(("127.0.0.1", 65432))
        print("You have joined the server...")
        print(f"Welcome to the server!")
        self.usr = input("Type a username: ")
        self.name = Username(self.usr)

    def prompt(self):
        self.message_to_send = input(f"{self.usr}: ")

    def send_message(self):
        self.client_socket.sendall(self.message_to_send.encode())
        self.received_message = repr(self.client_socket.recv(1024))
        print(self.received_message)

Client_run = Client()
Client_run.prompt()
Client_run.send_message()

