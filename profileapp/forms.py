
from django.forms import ModelForm

from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta: # 만드는거임
        model = Profile
        fields = ['image', 'nickname', 'message'] # 클라이언트로부터 입력 받을 속성들??