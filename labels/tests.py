from django.test import TestCase
from .models import Label


class UserTestCase(TestCase):
    def setUp(self):
        Label.objects.create(name="Critical")
        Label.objects.create(name="Low")

    def test_user_create(self):
        """User is created correctly"""
        label1 = Label.objects.get(name="Critical")
        label2 = Label.objects.get(name="Low")
        self.assertEqual(label1.name, "Critical")
        self.assertEqual(label2.name, "Low")
