from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.sessions.models import Session
from .models import Tasks
from django.contrib.sessions.backends.db import SessionStore
import uuid

def create_user_session(request, user_id):
    session = SessionStore()
    session['user_id'] = str(user_id)
    session.create()
    request.session = session
    return user_id

def home(request):
    user_id = request.session.get('user_id')
    tasks=[]

    tasks = Tasks.objects.filter(user_id=user_id)
    return render(request,'test.html',{'tasks':tasks})


def add_todo_task(request):

    if request.method == 'POST':

        user_id = request.session.get('user_id')
        if not user_id:
            user_id = create_user_session(request,uuid.uuid4())

        print('user id = ',user_id)
        todo_task = request.POST['todo_task']
        Tasks.objects.create(user_id=user_id,do_task=todo_task)
        return redirect(home)

    return HttpResponse('Request Failed! Unauthorised Access')

def del_todo_task(request):

    if request.method == 'POST':
        id = request.POST['task_id']
        Tasks.objects.get(id=id).delete()
        return redirect(home)

    return HttpResponse('Request Failed! Unauthorised Access')
