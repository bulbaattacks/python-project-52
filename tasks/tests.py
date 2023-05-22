from django.test import TestCase
from django.urls import reverse
from .models import Task
from users.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _


class TaskTestCase(TestCase):
    fixtures = ["tasks.json", "users.json", "statuses.json", "labels.json"]

    def setUp(self):
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.task3 = Task.objects.get(pk=3)
        self.form_data = {"name": "Сходить к стоматологу",
                          "description": "Вылечить зубы",
                          "status": 1,
                          "creator": 1,
                          "executor": 2,
                          "labels": 3}
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

    def test_task_list(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse("tasks_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text=_("Tasks"))

    def test_create_task(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse("task_create"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("task_create"), self.form_data, follow=True)
        self.assertRedirects(response, reverse("tasks_list"))
        self.assertTrue(Task.objects.get(id=4))
        self.assertContains(response, text=_("Task was created successfully"))

    def test_update_task(self):
        self.client.force_login(self.user3)
        response = self.client.get(reverse("task_update", args=[self.task3.pk]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("task_update",
                                            args=[self.task3.pk]), self.form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.get(id=self.task3.pk))
        self.assertContains(response, text=_("Task was updated successfully"))

    def test_delete_user(self):
        self.client.force_login(self.user1)
        response = self.client.post(reverse("task_delete", args=[self.task3.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("tasks_list"))
        self.assertContains(response, text=_("Task was deleted successfully"))
        with self.assertRaises(ObjectDoesNotExist):
            self.assertFalse(Task.objects.get(id=self.task3.pk))
