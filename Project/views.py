from django.db import models
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ProjectModel

# Create your views here.
class AllProjectsView(ListView):
    template_name = 'Project/all_projects.html'
    model = ProjectModel
    context_object_name = 'projects'


class ProjectDetailView(DetailView):
    template_name = 'Project/project_detail.html'
    model = ProjectModel
    context_object_name = 'project'