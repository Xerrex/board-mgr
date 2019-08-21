from django.test import TestCase
from django.urls import reverse


class InvalidSignUpTests(TestCase):
    """Test for invalid signup
    """

    def setUp(self):
        url = reverse('signup')
        self.response = self.client.post(url, {})  # submit an empty dictionary

    def test_signup_status_code(self):
        """Test signup status code

         An invalid form submission should return
         to the same page.
        """
        self.assertEquals(self.response.status_code, 200)

    def test_form_errors(self):
        """Test form errors.
        """
        form = self.response.context.get('form')
        self.assertTrue(form.errors)
