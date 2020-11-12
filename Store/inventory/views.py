from django.shortcuts import render
from django.http import HttpResponse

def indexPageView(request) :
    return HttpResponse('Hello Nefi, Welcome to the Home Page!') 
# Create your views here.
