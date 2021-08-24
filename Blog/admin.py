from django.contrib import admin
from .models import BlogImagesModel, BlogModel, TagsModel

class BlogAdminModel(admin.ModelAdmin):
    prepopulated_fields = {
        'slug' : ('blog_title',)
    }
    readonly_fields = ('blog_date_added', 'blog_date_modified')

# Register your models here.
admin.site.register(BlogModel, BlogAdminModel)
admin.site.register(BlogImagesModel)
admin.site.register(TagsModel)
