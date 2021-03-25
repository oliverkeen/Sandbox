from django.shortcuts import render
from django.http import HttpResponse

# Houses functions and classes that handle what data displays in HTML templates
# Create your views here.

def index(request):
    return HttpResponse("Hello, world! This is the polls app index.")
