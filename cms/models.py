from django.db import models

# Create your models here.
class Post(models.Model):
    seo_title
    seo_description
    seo_keywords
    slug = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    banner = models.CharField(max_length=120)
    banner_alt = models.CharField(max_length=20)
    banner_title = models.CharField(max_length=20)
    updatedAt = models.CharField(max_length=20)
    categories = models.CharField(max_length=30)
    content = models.TextField()

    def __str__(self):
        return self.title