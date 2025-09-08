import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hola servidor UDP!"
client_socket.sendto(message.encode(), (UDP_IP, UDP_PORT))

data, server = client_socket.recvfrom(1024)
print("Respuesta del servidor:", data.decode())
