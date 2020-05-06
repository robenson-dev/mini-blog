from django import forms
from blogger.models import Post, Comment

class CreatePostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
