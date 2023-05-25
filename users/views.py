from django.shortcuts import redirect
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from users.models import User
from users.forms import UserForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from .mixins import UserPermissionCustomMixin
from django.db.models import ProtectedError


class UsersListView(ListView):
    model = User
    template_name = "users/list_of_users.html"
    extra_context = {"created_at": timezone.now()}


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    model = User
    template_name = "edit.html"
    success_url = reverse_lazy("login")
    success_message = _("User was created successfully")
    extra_context = {"title": _("Registration"),
                     "button": _("Registrate")
                     }


class UserUpdateView(UserPermissionCustomMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'edit.html'
    success_url = reverse_lazy('users_list')
    success_message = _("User was updated successfully")
    extra_context = {"title": _("Edit the user"),
                     "button": _("Update")
                     }


class UserDeleteView(UserPermissionCustomMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'delete.html'
    success_url = reverse_lazy('users_list')
    success_message = _("User was deleted successfully")
    extra_context = {"title": _("Delete the user"),
                     "button": _("Yes, delete")
                     }

    def post(self, request, *args, **kwargs):
        try:
            self.delete(request, *args, **kwargs)
            messages.success(self.request, _("User was deleted successfully"))
        except ProtectedError:
            messages.add_message(request, messages.ERROR,
                                 _("Can't delete the user because it's used for the task"))
        return redirect(reverse_lazy('users_list'))
