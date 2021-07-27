from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountCreationForm
from accountapp.models import HelloWorld

@login_required(login_url=reverse_lazy('accountapp:login'))     # 장고 기본 기능,, accounts/login이 자동 경로로 저장
def hello_world(request):
        if request.method == "POST":
            temp = request.POST.get('hello_world_input')
            new_hello_world = HelloWorld()
            new_hello_world.text = temp
            new_hello_world.save()
            return HttpResponseRedirect(reverse('accountapp:hello_world')) # reverse 로 주소를 역 추적.
        else:
            hello_world_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hello_world.html',
                          context={'hello_world_list': hello_world_list})

has_ownership = [login_required(login_url=reverse_lazy('accountapp:login')), account_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User #어떤 객체를 수정 할 것 인가
    form_class = AccountCreationForm
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html' # 어떤 페이지를 가져와서 시각화 할 것 인가

class AccountCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world') # class에서 rever.lazy()
    template_name = 'accountapp/create.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/delete.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    def form_valid(self,form):
        form.instance.user = self.request.user
        return super().form_valid(form)