from django.test import TestCase
from .models import User
from django.test import Client


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

    def test_user_update(self):
        """User is updated correctly"""
        user1 = User.objects.get(last_name="Ivanyan")
        user1.last_name = "Iman"
        user2 = User.objects.get(last_name="Zubova")
        user2.last_name = "Kant"
        self.assertEqual(user1.last_name, "Iman")
        self.assertEqual(user2.last_name, "Kant")

    '''обязуюсь написать нормальные тесты'''

