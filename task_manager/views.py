from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = "home_page.html"


class MyLoginView(SuccessMessageMixin, LoginView):
    template_name = "login.html"
    success_message = _("You are logged in")


class MyLogoutView(SuccessMessageMixin, LogoutView):
    def dispatch(self, request, *args, **kwargs):
        messages.add_message(request, messages.INFO, _("You are logged out"))
        return super().dispatch(request, *args, **kwargs)
