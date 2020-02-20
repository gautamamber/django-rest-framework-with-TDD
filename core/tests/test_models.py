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

    def test_new_user_invalid_email(self):
        """
        Test creating with user no email error raise
        :return:
        """
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None)

    def test_create_new_super_user(self):
        """
        Test creating a new super user
        :return:
        """
        user = get_user_model().objects.create_superuser(
            "amber@test.com",
            "test@123"
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
