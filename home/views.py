from django.shortcuts import render
from django.http import HttpResponse

def app(req):
    return HttpResponse('hello world')
