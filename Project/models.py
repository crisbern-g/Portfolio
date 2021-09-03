from django.db import models

# Create your models here.
class TechModel(models.Model):
    tech_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tech_name


class ProjectModel(models.Model):
    project_name = models.CharField(max_length=100)
    project_repository = models.URLField(blank=True, null=True)
    project_link = models.URLField(blank=True, null=True)
    project_brief = models.CharField(null=True, blank=True, max_length=100)
    project_description = models.TextField()
    project_demonstration = models.TextField(blank=True, null=True)
    project_screencapture = models.ImageField(blank=True, null=True, upload_to='project_screen_capture')
    project_thumbnail = models.ImageField(upload_to='project_thumbnail')
    project_tech = models.ManyToManyField(TechModel)
    slug = models.SlugField()

    def __str__(self):
        return self.project_name