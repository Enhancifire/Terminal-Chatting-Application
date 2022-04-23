import socket
import threading

HOST = '127.0.0.1'
PORT = 2077

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

stop = False

def receive():
    global stop
    while not stop:
        msg = client.recv(1024).decode('utf-8')
        print(msg)

def main():
    global stop
    nickname = input("Enter your username: ")
    client.send(nickname.encode('utf-8'))

    thread = threading.Thread(target=receive)
    thread.start()

    while True:
        msg = input(f"{nickname}> ")
        acmsg = f"{nickname}> {msg}"
        client.send(acmsg.encode('utf-8'))

        if KeyboardInterrupt:
            stop = True

if __name__ == "__main__":
    main()
