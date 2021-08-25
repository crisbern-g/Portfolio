from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import BlogModel

# Create your views here.
class AllBlogsView(ListView):
    template_name = 'Blog/all_blogs.html'
    model = BlogModel
    context_object_name = 'blogs'
    ordering = ['-blog_date_added']
    paginate_by = 10

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['latest'] = BlogModel.objects.all().order_by('-blog_date_modified')[:10]

        return data

class BlogDetail(DetailView):
    template_name = 'Blog/blog_detail.html'
    model = BlogModel
    context_object_name = 'blog'