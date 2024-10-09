import socket
import threading
import time

# Global list to keep track of connected clients
clients = []

# Handle each client connection
def handle_client(client_socket, client_address):
    print(f"{client_address} connected.")
    client_socket.send("Enter your username: ".encode('utf-8'))
    
    username = client_socket.recv(1024).decode('utf-8')
    clients.append((client_socket, username))
    
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                full_message = f"[{timestamp}] {username}: {message}"
                print(full_message)
                broadcast(full_message, client_socket)
            else:
                break
        except:
            break

    print(f"{username} disconnected.")
    clients.remove((client_socket, username))
    client_socket.close()

# Broadcast message to all clients except the sender
def broadcast(message, sender_socket):
    # Log chat history to a file
    with open("chat_history.txt", "a") as history_file:
        history_file.write(message + "\n")
    for client in clients:
        if client[0] != sender_socket:
            try:
                client[0].send(message.encode('utf-8'))
            except:
                pass  # Ignore any errors when sending messages

# Main function to run the server
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 5555))
    server.listen(5)
    print("Server started...")

    while True:
        client_socket, client_address = server.accept()
        thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
        thread.start()

if __name__ == "__main__":
    start_server()
