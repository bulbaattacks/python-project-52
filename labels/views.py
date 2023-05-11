from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from labels.models import Label
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from labels.forms import LabelForm
from tasks.models import Task
from django.contrib import messages
from django.http import HttpResponseRedirect


class LabelsListView(LoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/list_of_labels.html"
    success_url = reverse_lazy("labels_list")


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    form_class = LabelForm
    model = Label
    template_name = "labels/edit.html"
    success_url = reverse_lazy("labels_list")
    success_message = _("Label was created successfully")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Create label")
        context["button"] = _("Create")
        return context


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = "labels/edit.html"
    success_url = reverse_lazy("labels_list")
    success_message = _("Label was updated successfully")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Edit the label")
        context["button"] = _("Update")
        return context


class LabelDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    success_url = reverse_lazy("labels_list")

    def post(self, request, *args, **kwargs):
        label_id = kwargs.get('pk')
        if Task.objects.filter(labels=label_id):
            messages.add_message(request, messages.ERROR, _("Can't delete the label because it's used for the task"))
            return HttpResponseRedirect(reverse_lazy('labels_list'))
        messages.add_message(request, messages.SUCCESS, _("Label was deleted successfully"))
        return self.delete(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = _("Delete the label")
        return context


