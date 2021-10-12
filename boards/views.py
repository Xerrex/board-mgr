from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Board, Topic, Post
from .forms import NewTopicForm


def home(request):
    boards = Board.objects.all()
    
    return render(request, 'boards/home.html', {'boards': boards})

def board_topics(request, pk):
    """Show topics on board
    """
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'boards/topics.html', {'board': board})

@login_required
def new_topic(request, pk):
    """Create a new Topic
    """
    board = get_object_or_404(Board, pk=pk)

    if request.method == "POST":
        form = NewTopicForm(request.POST)

        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()

            post = Post.objects.create(
                message=form.cleaned_data.get('message'), 
                topic=topic, created_by=request.user
            )
            return redirect('board_topics', pk=board.pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})