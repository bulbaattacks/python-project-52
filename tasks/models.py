from django.db import models
from users.models import User
from statuses.models import Status
from labels.models import Label


class Task(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.PROTECT)
    assignee = models.ForeignKey(User, related_name='assignee', on_delete=models.PROTECT, blank=True)
    label = models.ManyToManyField(Label, blank=True)

    def __str__(self):
        return self.name
