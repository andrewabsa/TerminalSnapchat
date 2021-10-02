# Algorithmic Solution: Terminal Snapchat

### How Input and Output will be handled:
- Upon launching the program, it will initially ask the user for input, from the client file, to insert a string as text and then communicate and allow the server to receive that text as output. 

### Structure of the solution(classes and other entities):

- The program will be structured around two main classes: The Server and Client class.
These will contain their own methods in order to create a program which utilises two way communication between the client and server. Examples of these class methods include: "send_message", "receive_message". The solution structure will limit the use of functions for additional features and will the majority of these features will be implemented by use of instantiated classes and class attributes also utilising class properties/decorators.

### How the algorithm will function:

- Terminal Snapchat will allow users (client & server) to send and receive messages to each other via socket communication through the command line: The main use and function of this algorithm will be to facilitate the sending and receiving of messages between two computers, in this case it will between the server and the client. This will work through a sequence of steps implemented in the algorithm:

 1. Firstly, the server and client files must simultaneously be launched for the program to function. The server socket will initially begin to listen for any incoming connections.
 2. Once the client is launched it will connect to the server using the given ip and port numbers. This will create a connection between the two networks.
 3. Text is sent in byte format from the client and then converted back into string format and can now be sent to the server.


### Python Dependencies used:

- socket


