from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def indexPageView(request) :
    return HttpResponse('Payment Page')

def rentalPageView(request) :
    return HttpResponse('Rental Page')