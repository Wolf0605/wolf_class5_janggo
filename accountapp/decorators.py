from django.contrib.auth.models import User
from django.http import HttpResponseForbidden


def account_ownership_required(func): # 유저정보와 데이터 정보에서 갖겨온 데이터가 일정할떄만 함수 호출
    def decorated(request, *args, **kwargs): # 데이터 베이스에서 가져옴
        target_user = User.objects.get(pk=kwargs['pk'])  #User의 객체중에 뭘 가져올지 view hellow world.objects.all() 과 비슷
        if target_user == request.user:
            return func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden()
    return decorated