# для установки соединения между клиентом и сервером
# по протоколу tcp/ip используем библиотеку socket
import socket


def parse_request(request_text):
    parsed_text = request_text.split(' ')
    method_name = parsed[0]
    url = parsed[1]

    return method_name, url


def generate_headers(method: str, url: str):
    if method != 'GET':
        return ('HTTP/1.1 405 Method not allowed\n\n', 405)


def generate_response(request: str):
    method, url = parse_request(request)
    headers, code = generate_headers(method, url)




def run():
    # клиент - тот, кто делает запрос
    # сервер - будет обрабатывать response и возвращать ответ
    # socket.AF  - address family
    # INET - протокол ip 4 версии
    # INET6 - протокол ip 6 версии
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # связываем объект с конкретным клиентом
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        client_socket, addr = server_socket.accept()
        request = client_socket.recv(1024)
        print(request, '\n', addr)
        response = generate_response(request.decode('utf-8'))

        client_socket.sendall('Hello, World!'.encode())
        client_socket.close()


# если происходит самостоятельный запуск файла с консоли
if __name__ == '__main__':
    run()
