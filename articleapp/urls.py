from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView

app_name = 'articleapp'

# TemplateView 어떤 html을 쓸지 말하면 그걸 보여줌


urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='List'),

    path('create/', ArticleCreateView.as_view(), name='create'),

    path('detail/<int:pk>', ArticleDetailView.as_view(),name='detail'),

    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),
]