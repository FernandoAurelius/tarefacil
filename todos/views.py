from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from django.shortcuts import get_object_or_404, redirect

from django.contrib import messages

from django.utils import timezone

from todos.models import Todo


# Defini uma classe Mixin "OwnedMixin", que herda de "LoginRequiredMixin", e defini os métodos get_queryset e form_valid de maneira a não ter
# que repetir o código em todas as outras CBVs
class OwnedMixin(LoginRequiredMixin):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(owner=self.request.user)

    def check_ownership(self, obj):
        if obj.owner != self.request.user:
            messages.error(
                self.request, "Você não tem permissão para modificar esta tarefa."
            )
            return False
        return True

    def set_owner(self, form):
        form.instance.owner = self.request.user
        return form


class TodoListView(OwnedMixin, ListView):
    login_url = "accounts/login/"
    model = Todo


class TodoCreateView(OwnedMixin, CreateView):
    login_url = "accounts/login/"
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form = self.set_owner(form)
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


class TodoUpdateView(OwnedMixin, UpdateView):
    login_url = "accounts/login/"
    model = Todo
    fields = ["title", "deadline"]
    success_url = reverse_lazy("todo_list")

    def form_valid(self, form):
        form = self.set_owner(form)
        return super().form_valid(form)


class TodoDeleteView(OwnedMixin, DeleteView):
    login_url = "accounts/login/"
    model = Todo
    success_url = reverse_lazy("todo_list")

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.check_ownership(self.object):
            return redirect("todo_list")
        return super().post(request, *args, **kwargs)


class TodoCompleteView(View):
    login_url = "accounts/login/"

    def get(self, request, pk):
        todo = get_object_or_404(Todo, pk=pk, owner=request.user)
        todo.mark_has_complete()
        return redirect("todo_list")
