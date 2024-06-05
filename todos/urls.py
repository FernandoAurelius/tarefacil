from django.urls import path

from todos.views import todo_list

urlpatterns = [
    path('', todo_list, name="todo")
]