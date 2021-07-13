import socket


def tcp_connect(TCP_IP, TCP_PORT):
    con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    con.connect((TCP_IP, TCP_PORT))
    return con
