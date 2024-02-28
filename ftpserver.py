import socket
import os

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
        file_size = os.path.getsize(filename)
        client_socket.send(str(file_size).encode())
        while True:
            data = file.read(BUFFER_SIZE)
            if not data:
                break
            client_socket.send(data)


def main():
    port_input = input("Enter the port number or press ENTER to use default port number(12000): ")
    server_port = int(port_input) if port_input else SERVER_PORT

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', int(server_port)))
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
                elif cmd.startswith("upload"):
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