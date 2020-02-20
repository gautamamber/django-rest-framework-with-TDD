from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):
    """
    Model test case
    """
    def test_create_user_with_email(self):
        """
        Test creating a new user with email and password
        :return:
        """
        email = "test@gmail.com"
        password = "Test@12345"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """
        Test the email
        :return:
        """
        email = "amber@GAUTAM.com"
        user = get_user_model().objects.create_user(email, "test@123")
        self.assertEqual(user.email, email.lower())
