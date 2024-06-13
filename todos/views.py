from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404, redirect

from django.utils import timezone

from todos.models import Todo


class TodoListView(ListView):
    model = Todo


class TodoCreateView(CreateView):
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


class TodoUpdateView(UpdateView):
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")


class TodoDeleteView(DeleteView):
    model = Todo
    success_url = reverse_lazy("todo_list")


class TodoCompleteView(View):
    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk)
        todo.mark_has_complete()
        return redirect("todo_list")
