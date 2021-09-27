import socket

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect(("127.0.0.1", 65432))
        self.message_to_send = input("Send a message: ")

    def send_a_message(self):
        self.client_socket.sendall(bytes(str(self.message_to_send), "utf-8"))
        self.received_message = repr(self.client_socket.recv(1024))
        print(self.received_message)

Client_func = Client()


        
        