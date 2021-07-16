from main.utils.TCPHandler import TCPHandler
from django.shortcuts import render
from .models import List

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
lists = List.objects.all()


def index(request):
    return render(request, 'main/index.html', {"lists": lists})


def send_data(request):
    if request.method == "GET":
        MESSAGE = "keklol".encode()
        connection = TCPHandler(TCP_IP, TCP_PORT, BUFFER_SIZE)
        connection.connect()
        connection.send(MESSAGE)
        data = connection.receive()
        print("received data:", data)

    return render(request, 'main/index.html', {"lists": lists})
