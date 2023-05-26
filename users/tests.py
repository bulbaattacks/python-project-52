from django.test import TestCase
from django.urls import reverse
from .models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.translation import gettext_lazy as _
import os
import json
from task_manager.settings import FIXTURE_DIRS


class UserTestCase(TestCase):
    fixtures = ["users.json", "one_task.json", "statuses.json", "labels.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.login = reverse("login")
        with open(os.path.join(FIXTURE_DIRS[0], "user_form_data.json")) as file:
            self.form_data = json.load(file)

    def test_users_list(self):
        response = self.client.get(reverse("users_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text=_("Users"))

    def test_create_user(self):
        response = self.client.get(reverse("user_create"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("user_create"), self.form_data, follow=True)
        self.assertRedirects(response, self.login)
        self.assertTrue(User.objects.get(id=4))
        self.assertContains(response, text=_("User was created successfully"))

    def test_create_user_with_existing_username(self):
        response = self.client.get(reverse("user_create"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("user_create"), self.form_data, follow=True)
        self.assertRedirects(response, self.login)
        self.assertTrue(User.objects.get(id=4))
        response = self.client.get(reverse("user_create"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("user_create"), self.form_data, follow=True)
        with self.assertRaises(ObjectDoesNotExist):
            self.assertFalse(User.objects.get(id=5))
        self.assertContains(response, text=_("A user with the same name already exists."))

    def test_update_user_with_permission(self):
        self.client.force_login(self.user3)
        response = self.client.get(reverse("user_update", args=[self.user3.pk]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("user_update",
                                            args=[self.user3.pk]), self.form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.get(id=self.user3.pk))
        self.assertContains(response, text=_("User was updated successfully"))

    def test_update_user_with_no_permission(self):
        self.client.force_login(self.user3)
        response = self.client.post(reverse("user_update",
                                            args=[self.user2.pk]), self.form_data, follow=True)
        self.assertRedirects(response, reverse("users_list"))
        self.assertContains(response, text=_("You have no right to edit the user."))
        self.assertTrue(User.objects.get(id=self.user3.pk))

    def test_delete_user(self):
        self.client.force_login(self.user3)
        response = self.client.post(reverse("user_delete", args=[self.user3.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("users_list"))
        self.assertContains(response, text=_("User was deleted successfully"))
        with self.assertRaises(ObjectDoesNotExist):
            self.assertFalse(User.objects.get(id=self.user3.pk))

    def test_delete_user_with_no_permission(self):
        self.client.force_login(self.user3)
        response = self.client.post(reverse("user_delete", args=[self.user2.pk]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("users_list"))
        self.assertContains(response, text=_("You have no right to edit the user."))
        self.assertTrue(User.objects.get(id=self.user2.pk))

    def test_delete_user_with_task(self):
        self.client.force_login(self.user2)
        response = self.client.post(reverse("user_delete", args=[self.user2.pk]), follow=True)
        self.assertRedirects(response, reverse("users_list"))
        self.assertContains(response,
                            text=_("Can't delete the user because it's used for the task"))
        self.assertTrue(User.objects.get(id=self.user2.pk))
