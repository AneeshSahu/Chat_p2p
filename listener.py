import socket
import threading


class Listener(threading.Thread):
    def __init__(self, port, host, buff):
        super().__init__()
        self.port = port
        self.host = host
        self.buff = buff

    def run(self):
        l_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        l_socket.bind((self.host, self.port))
        l_socket.listen(1)

        while True:
            connection, address = l_socket.accept()
            print("Established connection with: ", address)
            msg = connection.recv(self.buff)
            print("Them: ", msg)