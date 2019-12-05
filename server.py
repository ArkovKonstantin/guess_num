import socket
import random

HOST = ''
PORT = 8000
NUM = random.randint(1, 10)
TRIES_NUM = 10

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print("start server on port ", PORT)
    while True:
        try:
            conn, addr = s.accept()
            count = 0
            with conn:
                print('Connected by ', addr)
                while True:
                    data = conn.recv(1024).decode('utf-8')
                    print(data)
                    if data == 'exit':
                        break
                    arg = int(data)
                    count += 1
                    if arg > NUM:
                        conn.send(b'less')
                    elif arg < NUM:
                        conn.send(b'more')
                    elif arg == NUM:
                        conn.send(b'correct')
                        break
                    if count > TRIES_NUM:
                        conn.send(b'lose')
                        break

            print('Disconnected by ', addr)
        except KeyboardInterrupt:
            print()
            print('Stop server')
            break
