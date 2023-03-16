from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def minhong(request):
    return HttpResponse("Hello Minhong!")

def greet(request, name):
    return HttpResponse(f"Hello {name.capitalize()}!")