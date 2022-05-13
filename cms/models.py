from django.db import models

# Create your models here.
class Post(models.Model):
    slug = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    banner_src = models.CharField(max_length=120)
    banner_alt = models.CharField(max_length=60)
    banner_title = models.CharField(max_length=60)
    updatedAt = models.CharField(max_length=30)
    categories = models.CharField(max_length=30)
    content = models.TextField()
    seo_title  = models.CharField(max_length=120)
    seo_description = models.TextField()
    seo_keywords = models.TextField()

    def __str__(self):
        return self.title