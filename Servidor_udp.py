import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5005

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((UDP_IP, UDP_PORT))

print(f"Servidor UDP escuchando en {UDP_IP}:{UDP_PORT}")

while True:
    data, addr = server_socket.recvfrom(1024)  # Recibir datagrama
    print(f"Mensaje recibido de {addr}: {data.decode()}")
    server_socket.sendto("Mensaje recibido".encode(), addr)
