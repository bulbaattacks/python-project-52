from django.test import TestCase
from django.urls import reverse
from .models import User
from django.core.exceptions import ObjectDoesNotExist


class UserTestCase(TestCase):
    fixtures = ["users.json"]

    def setUp(self):
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.login = reverse("login")
        self.form_data = {"username": "Neo",
                          "last_name": "Tomas",
                          "first_name": "Anderson",
                          "password1": "mystupidpassword1234",
                          "password2": "mystupidpassword1234"}
    def test_users_list(self):
        response = self.client.get(reverse("users_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text='Пользователи')

    def test_create_user(self):
        response = self.client.get(reverse("user_create"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("user_create"), self.form_data, follow=True)
        self.assertRedirects(response, self.login)
        self.assertTrue(User.objects.get(id=4))
        self.assertContains(response, text="Пользователь успешно зарегистрирован")

    def test_update_user_with_permission(self):
        self.client.force_login(self.user3)
        response = self.client.get(reverse("user_update", args=[3]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("user_update", args=[3]), self.form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(User.objects.get(id=3))
        self.assertContains(response, text="Пользователь успешно изменён")

    def test_update_user_with_no_permission(self):
        self.client.force_login(self.user3)
        response = self.client.post(reverse("user_update", args=[2]), self.form_data, follow=True)
        self.assertRedirects(response, reverse("users_list"))
        self.assertContains(response, text="У вас нет прав для изменения другого пользователя.")
        self.assertTrue(User.objects.get(id=3))

    def test_delete_user(self):
        self.client.force_login(self.user3)
        response = self.client.post(reverse("user_delete", args=[3]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("users_list"))
        self.assertContains(response, text="Пользователь успешно удалён")
        with self.assertRaises(ObjectDoesNotExist):
            self.assertFalse(User.objects.get(id=3))

    def test_delete_with_no_permission(self):
        self.client.force_login(self.user3)
        response = self.client.post(reverse("user_delete", args=[2]), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, reverse("users_list"))
        self.assertContains(response, text="У вас нет прав для изменения другого пользователя.")
        self.assertTrue(User.objects.get(id=2))