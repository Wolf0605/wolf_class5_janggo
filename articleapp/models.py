from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Article(models.Model):
    writer = models.ForeignKey(User, on_delete=models.SET_NULL,
                               related_name='article',
                               null=True)
    project = models.ForeignKey(Project,
                                on_delete=models.SET_NULL,
                                related_name='article',
                                null=True)  #models.SET회원이 삭제된다고 글이 삭제되진않음
    title = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='articles/', null=True)
    content = models.TextField(null=True)

    created_at = models.DateField(auto_now_add=True, null=True)