from .models import Task
from statuses.models import Status
from labels.models import Label
from users.models import User
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django import forms


class TaskFilter(FilterSet):

    def my_task_filter(self, queryset):
        author = self.request.user
        return queryset.filter(creator=author)

    status = ModelChoiceFilter(queryset=Status.objects.all(),
                               label='Status',
                               widget=forms.Select(
                                   attrs={'class': 'custom-select d-block'}))

    label = ModelChoiceFilter(queryset=Label.objects.all(),
                              label='Label',
                              widget=forms.Select(
                                  attrs={'class': 'custom-select d-block'}))

    assignee = ModelChoiceFilter(queryset=User.objects.all(),
                                 label='Assignee',
                                 widget=forms.Select(
                                     attrs={'class': 'custom-select d-block'}))

    mine = BooleanFilter(label='My tasks only',
                         widget=forms.widgets.CheckboxInput(
                             attrs={'name': 'mine'}),
                         method='my_task_filter',
                         )

    class Meta:
        model = Task
        fields = ['status', 'label', 'assignee', 'mine']
