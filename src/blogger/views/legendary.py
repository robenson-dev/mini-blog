from django.shortcuts import render, redirect,get_object_or_404
from blogger.models import Post, Comment
from django.db.models import Q
from blogger.forms import CreatePostForm, CommentForm

from users.decorators import super_blogger_required
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
from django.views.generic.edit import FormMixin


@login_required()
@super_blogger_required()
def dashboard(request):
    posts = Post.objects.all().filter(author=request.user.id)
    posts_count = posts.count()
    return render(request, 'blogger/legendary/dashboard.html', locals())


class PostListView(ListView):

    model = Post
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2

    def get(self, request, *args, **kwargs):
        post_contains = request.GET.get('post_search')

        if post_contains:
            self.object = Post.objects.filter(Q(title=post_contains)).distinct()
        else:
            self.object = Post.objects.all()

        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = self.object
        return context


class PostDetailView(LoginRequiredMixin, FormMixin, DetailView):

    template_name = 'blogger/legendary/post_detail.html'
    model = Post
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'post': self.object})
        context['comments'] = Comment.objects.filter(post=kwargs['object'].id).order_by('id')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            instance_post = get_object_or_404(Post, id=kwargs['pk'])
            content_data = request.POST.get('content')
            comment = Comment.objects.create(post=instance_post, user=request.user, content=content_data)
            comment.save()
            return redirect('detail-post', pk=kwargs['pk'])
        else:
            return self.form_invalid(form)



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


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = Post
    template_name = 'blogger/legendary/post_confirm_delete.html'
    success_url = reverse_lazy('legendary:legendary-dashboard')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False


#-------------------------------------[ POST-COMMENT ]-----------------------------------------------------------------#


# class CommentCreateView(LoginRequiredMixin, CreateView):
#
#     model = Comment
#     form_class = CommentForm
#     success_url = reverse_lazy('legendary:legendary-dashboard')
#
#     def form_valid(self, form):
#         # form.instance.author = self.request.user
#         #
#         # comment = Comment.objects.create(episode=episode, user=request.user, content=content)
#         # comment.save()
#         return super().form_valid(form)
