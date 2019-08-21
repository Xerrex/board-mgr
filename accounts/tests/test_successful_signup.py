from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class SuccessfulSignUpTests(TestCase):
    """Test successful signup.
    """

    def setUp(self):
        url = reverse('signup')
        data = {
            'username': 'john',
            'email': 'john@doe.com',
            'password1': 'abcdef123456',
            'password2': 'abcdef123456'
        }
        self.response = self.client.post(url, data)
        self.home_url = reverse('home')

    def test_redirection(self):
        """Test redirection.

        A valid form submission should redirect
        the user to the home page.
        """

        self.assertRedirects(self.response, self.home_url)

    def test_user_creation(self):
        """Test user creation.
        """
        self.assertTrue(User.objects.exists())

    def test_user_authentication(self):
        """Test user authentication.

        Create a new request to an arbitrary page.
        The resulting response should now have a `user` to its context,
        after a successful sign up.
        """

        response = self.client.get(self.home_url)
        user = response.context.get('user')
        self.assertTrue(user.is_authenticated)