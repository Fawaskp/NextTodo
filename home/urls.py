from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('add-todo-task',views.add_todo_task,name="add_todo_task"),
    path('delete-todo-task',views.del_todo_task,name="del_todo_task"),
]
