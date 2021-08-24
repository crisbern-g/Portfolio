from django.db import models

class TagsModel(models.Model):
    tag_name = models.CharField(max_length=30)

    def __str__(self):
        return self.tag_name


class BlogImagesModel(models.Model):
    image = models.ImageField(upload_to='blog_images')
    image_caption = models.CharField(max_length=100, blank=True)
    image_source = models.CharField(max_length=100, blank=True)


class BlogModel(models.Model):
    blog_title = models.CharField(max_length=50)
    blog_text = models.TextField()
    blog_images = models.ManyToManyField(BlogImagesModel)
    blog_tag = models.ManyToManyField(TagsModel, related_name='tags')
    blog_date_added = models.DateTimeField(auto_now_add=True, editable=False)
    blog_date_modified = models.DateTimeField(auto_now=True)
    slug = models.SlugField()