from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def detail(request):
    return render(request,'detail.html')


def list(request):
    return render(request,'list.html')


def login(request):
    return render(request,'login.html')


def register(request):
    return render(request,'register.html')


def shoppingCar(request):
    return render(request,'shoppingCar.html')