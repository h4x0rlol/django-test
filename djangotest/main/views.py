from django.shortcuts import render
from .models import List


def index(request):
    lists = List.objects.all()
    return render(request, 'main/index.html', {"lists": lists})
