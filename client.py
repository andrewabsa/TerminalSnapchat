import socket
class Client:

    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Attempting connection...")
        self.client_socket.connect(("127.0.0.1", 65432))
        print("Welcome to the chat server!")
        self.username_selection = input("Enter your username: ")
        self.message_to_send = input(f"{self.username_selection}: ")

    def send_a_message(self):
        self.client_socket.sendall(bytes(str(self.message_to_send), "utf-8"))
        self.received_message = repr(self.client_socket.recv(1024))
        print(self.received_message)

    def send_another_message(self):
        pass
        

client_func = Client()
client_func.send_a_message()



        
        