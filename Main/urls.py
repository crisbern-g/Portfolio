from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('about-me/', views.AboutMeView.as_view(), name='about_me'),
    path('contact-me/', views.ContactMeView.as_view(), name='contact_me')
]
