from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from tasks.models import Task
from tasks.forms import TaskForm
from django.utils.translation import gettext_lazy as _
from django_filters.views import FilterView
from .filters import TaskFilter


class TasksListView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = "tasks/list_of_tasks.html"
    context_object_name = 'tasks'
    filterset_class = TaskFilter
    login_url = 'login'
    extra_context = {"title": _("Tasks")}


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "edit.html"
    success_url = reverse_lazy('tasks_list')
    success_message = _("Task was created successfully")
    extra_context = {"title": _("Create task"),
                     "button": _("Create")
                     }

    def form_valid(self, form):
        """If the form is valid, add creator of the task and save the associated model."""
        form.instance.creator = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "edit.html"
    success_url = reverse_lazy('tasks_list')
    success_message = _("Task was updated successfully")
    extra_context = {"title": _("Edit the task"),
                     "button": _("Update")
                     }


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "delete.html"
    success_url = reverse_lazy('tasks_list')
    success_message = _("Task was deleted successfully")
    extra_context = {"title": _("Delete the task"),
                     "button": _("Yes, delete")}


class TaskDetailView(LoginRequiredMixin, SuccessMessageMixin, DetailView):
    model = Task
    template_name = "tasks/detail.html"
    extra_context = {"title": _("View the task")}
