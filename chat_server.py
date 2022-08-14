import asyncio
import re
import socket
from time import time

clients = {}


class TCPServerSocket:
    def __init__(self, addr, queue):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind(addr)
        self.server_socket.setblocking(False)
        self.server_socket.listen(queue)


server_port = 8000
server_socket = TCPServerSocket(('0.0.0.0', server_port), 2).server_socket


async def accept_connection(server_socket):
    loop = asyncio.get_running_loop()
    while True:
        try:
            client_socket, addr = server_socket.accept()
            client_name = client_socket.recv(1024).decode().strip()
            clients[client_name] = client_socket

            print(f'[INFO] - {client_name} connected\n')

            loop.create_task(receive_massage(client_name))

        except BlockingIOError:
            await asyncio.sleep(0.00)


async def send_massage(request, sender):
    try:
        recipient = re.search(r'^(\w+)', request).group(0)
    except AttributeError:
        return

    massage = re.sub(r'^(\w+\s)', '', request)
    try:
        client = clients[recipient]
        client.send(f'{sender} > {massage}\n'.encode())
    except KeyError:
        pass


async def receive_massage(client_name):
    client_socket = clients[client_name]
    client_socket.setblocking(False)

    while True:
        try:
            request = client_socket.recv(1024)
            if request == b'\n':
                continue

            if request:
                request = request.decode().strip()
                print(f'[{client_name}] - {request}')

                asyncio.get_running_loop().create_task(send_massage(request, client_name))

            else:
                print(f'[INFO] - {client_name} disconnected\n')
                clients.pop(client_name)
                client_socket.close()
                break
        except BlockingIOError:
            continue
        finally:
            await asyncio.sleep(0.00)


async def main():
    with server_socket:
        task = asyncio.create_task(accept_connection(server_socket), name='accept_function')
        await task


if __name__ == '__main__':
    t0 = time()
    print(f'[STARTED] - Server is running on 127.0.0.1:{server_port}\n')
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print(f'\n[STOPPED] - The server worked {(time() - t0):.2f} seconds')
