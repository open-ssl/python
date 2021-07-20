import socket
# domain:5000

# socket.AF_INET - IP версии 4, socket.SOCK_STREAM - поддержка протокола TCP

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# серверный сокет привязан к порту
server_socket.bind(('localhost', 5000))
server_socket.listen()

while True:
    print('before accept()')
    client_socket, addr = server_socket.accept()
    print('has connection, catched client socket')
    while True:
        print('before recv')
        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = 'Hello, World!\n'.encode()
    print('')
    client_socket.close()
