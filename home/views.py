from django.shortcuts import render,redirect
from django.http import HttpResponse

def app(req):
    return render(req,'test.html')