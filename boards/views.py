from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.generic import UpdateView, ListView
from django.utils import timezone
from django.utils.decorators import method_decorator
from .models import Board, Topic, Post
from .forms import NewTopicForm, PostForm


class BoardListView(ListView):
    """previously home
    """
    model = Board
    context_object_name = 'boards'
    template_name = 'boards/home.html'


def board_topics(request, pk):
    """Show topics on board
    """
    board = get_object_or_404(Board, pk=pk)
    topics = board.topics.order_by('-last_updated').annotate(replies=Count('posts')-1)
    return render(request, 'boards/topics.html', {'board': board, 'topics': topics})

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
            return redirect('topic_posts', pk=pk, topic_pk=topic.pk)
    else:
        form = NewTopicForm()
    return render(request, 'boards/new_topic.html', {'board': board, 'form': form})

def topic_posts(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    topic.views +=1
    topic.save()
    return render(request, 'boards/topic_posts.html', {'topic': topic})

@login_required
def topic_reply(request, pk, topic_pk):
    topic = get_object_or_404(Topic, board__pk=pk, pk=topic_pk)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('topic_posts', pk=pk, topic_pk=topic_pk)
    else:
        form = PostForm()
    return render(request, 'boards/topic_reply.html', {'topic': topic, 'form': form})


@method_decorator(login_required, name="dispatch")
class PostEditView(UpdateView):
    """GCBV for editing a post
    """
    model = Post
    fields = ('message', )
    template_name = 'boards/post_edit.html'
    pk_url_kwarg = 'post_pk'
    context_object_name = 'post'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(created_by=self.request.user)

    def form_valid(self, form):
        post = form.save(commit=False)
        post.updated_by = self.request.user
        post.updated_at = timezone.now()
        post.save()
        return redirect('topic_posts', 
                pk=post.topic.board.pk, 
                topic_pk=post.topic.pk
        )
