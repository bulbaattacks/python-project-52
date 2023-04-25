from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from users.models import User
from users.forms import UserForm
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UsersListView(ListView):
    model = User
    # context_object_name = "users"
    template_name = 'users/list_of_users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["created_at"] = timezone.now()
        return context


class UserCreateView(SuccessMessageMixin, CreateView):
    form_class = UserForm
    model = User
    template_name = 'users/edit.html'
    success_url = reverse_lazy('login')
    success_message = _("User was created successfully")


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/edit.html'
    success_url = reverse_lazy('users_list')
    success_message = _("User was updated successfully")
    login_url = reverse_lazy('login')

    def test_func(self):
        user = self.get_object()
        return user.id == self.request.user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, _("You have no right to edit the user."))
            return redirect(reverse_lazy('users_list'))
        else:
            messages.error(self.request, _("You are not authored! Please, log in."))
            return redirect(reverse_lazy('login'))


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_list')
    success_message = _("User was deleted successfully")
    login_url = reverse_lazy('login')

    def test_func(self):
        user = self.get_object()
        return user.id == self.request.user.id

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request, _("You have no right to edit the user."))
            return redirect(reverse_lazy('users_list'))
        else:
            messages.error(self.request, _("You are not authored! Please, log in."))
            return redirect(reverse_lazy('login'))
