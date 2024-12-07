import socket
import threading

#proxy server configuration
proxy_host = '127.0.0.1'
proxy_port = 8888

#destination server configuration
dest_host = "google.com"
dest_port = 80

def handle_client(client_socket):
    #connect to destination server
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.connect((dest_host, dest_port))

    #forward data between client and server
    while True:
        #receive data from client
        client_data = client_socket.recv(4096)
        if len(client_data) == 0:
            break

        #forward data to the server
        server_socket.send(client_data)
    #close the connection
    client_socket.close()
    server_socket.close()

def start_proxy():
    #crete socket object
    proxy = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #bind the socket to a host and port
    proxy.bind((proxy_host, proxy_port))
    #listen for incoming connection
    proxy.listen()

    print(f"Proxy server listening on {proxy_host}: {proxy_port}")

    while True:
        client_socket, addr = proxy.accept()
        print(f"Accepted conection from {addr[0]} : {addr[1]}")

        #start a new thread to handle the client
        client_handle = threading.Thread(target=handle_client, args=(client_socket,))
        client_handle.start()

if __name__ == "__main__":
    start_proxy()