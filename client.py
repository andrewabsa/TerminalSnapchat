import socket

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Attempting connection...")
        self.client_socket.connect(("127.0.0.1", 65432))
        print("Welcome to the chat server!")
        self.message_to_send = input()

    def send_message(self):
        self.client_socket.sendall(self.message_to_send.encode())
        self.received_message = repr(self.client_socket.recv(1024))
        print(self.received_message)

    


Client_run = Client()
Client_run.send_message()

