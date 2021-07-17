import socket
from views import *
# Protocol HTTP is TCP/IP

# https://www.youtube.com/watch?v=4haMUvUxUJI&t=0s
# sockets works with http
# and based with tcp Transmission Control Protocol   track PORT
# port is using for opening different connection with TCP by one computer
# (helps keep order for receiving and sending packages)
# if no packages it doing reponse again and etc.

# and ip (main part of protocol is IP-address) 4 parts with 1 byte for part
# there is connection between hosts and uses packages with data

# pair IP address and port is Socket
# socket is a bridge between client and server
# There is two types of socket
# 1. client socket
# 2. server socket

URLS = {
    '/': index,
    '/blog': blog
}


def parse_request(request):
    parsed = request.split(' ')
    method = parsed[0]
    url = parsed[1]
    return method, url


def generate_headers(method, url):
    if not method == 'GET':
        return ('http/1.1 405 Method not allowed\n\n', 405)
    if not url in URLS:
        return ('http/1.1 404 Not found\n\n', 404)

    return ('http/1.1 200 All Ok!\n\n', 200)


def generate_content(code, url):
    if code == '404':
        return '<h1>404</h1><p>Not Found =*(</p>'
    elif code == '405':
        return '<h1>405</h1><p>Method not allowed =(</p>'
    return URLS.get(url)()

def generate_response(request):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)
    body = generate_content(code, url)
    return (headers + body).encode()

# describing server part
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# по какому адресу должны придти пакеты
server_socket.bind(('localhost', 5000))
# входи в режим прослушивания и ожидания получения пакетов
server_socket.listen()


while True:
    print('Before .accept()')
    # receiving response by client
    client_socket, address = server_socket.accept()

    # if accept works it means that response made
    print('Connection from', address)


    request = client_socket.recv(1024)
    # print(request.decode('utf-8'))
    print(request)
    print()
    print(address)
    response = generate_response(request.decode())
    # сервер возвращает клиенту что-то - методы send и sendall
    client_socket.sendall(response)
    client_socket.close()
    # while True:
    #     print('Before .recv()')
    #     # receiving all bytes by client. it is address
    #     request = client_socket.recv(4096)
    #
    #     if not request:
    #         break
    #     else:
    #         response = 'hello world\n'.encode()
    #         client_socket.send(response)
    #
    # print('outside client while loop')
    # client_socket.close()
