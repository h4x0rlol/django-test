from main.utils.XMLHandler import XMLHandler
from main.utils.TCPHandler import TCPHandler
from django.shortcuts import render
from .models import List

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
lists = List.objects.all()


# Tests
test_data1 = {
    "id": 11055,
    "type": "log",
    "messageType": 1,
    'messageText': '[09.07.21 17:07:44.305] rpcManagementServer : Входящее подключение от 192.168.0.143:45022'
}

test_data2 = {
    "id": 12480,
    "type": "version",
    "value": 0.1
}

test_data3 = {
    "id": 90769,
    "type": "linkState",
    "bandwidth": 0,
    'direction': 0,
    'progress': 0,
    'stage': 1
}

server_response = XMLHandler().build(test_data3).decode(encoding="utf-8")


def index(request):
    return render(request, 'main/index.html', {"test_data": server_response})


def send_data(request):
    if request.method == "GET":
        xml = XMLHandler()
        message = xml.build(test_data1)

        builded = message.decode(encoding="utf-8")

        print('Builded message\n\n')
        print(builded)
        print('\n\n')

        parsed_message = xml.parse(server_response)

        print('Parsed message\n\n')
        print(parsed_message)
        print('\n\n')

        # connection = TCPHandler(TCP_IP, TCP_PORT, BUFFER_SIZE)
        # connection.connect()
        # connection.send(builded.encode())
        # data = connection.receive()
        # print("received data:", data)

    return render(request, 'main/index.html', {"test_data_builded": builded, "parsed_data": parsed_message})
