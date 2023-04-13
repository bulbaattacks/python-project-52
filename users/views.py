from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views import View
from users.models import User
from users.forms import UserForm


class UsersListView(ListView):

    model = User
    template_name = 'users/list_of_users.html'


class UserCreateView(CreateView):

    model = User
    def get(self, request, *args, **kwargs):
        form = UserForm()
        return render(request, 'users/create.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
        return render(request, 'users/create.html', {'form': form})
