from django.http import HttpResponse
from django.shortcuts import render
from .models import Board

def index(request):
    boards = Board.objects.all()
    board_names = []

    for board in boards:
        board_names.append(board.name)
    
    output = '<br>'.join(board_names)

    return HttpResponse(output)
