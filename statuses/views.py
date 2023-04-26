from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from statuses.models import Status
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from statuses.forms import StatusForm


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/list_of_statuses.html"
    success_url = reverse_lazy('statuses_list')
    login_url = reverse_lazy('login')


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = StatusForm
    model = Status
    template_name = "statuses/edit.html"
    success_url = reverse_lazy('statuses_list')
    success_message = _("Status was created successfully")


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'statuses/edit.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("Status was updated successfully")


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'statuses/delete.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("Status was deleted successfully")
