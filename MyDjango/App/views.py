from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')


def detail(request):
    return None


def list(request):
    return None


def login(request):
    return None


def register(request):
    return None


def shoppingCar(request):
    return None