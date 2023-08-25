# Importing Libraries
import threading
import socket
# Starting Server
host = "192.168.6.110"
port = 14438
# Creating a socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Tell the server to listen on the given port and host
server.bind((host, port))
# Server is listening
server.listen()
# Creating lists of clients connected to the server
clients = []
# Create a list of clients connected username
usernames = []

# Create a function that broadcasts messages
def broadcast(message):
    for client in clients:
        client.send(message)

# Function to handle client's connections
def handle_client(client):
    # Endless loop until recv messages
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)

        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            username = usernames[index]
            broadcast(f'{username} has left the chat room!'.encode('utf-8'))
            usernames.remove(username)
            show_username = str(usernames)
            show_clients = str(len(clients))
            broadcast(show_username.encode('utf-8'))
            broadcast(show_clients.encode('utf-8'))
            break

# Main function to receive the clients connection
def receive():
    # Endless connection to server client
    while True:
        try:
            print('Server is running and listening ...')

            client, address = server.accept()
            print(f'connection is established with {str(address)}')
            
            show_username = str(usernames)

            broadcast(show_username.encode('utf-8'))

            client.send('username?'.encode('utf-8'))
            username = client.recv(1024)
            usernames.append(username)

            clients.append(client)
            print(f'The username of this client is {username}'.encode('utf-8'))

            broadcast(
                f'{username} has connected to the chat room'.encode('utf-8'))
            client.send('you are now connected!'.encode('utf-8'))

            thread = threading.Thread(target=handle_client, args=(client,))
            thread.start()
        except Exception as e:
            print(e)
            continue


# if __name__ == '__main__': syntax
if __name__ == "__main__":
    receive()
