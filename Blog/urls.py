from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllBlogsView.as_view(), name='all_blogs')
]
