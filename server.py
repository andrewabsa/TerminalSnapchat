import socket
import threading

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
            data = self.connection.recv(1024).decode()
            message = data
            print(message)
            if not data:
                break

    def send_message(self, text):
        self.connection.send(text.encode())        

    def prompt_input(self):
        while True:
            prompt = input()
            self.send_message(prompt)
            if not prompt:
                print("You didn't enter anything...")

        
            
server_func = Server()
r = threading.Thread(target=server_func.receive_message)
r.daemon = True
r.start()
server_func.prompt_input()





   



