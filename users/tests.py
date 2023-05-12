from django.test import TestCase
from .models import User


class UserTestCase(TestCase):
    def setUp(self):
        User.objects.create(first_name="Ivan", last_name="Ivanyan",
                            username="roar", password='tyubnm678')
        User.objects.create(first_name="Arina", last_name="Zubova",
                            username="zub", password='bnmtyu890')

    def test_user_create(self):
        """User is created correctly"""
        user1 = User.objects.get(last_name="Ivanyan")
        user2 = User.objects.get(last_name="Zubova")
        self.assertEqual(user1.first_name, "Ivan")
        self.assertEqual(user2.first_name, "Arina")
