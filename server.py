import threading
import socket

HOST = '127.0.0.1'
PORT = 58000
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients = []
nicknames = []

# Function to send a message to every connected client.
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle Client
def handle_client(client):
    while True:
        try:
            message = client.recv(1024) # Listens for messages from a specific client.
            broadcast(message)
        except:
            index = clients.index(client) # If the client disconnects or throws an error:
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat room!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

#Main function to receive the clients connection

def receive():
    while True:
        print('Server is running and listening...')
        client, address = server.accept()
        print(f"Connected with {str(address)}")

        client.send('nickname?'.encode('utf-8'))
        nickname = client.recv(1024)
        nicknames.append(nickname) # Stores the nickname and client socket.
        clients.append(client)
        print(f'Nickname of the client is {nickname}'.encode('utf-8'))

        broadcast(f'{nickname} has connected in the chat room!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start() # Starts a new thread to handle this client’s messages.

if __name__ == "__main__":
    receive()