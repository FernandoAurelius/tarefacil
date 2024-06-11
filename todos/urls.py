from django.urls import path

from todos.views import TodoListView, TodoCreateView, TodoUpdateView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("create_view", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
]
