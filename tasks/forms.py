from django.forms import ModelForm
from django import forms
from .models import Task
from django.utils.translation import gettext_lazy as _
from labels.models import Label


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee', 'label']
        labels = {
            "name": _("Name"),
            "description": _("Description"),
        }

