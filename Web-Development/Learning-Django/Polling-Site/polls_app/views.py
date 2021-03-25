from django.shortcuts import render
from django.http import HttpResponse

# Houses functions and classes that handle what data displays in HTML templates
# Create your views here.

def index(request):
    return HttpResponse("Hello, world! This is the polls app index.")

def detail(request, question_id):
    return HttpResponse("This is question %s." % question_id)

def results(request, question_id):
    response = "These are the results of question %s."

    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)