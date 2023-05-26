from django.db import models
from users.models import User
from statuses.models import Status
from labels.models import Label
from django.utils.translation import gettext_lazy as _


class Task(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name=_('Name'))
    description = models.TextField(null=True, blank=True, verbose_name=_("Description"))
    created_at = models.DateTimeField(auto_now=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name=_("Status"))
    creator = models.ForeignKey(User, related_name='creator', on_delete=models.PROTECT)
    executor = models.ForeignKey(User, related_name='executor', on_delete=models.PROTECT,
                                 null=True, blank=True,
                                 verbose_name=_("Executor"))
    labels = models.ManyToManyField(Label, blank=True, verbose_name=_("Labels"))

    def __str__(self):
        return self.name
