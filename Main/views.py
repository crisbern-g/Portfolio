from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.views import View
from Blog.models import BlogModel, TagsModel

# Create your views here.
class HomeView(TemplateView):
    template_name = 'Main/index.html'
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['latest_blogs'] = BlogModel.objects.all().order_by('-blog_date_added')[:4]
        context['tags'] =  TagsModel.objects.all().order_by('tag_name')

        return context


class AboutMeView(TemplateView):
    template_name = 'Main/about_me.html'

class ContactMeView(TemplateView):
    template_name = 'Main/contact_me.html'