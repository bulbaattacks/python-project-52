from django.db import models


class Label(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now=True)
