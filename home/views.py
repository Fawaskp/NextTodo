from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from .models import Tasks



def home(request):
    session_id = request.COOKIES.get('sessionid')
    tasks=[]

    tasks = Tasks.objects.filter(session_id=session_id)
    return render(request,'test.html',{'tasks':tasks})


def add_do_task(request):

    if request.method == 'POST':
        session_id = request.COOKIES.get('sessionid')
        todo_task = request.POST['todo_task']
        Tasks.objects.create(session_id=session_id,do_task=todo_task)
        return redirect(home)

    return HttpResponse('Request Failed! Unauthorised Access')