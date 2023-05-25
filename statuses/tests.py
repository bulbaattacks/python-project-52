from django.test import TestCase
from django.urls import reverse
from .models import Status
from users.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _


class StatusTestCase(TestCase):
    fixtures = ["statuses.json", "users.json", "labels.json", "tasks.json"]

    def setUp(self):
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.status3 = Status.objects.get(pk=3)
        self.form_data = {"name": "new_status"}
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

    def test_statuses_list(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse("statuses_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text=_("Statuses"))

    def test_create_status(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse("status_create"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("status_create"), self.form_data, follow=True)
        self.assertRedirects(response, reverse("statuses_list"))
        self.assertTrue(Status.objects.get(id=4))
        self.assertContains(response, text=_("Status was created successfully"))

    def test_update_status(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse("status_update", args=[self.status2.pk]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("status_update",
                                            args=[self.status2.pk]), self.form_data, follow=True)
        self.assertRedirects(response, reverse("statuses_list"))
        self.assertTrue(Status.objects.get(id=self.status2.pk))
        self.assertContains(response, text=_("Status was updated successfully"))

    def test_delete_status(self):
        self.client.force_login(self.user3)
        response = self.client.get(reverse("status_delete", args=[self.status3.pk]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("status_delete", args=[self.status3.pk]), follow=True)
        self.assertRedirects(response, reverse("statuses_list"))
        with self.assertRaises(ObjectDoesNotExist):
            self.assertFalse(Status.objects.get(pk=self.status3.pk))
        self.assertContains(response, text=_("Status was deleted successfully"))

    def test_delete_status_attached_to_task(self):
        self.client.force_login(self.user3)
        response = self.client.get(reverse("status_delete", args=[self.status1.pk]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("status_delete", args=[self.status1.pk]), follow=True)
        self.assertRedirects(response, reverse("statuses_list"))
        self.assertTrue(Status.objects.get(id=1))
        self.assertContains(response,
                            text=_("Can't delete the status because it's used for the task"))
