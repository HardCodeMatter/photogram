from django.db import models
from django.utils import timezone
from user.models import User


class Post(models.Model):
    image = models.ImageField(('image'), upload_to='posts/')
    title = models.CharField(('title'), max_length=50)
    description = models.TextField(('description'), max_length=300, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    date_published = models.DateField(('published date'), default=timezone.now)

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField(('comment'), max_length=300)
    date_published = models.DateTimeField(('published date'), default=timezone.now)
    date_updated = models.DateTimeField(('updated date'), blank=True, null=True)

    def __str__(self) -> str:
        return f'Comment {self.pk}'
