import socket
import time

HOST = "127.0.0.1"
PORT = 61651

if __name__ == '__main__':
    socket = socket.socket()
    socket.bind((HOST, PORT))
    socket.listen()
    print("Listening to {}:{}".format(HOST, PORT))
    conn, addr = socket.accept()
    print("Connected with {}".format(addr))
    for i in range(1,6):
        conn.send("This is message #{}\n".format(i).encode())
        time.sleep(1)
    conn.close()
    print("Connection closed")