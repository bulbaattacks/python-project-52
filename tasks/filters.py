from .models import Task
from statuses.models import Status
from labels.models import Label
from users.models import User
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms
from django.utils.translation import gettext_lazy as _


class TaskFilter(FilterSet):

    def my_task_filter(self, queryset):
        author = self.request.user
        return queryset.filter(creator=author)

    status = ModelChoiceFilter(queryset=Status.objects.all(),
                               label=_('Status'),
                               widget=forms.Select(
                                   attrs={'class': 'custom-select d-block'}))

    label = ModelChoiceFilter(queryset=Label.objects.all(),
                              label=_('Label'),
                              widget=forms.Select(
                                  attrs={'class': 'custom-select d-block'}))

    assignee = ModelChoiceFilter(queryset=User.objects.all(),
                                 label=_('Assignee'),
                                 widget=forms.Select(
                                     attrs={'class': 'custom-select d-block'}))

    mine = BooleanFilter(label=_('My tasks only'),
                         widget=forms.widgets.CheckboxInput(
                             attrs={'name': 'mine'}),
                         method='my_task_filter',
                         )

    class Meta:
        model = Task
        fields = ['status', 'label', 'assignee', 'mine']
