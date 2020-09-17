import socket
import time

HOST = "127.0.0.1"
PORT = 6165

1
def protocolHandlers(conn, req):
    if "GET" in req:
        conn.send("ANSWER".encode())


if __name__ == '__main__':
    socket = socket.socket()
    socket.bind((HOST, PORT))
    socket.listen()
    print("Listening to {}:{}".format(HOST, PORT))
    conn, addr = socket.accept()
    print("Connected with {}".format(addr))
    reply = conn.recv(4096)
    protocolHandlers(conn, reply.decode())
    conn.close()
    print("Connection closed")
