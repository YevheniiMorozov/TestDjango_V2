from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    date_create = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT)

    def get_absolut_url(self):
        return reverse("news", kwargs={"id": self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.user.name, self.post)


class Upvotes(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    post = models.ForeignKey(News, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.name
