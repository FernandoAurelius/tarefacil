from django.urls import path

from todos.views import (
    TodoListView,
    TodoCreateView,
    TodoUpdateView,
    TodoDeleteView,
    TodoCompleteView,
)

urlpatterns = [
    path("list", TodoListView.as_view(), name="todo_list"),
    path("create_view", TodoCreateView.as_view(), name="todo_create"),
    path("update/<int:pk>", TodoUpdateView.as_view(), name="todo_update"),
    path("delete/<int:pk>", TodoDeleteView.as_view(), name="todo_delete"),
    path("complete/<int:pk>", TodoCompleteView.as_view(), name="todo_complete"),
]
