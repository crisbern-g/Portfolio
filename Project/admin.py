from django.contrib import admin
from .models import ProjectModel, TechModel

# Register your models here.
class ProjectAdminModel(admin.ModelAdmin):
    prepopulated_fields ={
        'slug' : ('project_name',)
    }

admin.site.register(ProjectModel, ProjectAdminModel)
admin.site.register(TechModel)
