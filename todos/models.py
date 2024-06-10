from django.db import models


class Todo(models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Prazo final", null=False, blank=False)
    finished_at = models.DateField(null=True)
