import socket

SERVER_PORT = 12000
BUFFER_SIZE = 1024

def receive_file(client_socket, filename):
    with open("new" + filename, 'wb') as file:
        while True:
            data = client_socket.recv(BUFFER_SIZE)
            if data == b'END':
                break
            file.write(data)

def send_file(client_socket, filename):
    with open(filename, 'rb') as file:
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                client_socket.send(b'END')
                break
            client_socket.send(data)

def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', SERVER_PORT))
    server_socket.listen(5)
    print('Server is ready to receive')

    while True:
        client_socket, addr = server_socket.accept()
        print('Connected to', addr)

        while client_socket:
            try:
                cmd = client_socket.recv(BUFFER_SIZE).decode()
                if cmd.startswith("get"):
                    filename = cmd.split()[1]
                    send_file(client_socket, filename)
                    print('File sent successfully')
                elif cmd.startswith("put"):
                    filename = cmd.split()[1]
                    receive_file(client_socket, filename)
                    print('File received successfully')
                elif cmd == 'quit':
                    break
                else:
                    print('Invalid command')
            except Exception as e:
                print('Error:', e)
                break

if __name__ == '__main__':
    main()