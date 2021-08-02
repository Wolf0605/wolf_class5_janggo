from django.urls import path
from django.views.generic import TemplateView

app_name = 'articleapp'

# TemplateView 어떤 html을 쓸지 말하면 그걸 보여줌
urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='List')

]