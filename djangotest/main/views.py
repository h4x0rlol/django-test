import os
from main.tcp_handler import tcp_connect
from django.shortcuts import render
from .models import List
from django.core import serializers


TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
lists = List.objects.all()


def index(request):
    return render(request, 'main/index.html', {"lists": lists})


def send_data(request):
    if request.method == "GET":
        MESSAGE = "keklol".encode()
        con = tcp_connect(TCP_IP, TCP_PORT)
        con.send(MESSAGE)
        data = con.recv(BUFFER_SIZE)
        print("received data:", data)

    return render(request, 'main/index.html', {"lists": lists})
