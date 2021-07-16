import socket


class TCPHandler:
    con = None

    def __init__(self, TCP_IP, TCP_PORT, BUFFER_SIZE):
        self.TCP_IP = TCP_IP
        self.TCP_PORT = TCP_PORT
        self.BUFFER_SIZE = BUFFER_SIZE

    def connect(self):
        con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        con.connect((self.TCP_IP, self.TCP_PORT))
        self.con = con

    def send(self, message):
        self.con.send(message)

    def receive(self):
        return self.con.recv(self.BUFFER_SIZE)
