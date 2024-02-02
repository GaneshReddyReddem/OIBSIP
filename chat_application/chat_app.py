#server
import socket
import threading

def handle_client(client_socket, address):
    print(f"Accepted connection from {address}")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if not message:
                print(f"Connection with {address} closed.")
                break

            print(f"Received message from {address}: {message}")

            # Broadcast the message to all connected clients
            for c in clients:
                if c != client_socket:
                    c.send(message.encode('utf-8'))

        except Exception as e:
            print(f"Error handling client {address}: {e}")
            break

    client_socket.close()

# Set up the server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)
print("Server listening on port 5555")

clients = []

while True:
    client_socket, client_address = server.accept()
    clients.append(client_socket)

    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
