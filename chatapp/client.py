import socket
import threading

# Function to receive messages from the server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(message)
            else:
                break
        except:
            print("An error occurred while receiving messages.")
            client_socket.close()
            break

# Function to send messages to the server
def send_messages(client_socket):
    while True:
        message = input()
        if message.strip():  # Avoid sending empty messages
            client_socket.send(message.encode('utf-8'))

# Start the client
def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(("127.0.0.1", 5555))

    # Start threads for receiving and sending messages
    thread_receive = threading.Thread(target=receive_messages, args=(client_socket,))
    thread_receive.start()

    thread_send = threading.Thread(target=send_messages, args=(client_socket,))
    thread_send.start()

if __name__ == "__main__":
    start_client()
