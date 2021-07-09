from django.shortcuts import render
from .models import List
import socket
from django.core import serializers


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
# MESSAGE = "Hello, World!".encode()
lists = List.objects.all()


def index(request):
    return render(request, 'main/index.html', {"lists": lists})


def send_data(request):
    if request.method == "GET":
        MESSAGE = serializers.serialize("xml", lists).encode()
        print(MESSAGE)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((TCP_IP, TCP_PORT))
        s.send(MESSAGE)
        data = s.recv(BUFFER_SIZE)
        s.close()
        print("received data:", data)
    return render(request, 'main/index.html', {"lists": lists})
