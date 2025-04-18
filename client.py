import socket
import threading

HOST = '127.0.0.1'
PORT = 58000

alias = input('Choose a nickname >>>')
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

def client_receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-8')
            if message == "nickname?":
                client.send(alias.encode('utf-8'))
            else:
                print(message)
        except:
            print('Error!')
            client.close()
            break

def client_send():
    while True:
        message = f'{alias}: {input("")}'
        client.send(message.encode('utf-8'))

receive_thread = threading.Thread(target=client_receive)
receive_thread.start()

send_thread = threading.Thread(target=client_send)
send_thread.start()