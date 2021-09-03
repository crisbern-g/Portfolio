from django.urls import path
from . import views

urlpatterns = [
    path('', views.AllProjectsView.as_view(), name='all_projects'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name='project_detail'),
]
