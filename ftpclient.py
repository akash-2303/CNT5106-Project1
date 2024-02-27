import socket
import os

SERVER_IP = '127.0.0.1'
SERVER_PORT = 12000
BUFFER_SIZE = 1024

def receive_file(client_socket, filename):
    with open("new"+filename, 'wb') as file:
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
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect((SERVER_IP, SERVER_PORT))
        print('Connected to server')
    except Exception as e:
        print('Error in connecting to server:', e)
        return
    
    while client_socket:
        try:
            cmd = input('Enter command: ')
            if cmd.startswith("get"):
                client_socket.send(cmd.encode())
                filename = cmd.split()[1]
                receive_file(client_socket, filename)
                print('File downloaded successfully')
            elif cmd.startswith("put"):
                client_socket.send(cmd.encode())
                filename = cmd.split()[1]
                send_file(client_socket, filename)
                print('File uploaded successfully')
            elif cmd == 'quit':
                client_socket.send(cmd.encode())
                break
            else:
                print('Invalid command')
        except Exception as e:
            print('Error:', e)
            break

    client_socket.close()

if __name__ == '__main__':
    main()