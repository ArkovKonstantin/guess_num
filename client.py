import socket

HOST = 'localhost'
PORT = 8000
with socket.socket() as s:
    s.connect((HOST, PORT))
    print(f'Connect to {HOST}:{PORT}')
    try:
        while True:
            cmd = input().split()
            if cmd[0] == 'exit':
                    s.send(cmd[0].encode('utf-8'))
                    break
            elif cmd[0] == 'guess':
                if len(cmd) == 2 and cmd[1].isdigit():
                    s.send(cmd[1].encode('utf-8'))
                    res = s.recv(1024).decode('utf-8')
                    print(res)
                    if res == "correct" or res == 'lose':
                        break
                else:
                    print('Wrong format')
            else:
                print('Wrong cmd')
    except KeyboardInterrupt:
        s.send('exit'.encode('utf-8'))
        print()

print(f'Disconnect from {HOST}:{PORT}')

            
     
        