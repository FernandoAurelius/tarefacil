from django.db import models

from datetime import date

from django.conf import settings


class OwnedModel(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Todo(OwnedModel, models.Model):
    title = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    created_at = models.DateField(auto_now_add=True, null=False, blank=False)
    deadline = models.DateField(verbose_name="Prazo final", null=False, blank=False)
    finished_at = models.DateField(null=True)

    class Meta:
        ordering = ["deadline"]

    def mark_has_complete(self):
        if not self.finished_at:
            self.finished_at = date.today()
            self.save()
