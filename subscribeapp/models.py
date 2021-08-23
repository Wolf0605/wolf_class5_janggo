from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from projectapp.models import Project


class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='subscribe', null=False) # 계정이 탈퇴되면 구독도 같이 탈퇴된다는 말

    project = models.ForeignKey(Project, on_delete=models.CASCADE,
                                related_name='subscription', null=False)

    class Meta:
        unique_together =['user', 'project'] #어떤 조합쌍이 유니크하도록 연결