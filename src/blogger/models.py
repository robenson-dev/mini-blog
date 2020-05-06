from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse

from django_ckeditor_5.fields import CKEditor5Field


class Post(models.Model):

    title = models.CharField(max_length=100)
    content = CKEditor5Field(config_name='extends', blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-post', kwargs={'pk': self.pk})


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = CKEditor5Field(config_name='extends', blank=True, null=True)
    release_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.post.title}-{self.user.username}'
