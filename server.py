import socket
import threading

HOST = '127.0.0.1'
PORT = 2077

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen()

clients = [
        [],
        []
        ]
threads = []

stop = False

def broadcast(message):
    for client in clients[1]:
        client.send(message)

    return

def handle(client):
    global stop
    while True:
        try:
            msg = client.recv(1024)
            broadcast(msg)

        except:
            index = clients[1].index(client)
            clients[0].remove(clients[0][index])
            clients[1].remove(client)
            return

def receive():
    try:
        while True:
            client, add = server.accept()

            print(f"Connected with {str(add)}")

            nickname = client.recv(1024)

            clients[0].append(nickname)
            clients[1].append(client)

            broadcast(f"{nickname} connected to server!\n".encode('utf-8'))
            client.send("Connected to server".encode('utf-8'))

            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
            threads.append(thread)


    except KeyboardInterrupt:
        for thread in threads:
            pass

        print("Closing")

print(f"Server listening on {HOST}:{PORT}")
receive()
