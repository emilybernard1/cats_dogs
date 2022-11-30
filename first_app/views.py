from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# the index function is going to take in a request
def index(request):
    return HttpResponse('<h1>Why hello there</h1>')
