from django.test import TestCase
from django.urls import reverse, resolve

from .views import home


class HomeTests(TestCase):
    """ Defines tests for the home page
    """

    def test_home_view_status_code(self):
        """Test the home view status code
        """

        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """Test the Home Url resolves '/'
        """

        view = resolve('/')
        self.assertEquals(view.func, home)