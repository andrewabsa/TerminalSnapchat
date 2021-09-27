import socket

class Server:
    def __init__(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind(("127.0.0.1", 65432))
        self.server_socket.listen(2)
        print("Listening for a connection to the server...")
        self.connection, address = self.server_socket.accept()
        print(f"Connected by {address}")

    def receive_message(self):
        while True:
            data = self.connection.recv(1024)
            message = repr(data)
            print(message)
    

Server_func = Server()   
    

   



