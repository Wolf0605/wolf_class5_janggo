from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Profile(models.Model): # models 안에있는 Model
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')#1대1로 (유저)를 연결해준다
    # Account 계정이 삭제됐을때 profile 은 어케 할꺼냐를 담당해주는게 on_delete, CASCADE ->종속 즉, account가 삭제되면 profile 도 삭제되게 함
    # user와 profile 을 연결해주는데 user과 1대1로 연결돼있는 프로필 객체를 불러주는 ex)target_user.profile

    image = models.ImageField(upload_to='profile/', null = True) # 경로 관련 비어있어도 괜찮다 null True
    nickname = models.CharField(max_length=30, unique=True, null=True) # 문자필드
    message = models.CharField(max_length=200, null=True)
    # make migrations # 변화를 측정하는 db를 만든다
    #     #db에 연결해줌ㅈ