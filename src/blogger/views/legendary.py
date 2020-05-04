from django.shortcuts import render
from blogger.models import Post
from blogger.forms import CreatePostForm

from users.decorators import super_blogger_required
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView
)


@login_required()
@super_blogger_required()
def dashboard(request):
    posts = Post.objects.all().filter(author=request.user.id)
    posts_count = posts.count()
    return render(request, 'blogger/legendary/dashboard.html', locals())


class PostListView(LoginRequiredMixin, ListView):

    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = 'blogger/legendary/post_detail.html'


class PostCreateView(LoginRequiredMixin, CreateView):

    model = Post
    template_name = 'blogger/legendary/create_post.html'
    form_class = CreatePostForm
    success_url = reverse_lazy('legendary:legendary-dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Post
    template_name = 'blogger/legendary/update_post.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('legendary:legendary-dashboard')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False
