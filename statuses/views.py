from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from statuses.models import Status
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from tasks.models import Task
from django.contrib import messages
from django.http import HttpResponseRedirect


class StatusesListView(LoginRequiredMixin, ListView):
    model = Status
    template_name = "statuses/list_of_statuses.html"
    success_url = reverse_lazy('statuses_list')


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    fields = ['name']
    template_name = "edit.html"
    success_url = reverse_lazy('statuses_list')
    success_message = _("Status was created successfully")
    extra_context = {"title": _("Create status"),
                     "button": _("Create")
                     }


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    fields = ['name']
    template_name = 'edit.html'
    success_url = reverse_lazy('statuses_list')
    success_message = _("Status was updated successfully")
    extra_context = {"title": _("Edit the status"),
                     "button": _("Update")
                     }


class StatusDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Status
    template_name = 'delete.html'
    success_url = reverse_lazy('statuses_list')
    extra_context = {"title": _("Delete the status"),
                     "button": _("Yes, delete")
                     }

    def post(self, request, *args, **kwargs):
        status_id = kwargs.get('pk')
        if Task.objects.filter(status=status_id):
            messages.add_message(request, messages.ERROR,
                                 _("Can't delete the status because it's used for the task"))
            return HttpResponseRedirect(reverse_lazy('statuses_list'))
        messages.add_message(request, messages.SUCCESS, _("Status was deleted successfully"))
        return self.delete(request, *args, **kwargs)
