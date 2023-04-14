from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from users.models import User
from users.forms import UserForm


class UsersListView(ListView):
    model = User
    template_name = 'users/list_of_users.html'


class UserCreateView(CreateView):
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('login')


class UserUpdateView(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'users/create.html'
    success_url = reverse_lazy('users_list')


class UserDeleteView(DeleteView):
    model = User
    template_name = 'users/delete.html'
    success_url = reverse_lazy('users_list')
