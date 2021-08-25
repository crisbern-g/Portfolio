from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllBlogsView.as_view(), name='all_blogs'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail')
]
