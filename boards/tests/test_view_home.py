from django.test import TestCase
from django.urls import reverse, resolve

from ..models import Board
from ..views import home


class HomeTests(TestCase):
    """ Defines tests for the home page
    """

    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    def test_home_view_status_code(self):
        """Test the home view status code.
        """
        self.assertEquals(self.response.status_code, 200)

    def test_home_url_resolves_home_view(self):
        """Test the Home Url resolves '/'.
        """

        view = resolve('/')
        self.assertEquals(view.func, home)

    def test_home_view_contains_link_to_topics_page(self):
        """Test Home view contains Link to topics page.
        """
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))