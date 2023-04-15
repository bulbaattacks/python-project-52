from django.views import View
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "home_page.html"
