from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_super_blogger = models.BooleanField(default=False)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'

    def __str__(self):
        return self.username


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(default='default.jpg', upload_to='picture')

    def __str__(self):
        return f'{self.user.username} Profile'

    def delete(self, *args, **kwargs):
        self.picture.delete()
        super().delete(*args, **kwargs)
