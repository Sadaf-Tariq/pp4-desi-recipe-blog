from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()


class CustomUserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            'testcustomuser@abc.pl', 'abcd')

    def test_custom_user(self):
        email = self.user.email
        self.assertEqual(email, 'testcustomuser@abc.pl')
