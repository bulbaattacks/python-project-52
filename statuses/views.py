from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from statuses.models import Status
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from statuses.forms import StatusForm
from tasks.models import Task
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from django.db.models import ProtectedError
from django.http import HttpResponseRedirect


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/list_of_statuses.html"
    success_url = reverse_lazy('statuses_list')


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    model = Status
    template_name = "statuses/edit.html"
    success_url = reverse_lazy('statuses_list')
    success_message = _("Status was created successfully")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Create status")
        return context


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/edit.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("Status was updated successfully")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Edit the status")
        return context


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("Status was deleted successfully")

    def post(self, request, *args, **kwargs):
        if Task.objects.filter(id__gt=0):
            messages.add_message(request, messages.ERROR, _("Can't delete the status because it's used for the task"))
            return HttpResponseRedirect(reverse_lazy('statuses_list'))
        return self.delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Delete the status")
        return context


