from django.shortcuts import render

from django.http import HttpRequest

from todos.models import Todo

def todo_list(request: HttpRequest):
    context = Todo.objects.all()
    return render(request, "todos/todo_list.html", {"todos": context})
