import socket
from concurrent.futures import ThreadPoolExecutor
import logging
from .parser import KpResponse

logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s')
log = logging.getLogger()

IP = '0.0.0.0'
PORT = 8888


def create_server(ip, port):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((ip, port))
    server.listen(5)  # max backlog of connections
    return server


def handle_client_connection(client_socket):
    request = client_socket.recv(1024)
    log.info('Received %s', request)

    res = KpResponse()
    log.info('Sending: %s', res)
    client_socket.send(res.raw())
    client_socket.close()


def listen(ip=IP, port=PORT):
    log.info('Listening on %s:%s', ip, port)
    server = create_server(ip, port)
    with ThreadPoolExecutor() as pool:
        while True:
            client_sock, address = server.accept()
            log.info('Accepted connection from %s:%s', address[0], address[1])
            pool.submit(handle_client_connection, client_sock)


if __name__ == '__main__':
    log.info('hello, now!')
    listen()
