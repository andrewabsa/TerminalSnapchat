import socket
import threading

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("Attempting connection...")
        self.client_socket.connect(("127.0.0.1", 65432))
        print("Welcome to the chat server!")
    
    def receive_message(self):
        while True:
            data = self.client_socket.recv(1024).decode()
            message = data
            print(message)
            if not data:
                break

    def send_message(self, text):
        self.client_socket.send(text.encode())        

    def prompt_input(self):
        while True:
            prompt = input()
            self.send_message(prompt)
            if not prompt:
                print("You didn't enter anything...")



client_func = Client()
r = threading.Thread(target=client_func.receive_message)
r.daemon = True
r.start()
client_func.prompt_input()






        
        