from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.views import PasswordResetDoneView


class PasswordResetDoneTests(TestCase):
    def setUp(self):
        url = reverse('password_reset_done')
        self.response = self.client.get(url)

    def test_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    def test_view_function(self):
        view = resolve('/auth/password-reset/done/')
        self.assertEquals(view.func.view_class, PasswordResetDoneView)