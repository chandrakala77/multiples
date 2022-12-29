from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def htmlfile(request):
    return HttpResponse('This is my htmlfile')
