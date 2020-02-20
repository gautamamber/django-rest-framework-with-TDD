from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class AdminSiteTests(TestCase):
    """
    Admin test case
    """
    def setUp(self):
        """
        Set up admin
        :return:
        """
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="amber@test.com",
            password="Test@12345"
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="amber+1@test.com",
            password="Test@12345",
            name="Amber"
        )

    def test_user_listed(self):
        """
        Test users are listed on user page
        :return:
        """
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
