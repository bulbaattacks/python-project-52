from django.test import TestCase
from django.urls import reverse
from .models import Label
from users.models import User
from django.core.exceptions import ObjectDoesNotExist


class LabelTestCase(TestCase):
    fixtures = ["labels.json", "users.json"]

    def setUp(self):
        self.status1 = Label.objects.get(pk=1)
        self.status2 = Label.objects.get(pk=2)
        self.status3 = Label.objects.get(pk=3)
        self.form_data = {"name": "new_label"}
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)

    def test_labels_list(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse("labels_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, text="Метки")

    def test_create_status(self):
        self.client.force_login(self.user1)
        response = self.client.get(reverse("label_create"))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("label_create"), self.form_data, follow=True)
        self.assertRedirects(response, reverse("labels_list"))
        self.assertTrue(Label.objects.get(id=4))
        self.assertContains(response, text="Метка успешно создана")

    def test_update_status(self):
        self.client.force_login(self.user2)
        response = self.client.get(reverse("label_update", args=[2]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("label_update", args=[2]), self.form_data, follow=True)
        self.assertRedirects(response, reverse("labels_list"))
        self.assertTrue(Label.objects.get(id=3))
        self.assertContains(response, text="Метка успешно изменена")

    def test_delete_status(self):
        self.client.force_login(self.user3)
        response = self.client.get(reverse("label_delete", args=[2]))
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse("label_delete", args=[2]), follow=True)
        self.assertRedirects(response, reverse("labels_list"))
        with self.assertRaises(ObjectDoesNotExist):
            self.assertFalse(Label.objects.get(pk=2))
        self.assertContains(response, text="Метка успешно удалена")
