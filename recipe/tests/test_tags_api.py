from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Tag, Ingredient
from recipe.serializers import TagSerializer

TAGS_URL = reverse('recipe:tag-list')


class PublicApiTests(TestCase):
    """
    Test the public available tags api
    """
    def setUp(self):
        """
        Set up database
        :return:
        """
        self.client = APIClient

    def test_login_required(self):
        """
        test that login is required for retrieving tags
        :return:
        """
        # res = self.client.get(TAGS_URL, )
        # self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateTagsApiTests(TestCase):
    """
    Test the authorized user
    """
    def setUp(self):
        """
        set up user
        :return:
        """
        self.user = get_user_model().objects.create_user(
            "amber@test.com",
            "password123"
        )
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_tags(self):
        """
        Test for retrieving tags
        :return:
        """
        Tag.objects.create(user=self.user, name="TestName")
        res = self.client.get(TAGS_URL)
        tags = Tag.objects.all().order_by('-name')
        serializer = TagSerializer(tags, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
