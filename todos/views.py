from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404, redirect

from django.contrib import messages

from django.utils import timezone

from todos.models import Todo

class TodoListView(LoginRequiredMixin, ListView):
    login_url = "accounts/login/"
    model = Todo

class TodoCreateView(LoginRequiredMixin, CreateView):
    login_url = "accounts/login/"
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        deadline = form.cleaned_data.get("deadline")
        if deadline < timezone.now().date():
            today = timezone.now().date()
            today = today.strftime("%d/%m/%Y")
            form.add_error(
                "deadline",
                f"O prazo de entrega precisa ser igual ou superior à data de hoje ({today}).",
            )
            return self.form_invalid(form)
        return super().form_valid(form)

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    login_url = "accounts/login/"
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "accounts/login/"
    model = Todo
    success_url = reverse_lazy("todo_list")

class TodoCompleteView(View):
    login_url = "accounts/login/"
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
