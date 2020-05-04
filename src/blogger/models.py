from django.db import models
from django.utils import timezone
from users.models import User
from django.urls import reverse

from ckeditor_uploader.fields import RichTextUploadingField

class Post(models.Model):

    title = models.CharField(max_length=100)
    content = RichTextUploadingField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail-post', kwargs={'pk': self.pk})
