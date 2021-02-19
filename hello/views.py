from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def harshi(request):
    return HttpResponse("hello, harshi!")


'''
def greet(request, name):
    return HttpResponse(f"hello, {name.capitalize()}!")
'''

# in order to let html access variarble like name(as key, value pair)
def greet(request, name):
    return render(request, "hello/greet.html", {
        "name": name.capitalize()})
