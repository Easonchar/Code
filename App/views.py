from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def index(request):
    return render(request,'index.html')


def detail(request):
    return render(request,'html/detail.html')


def list(request):
    return render(request,'html/list.html')


def login(request):
    return render(request,'html/login.html')


def register(request):
    return render(request,'html/register.html')


def shoppingCar(request):
    return render(request,'html/shoppingCar.html')