from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _
from django.urls import reverse_lazy
from django.contrib import messages


class UserPermissionCustomMixin(LoginRequiredMixin, UserPassesTestMixin):
    permission_denied_message = _("You have no right to edit the user.")
    not_auth_message = _("You are not authored! Please, log in.")

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
