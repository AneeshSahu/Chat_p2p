import socket
import threading

class Mouth(threading.Thread):
    def __init__(self,myname,myport):
        threading.Thread.__init__(self)
        self.myname = myname
        self.othername = None
        self.myport = myport
    def run(self):
        s = socket.socket()
        print("created")

        s.bind(('localhost',myport))
        s.listen(1)
        print("waiting")
        
        c,addr = s.accept()
        self.othername = c.recv(1024).decode()
        
        print("connected with", addr, self.othername)
        c.send(bytes("welcome to chat",'utf-8'))
        c.send(bytes(self.myname,'utf-8'))
            
        while True:
            msg = input(str(self.myname)+":")
            c.send(bytes(msg,'utf-8'))
    
class Ear(threading.Thread):
    def __init__(self,myname,otherport):
        threading.Thread.__init__(self)
        self.myname = myname
        self.othername = None
        self.otherport= otherport
    def run(self):
        c = socket.socket()
        while True:
            try:
                c.connect(('localhost',otherport))
                print("Established connection")
                break
            except:
                print("Trying to establish connection")
        c.send(bytes(self.myname,'utf-8'))
        
        print(c.recv(1024).decode())
        namethem= c.recv(1024).decode()
        while True:
            print(namethem,":",c.recv(1024).decode())
            
            
nameme = input("Username?")
myport = int(input("Which port should I host on?"))
otherport = int(input("Which port should I listen on?"))

s = Mouth(nameme,myport)

s.start()

c = Ear(nameme,otherport)

c.start()
