import asyncio
import socket
from time import time


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
            print(f'[INFO] - New connection from {addr}\n')
            loop.create_task(receive_massage(client_socket))
            # loop.create_task(send_massage(client_socket))
        except BlockingIOError:
            await asyncio.sleep(0.05)
        # loop.create_task(inner_function('Ivan'))


async def send_massage(client_socket, massage):
    pass


async def receive_massage(client_socket):
    client_socket.setblocking(False)

    while True:
        try:
            request = client_socket.recv(1024)
            if request == b'\n':
                continue

            if request:
                print(f'[{client_socket.getpeername()[-1]}] - {request.decode().strip()}')
            else:
                print(f'[INFO] - Client from {client_socket.getpeername()} was disconnected\n')
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
