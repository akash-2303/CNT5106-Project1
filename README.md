# CNT5106-Project1

In this project we had to present a simple ftp client and server that can handle basic file transfer and operations like get and upload. The server can handle one client. 


# FTP Server

    This is a simple FTP server implemented in Python. It uses TCP sockets to send and receive files.

## Features

    - Send and receive files over a TCP connection
    - Supports large files by sending and receiving data in chunks
    - Uses the file size to ensure the entire file is sent and received

 ## Usage

1. Run the server script:
    python3 ftpserver.py


2. When prompted, enter the port number for the server to listen on. If you press ENTER without entering a number, the server will use the default port number (12000).

3. The server will start and wait for a client to connect. Once a client connects, it can send and receive files.

## Functions

- `receive_file(client_socket, filename)`: Receives a file from a client and writes it to a new file.
- `send_file(client_socket, filename)`: Sends a file to a client.
- `main()`: Starts the server and waits for clients to connect.

## Requirements

- Python 3
- A client that can send and receive files over a TCP connection

# FTP Client

This is a simple FTP client implemented in Python. It uses TCP sockets to send and receive files.

## Features

- Send and receive files over a TCP connection
- Supports large files by sending and receiving data in chunks
- Uses the file size to ensure the entire file is sent and received

## Usage

1. Run the client script:
python3 ftpclient.py


2. When prompted, enter the server's IP address and port number. If you press ENTER without entering a number, the client will use the default IP address (localhost) and port number (12000).

3. The client will connect to the server. Once connected, it can send and receive files.

## Functions

- `send_file(client_socket, filename)`: Sends a file to the server.
- `receive_file(client_socket, filename)`: Receives a file from the server and writes it to a new file.
- `main()`: Connects to the server and waits for user input to send or receive files.

## Requirements

- Python 3
- A server that can send and receive files over a TCP connection


