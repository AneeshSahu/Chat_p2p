import threading

class Sender(threading.Thread):
    def __init__(self,address,port):
        super().__init__(self)
        self.address = address
        self.port = port

    def run(self):
        socketout = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketout.connect((self.address, self.port))

        while True:
            message = input("user 1: ")
            if message.lower() == "quit" or message.lower() == "exit":
                break
            else:
                try:
                    socketout.sendall(message)
                except:
                    Exception
