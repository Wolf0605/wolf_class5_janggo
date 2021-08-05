from django.urls import path
from django.views.generic import TemplateView

from articleapp.views import ArticleCreateView, ArticleDetailView, ArticleUpdateView, ArticleDeleteView, ArticleListView

app_name = 'articleapp'

# TemplateView 어떤 html을 쓸지 말하면 그걸 보여줌


urlpatterns = [

    path('list/', ArticleListView.as_view(), name='List'),

    path('create/', ArticleCreateView.as_view(), name='create'),

    path('detail/<int:pk>', ArticleDetailView.as_view(),name='detail'),

    path('update/<int:pk>', ArticleUpdateView.as_view(), name='update'),

    path('delete/<int:pk>', ArticleDeleteView.as_view(), name='delete')
]