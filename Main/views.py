from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views import View

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Main/index.html'