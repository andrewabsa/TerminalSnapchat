import random
import socket

class Server():
    def __init__(self):
        '''Creates server socket instance, binding itself to a given port and ip address
           
           Args: Only accepts self as given argument
           Accepts the connection once the client has connected to the given port and ip address
        '''
        # Creates a socket
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Binds to the given ip and port address
        self.server_socket.bind(("127.0.0.1", 65432))
        # Listens for incoming connections
        self.server_socket.listen(2)
        pick = input("Name the chat server: ")
        print(f"{pick} launched... \nWaiting for client to join...")
        # Accepts the connection request once the client attempts to connect
        self.connection, address = self.server_socket.accept()
        print(f"You are now connected to {address}")
        print(f"Welcome to {pick}!")

    def receive_message(self):
        '''As long as the server receives a message it returns it the screen as a string representation
           It initially receives the text in byte format, "b'" is stripped from the text to make it more readable
           
           Returns: Stripped string converted from bytes
        '''
        while True:
            # Whenever the server receives some data, print it to the screen 
            data = self.connection.recv(1024)
            self.msg = repr(data)
            # Print the message, stripping the "b'"
            print(self.msg.strip("b'"))

    def send_message(self):
        '''User input is provided to send a message to the client(s)
           It is encoded in utf-8 and converted from bytes to str
           Returns: String converted from bytes 
        '''
        # Input to send a message
        self.message_to_send = input()
        # Now send it to one or more clients      
        self.server_socket.send(bytes(str(self.msg), "utf-8"))

class Client():
    def __init__(self):
        '''Creates client socket instance, connecting to the given port and ip address
           
           Args: Only accepts self as given argument
           Requests a connection to the server, which the server then accepts and allows the client to connect
           
           Returns: Print statement letting the user know that the client has successfully connected
           to the server socket
        '''
        # Create the client socket
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Let user know the socket is attempting to connect
        print("Attempting connection...")
        # Connect to the server using the given ip and port address
        self.client_socket.connect(("127.0.0.1", 65432))
        print("You have joined the server...")
        print(f"Welcome to the server!")
        # Provide user with input to enter a username
        self.usr = input("Type a username: ")
        self.name = Username(self.usr)

    def send_message(self):
        '''Input is provided in order to send a message to the server
           The message being sent is sent as repr in byte chunks of 1024

           Returns: String to the server socket converted from bytes
        '''
        # Get input from the user to send a message       
        self.message_to_send = input(f"{self.usr}: ")
        # Then send the message
        self.client_socket.sendall(self.message_to_send.encode())
        self.received_message = repr(self.client_socket.recv(1024))
        # Now print the message
        print(self.received_message)


class Username():
    def __init__(self, nickname):
        self.nickname = nickname
        self.name_list = []
        
    def add_name(self):
        self.name_list.append(self.nickname)
    

class Message():
    def __init__(self):
        pass

    def send_text(self, txt):
        pass

    def send_messages(self):
        pass

class Names():
    def __init__(self, namelist):
        self.value = {
            "Tom": 0,
            "Emmanuel": 0,
            "Brad": 0,
            "Russel": 0
         }
        for name in namelist:
            self.value[name.value] += 5

    def name_choice(self):
        self.nickname = random.choice(self.value)


 

            
    


   

    
   
    
    




    

