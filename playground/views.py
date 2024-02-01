from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.


def welcome(request):
    return HttpResponse("Welcome to My Page")


def hello(request, name):
    return render(request, 'hello.html', context={'name': name})


def number(request, number):
    return HttpResponse(number)