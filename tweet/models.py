from uuid import uuid4

from django.db import models


# Create your models here.

class Tweet(models.Model):
    # id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.CharField(max_length=200)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ['-last_update']


class Comment(models.Model):
    comment = models.CharField(max_length=150)
    commented_on = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweet_comments')

    def __str__(self):
        return self.comment
