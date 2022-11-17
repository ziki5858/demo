import socket
import random

LENGTH = 4


def main():
    while True:
        if 'nextPort' in locals():
            nextPort = client(nextPort)
        else:
            nextPort = client(8820)
        if nextPort is not None:
            nextPort = server(nextPort)
        else:
            break


def server(nextPort):
    server_socket = socket.socket()
    server_socket.bind(("0.0.0.0", int(nextPort)))
    server_socket.listen()
    print("side s listening to port: " + str(nextPort))
    (client_socket, client_address) = server_socket.accept()
    while True:
        length = client_socket.recv(LENGTH).decode()
        message = client_socket.recv(int(length)).decode()
        if message == "EXIT":
            client_socket.send("EXIT".encode())
            client_socket.close()
            server_socket.close()
            return "EXIT"
        else:
            print("sideC send: " + message)
            newPort = random.randint(5550, 8820)
            client_socket.send(make_massage(str(newPort)).encode())
            return newPort
        break


def make_massage(mes):
    length = str(len(mes))
    message = length.zfill(LENGTH) + mes
    print(message)
    return message


def handle_server_response(my_socket):
    length = my_socket.recv(LENGTH).decode()
    message = my_socket.recv(int(length)).decode()
    print("The server sent:\n" + message)
    return message


def client(newPort):
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", int(newPort)))
    while True:
        inPut = input('Insert a message\n')
        my_socket.send(make_massage(inPut).encode())
        if inPut == "EXIT":
            my_socket.close()
            break
        my_socket.send("EXIT".encode())
        return handle_server_response(my_socket)


if __name__ == "__main__":
    main()
