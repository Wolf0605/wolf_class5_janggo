from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.views.generic.list import MultipleObjectMixin

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld
from articleapp.models import Article


has_ownership = [login_required(login_url=reverse_lazy('accountapp:login')), account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User #어떤 객체를 수정 할 것 인가
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    template_name = 'accountapp/update.html' # 어떤 페이지를 가져와서 시각화 할 것 인가

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('articleapp:List') # class에서 rever.lazy()
    template_name = 'accountapp/create.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('articleapp:List')
    template_name = 'accountapp/delete.html'


class AccountDetailView(DetailView, MultipleObjectMixin):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    paginate_by = 20

    def get_context_data(self, **kwargs):
        article_list = Article.objects.filter(writer=self.object)
        return super().get_context_data(object_list=article_list, **kwargs)

    # reverse 는 함수형에서 가져와서 쓰는?
    # 방금한게 succes_url = reverse_lazy(~~~) 를 오버라이딩으로 바꿔준게 방금내용이 맞나요??
