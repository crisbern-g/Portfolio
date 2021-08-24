from django.shortcuts import render
from django.views.generic import ListView
from .models import BlogModel

# Create your views here.
class AllBlogsView(ListView):
    template_name = 'Blog/all_blogs.html'
    model = BlogModel
    context_object_name = 'blogs'
    ordering = ['-blog_date_added']
    paginate_by = 2

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['latest'] = BlogModel.objects.all().order_by('-blog_date_added')[:5]

        return data