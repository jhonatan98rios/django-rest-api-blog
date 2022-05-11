from django.db import models

# Create your models here.
class Post(models.Model):
    slug = models.CharField(max_length=140)
    title = models.CharField(max_length=140)
    banner = models.TextField()
    content = models.TextField()
    categories = models.CharField(max_length=30)

    def __str__(self):
        return self.title