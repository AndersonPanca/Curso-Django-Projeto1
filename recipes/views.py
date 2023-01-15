from django.http import HttpResponse
from django.shortcuts import render


def Home(request):
    return render(request, 'recipes/home.html')


def Contato(request):
    return render(request, 'temp.html')


def Sobre(request):
    return HttpResponse('sobre')
