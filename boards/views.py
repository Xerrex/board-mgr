from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Board

def home(request):
    boards = Board.objects.all()
    
    return render(request, 'home.html', {'boards': boards})

def board_topics(request, pk):
    """Show topics on board
    """
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'board_topics.html', {'board': board})