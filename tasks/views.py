from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from tasks.models import Task
from tasks.forms import TaskForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect


class TasksListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = "tasks/list_of_tasks.html"
    # success_url = reverse_lazy('tasks_list')


class TaskCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/edit.html"
    success_url = reverse_lazy('tasks_list')
    success_message = _("Task was created successfully")

    def form_valid(self, form):
        """If the form is valid, add creator of the task and save the associated model."""
        form.instance.creator = self.request.user
        self.object = form.save()
        return super().form_valid(form)


class TaskUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = "tasks/edit.html"
    success_url = reverse_lazy('tasks_list')
    success_message = _("Task was updated successfully")


class TaskDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    success_url = reverse_lazy('tasks_list')
    success_message = _("Task was deleted successfully")
