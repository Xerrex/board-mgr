from django.urls import reverse, resolve
from django.test import TestCase

from boards.models import Board
from boards.views import board_topics


class BoardTopicsTests(TestCase):
    """Single Board Tests
    """

    def setUp(self):
        Board.objects.create(name="Django", description="Django topics.")
    
    def test_board_view_success_status_code(self):
        url = reverse('board_topics', kwargs={'pk':1})
        response = self.client.get(url)

        self.assertEquals(response.status_code, 200)
    
    def test_board_not_found_status_code(self):
        url = reverse('board_topics', kwargs={'pk': 99})
        response = self.client.get(url)
        self.assertEquals(response.status_code, 404)

    def test_board_topics_url_resolves_board_topics_view(self):
        view = resolve('/boards/1/')
        self.assertEquals(view.func, board_topics)
