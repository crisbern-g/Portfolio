from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views import View

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Main/index.html'


class AboutMeView(TemplateView):
    template_name = 'Main/about_me.html'

class ContactMeView(TemplateView):
    template_name = 'Main/contact_me.html'