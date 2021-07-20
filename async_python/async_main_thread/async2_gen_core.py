'''
from time import time
# generators = function  with next()

def gen1(name):
    for it in name:
        yield it

# g = gen('Stas')


# def gen_filename():
#     while True:
#         pattern = 'file {}.jpeg'
#         t = int(time() * 1000)
#         yield pattern.format(str(t))
#         # вызовется следующим после next
#         yield 'STAS'
#         yield 'STASEN'
#         yield 'STASEEEEK'



def gen2(num):
    for item_num in range(num):
        yield item_num


g1 = gen1('stas')
g2 = gen2(4)


tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)
    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass
'''




import socket
from select import select
# domain:5000

# socket.AF_INET - IP версии 4, socket.SOCK_STREAM - поддержка протокола TCP
tasks = []

to_read = {}
to_write = {}

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # серверный сокет привязан к порту
    server_socket.bind(('localhost', 5000))
    server_socket.listen()

    while True:
        yield ('read', server_socket)

        print('before accept()')
        client_socket, addr = server_socket.accept()
        print('has connection, catched client socket')
        tasks.append(client(client_socket))

def client(client_socket):
    while True:
        yield ('read', client_socket)

        request = client_socket.recv(4096)
        if not request:
            break
        else:
            response = 'Hello, World!\n'.encode()
            yield ('write', client_socket)
            client_socket.send(response)
    print('')
    client_socket.close()

def event_loop():
    while any([tasks, to_read, to_write]):
        while not tasks:
            ready_to_read, read_to_write, _ = select(to_read, to_write, [])

            for sock in ready_to_read:
                tasks.append(to_read.pop(sock))

            for sock in read_to_write:
                tasks.append(to_write.pop(sock))

        try:
            task = tasks.pop(0)
            reason, sock = next(task)
            if reason == 'read':
                to_read[sock] = task
            if reason == 'write':
                to_write[sock] = task
        except StopIteration:
            print('All done')

tasks.append(server())
event_loop()
