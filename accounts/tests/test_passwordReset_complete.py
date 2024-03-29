from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views


class PasswordResetCompleteTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_complete')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/auth/password-reset/complete/')
        self.assertEquals(view.func.view_class, auth_views.PasswordResetCompleteView)