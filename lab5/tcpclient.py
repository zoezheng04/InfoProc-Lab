import socket
print("We're in tcp client...");
#the server name and port client wishes to access
server_name = '51.20.65.178'
#'52.205.252.164'
server_port = 12000
#create a TCP client socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Set up a TCP connection with the server
#connection_socket will be assigned to this client on the server side
client_socket.connect((server_name, server_port))

msg = input("Enter a string to test if it is alphanumeric: ");
#send the message to the TCP server
client_socket.send(msg.encode())
#return values from the server
msg = client_socket.recv(1024)
print(msg.decode())
client_socket.close()
