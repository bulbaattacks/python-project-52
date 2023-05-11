from django.forms import ModelForm
from .models import Task
from django.utils.translation import gettext_lazy as _


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'description', 'status', 'assignee', 'label']
        labels = {
            "name": _("Name"),
            "description": _("Description"),
            "status": _("Status"),
            "assignee": _("Assignee"),
            "label": _("Label"),
        }
