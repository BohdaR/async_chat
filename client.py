import socket
import sys
from time import sleep
import threading


def send_massage(client):
    while True:
        try:
            client.send(f"Ivan {input('Enter massage: ')}".encode())
        except KeyboardInterrupt:
            break


def recv_massage(client, count):
    while True:
        print(client.recv(1024).decode())


def main():
    count = 10
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('127.0.0.1', 8000))
    client.send(sys.argv[1].encode())

    # recv_trh = threading.Thread(target=recv_massage, args=(client, count))
    #
    # recv_trh.start()
    send_massage(client)


if __name__ == '__main__':
    main()
