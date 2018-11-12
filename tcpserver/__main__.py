import socket
from concurrent.futures import ThreadPoolExecutor
from . import parser
from . import log
from .notify import monitor

IP = '0.0.0.0'
PORT = 8888

monitor("server up")

def create_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(20)  # max backlog of connections
    return server


def handle_client_connection(client_socket):
    try:
        request = parser.KpReceive(client_socket)
        monitor('Received %s', request)

        res = parser.KpResponse()
        monitor('Sending: %s', res)
        client_socket.send(res.raw())
        client_socket.close()
    except Exception as ex:
        monitor('crashed %s', ex)


def listen(ip=IP, port=PORT):
    server = create_server(ip, port)
    with ThreadPoolExecutor() as pool:
        while True:
            client_sock, address = server.accept()
            monitor('Accepted connection from %s:%s', address[0], address[1])
            pool.submit(handle_client_connection, client_sock)


if __name__ == '__main__':
    log.info('hello, now!')
    try:
        listen()
    except Exception as ex:
        log.exception('tcp server error %s', ex)
        monitor('crashed %s', ex)
