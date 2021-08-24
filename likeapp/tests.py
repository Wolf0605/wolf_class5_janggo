from django.contrib.auth.models import User
from django.db import models
from django.test import TestCase

# Create your tests here.
from articleapp.models import Article


class LikeRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name = 'like_record', null=False) # 유저삭제되면 함꼐 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE,
                                related_name='like_record', null=False) # 글이삭제되면 함꼐 삭제

    class Meta:
        unique_together = ['user', 'article']

