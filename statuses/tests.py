from django.test import TestCase
from .models import Status


class UserTestCase(TestCase):
    def setUp(self):
        Status.objects.create(name="In Progress")
        Status.objects.create(name="Backlog")

    def test_user_create(self):
        """User is created correctly"""
        status1 = Status.objects.get(name="In Progress")
        status2 = Status.objects.get(name="Backlog")
        self.assertEqual(status1.name, "In Progress")
        self.assertEqual(status2.name, "Backlog")
