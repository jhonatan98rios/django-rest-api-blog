from django.db import models
from ckeditor.fields import RichTextField
from cloudinary.models import CloudinaryField


class Image(models.Model):
    src = CloudinaryField('image')
    alt = models.CharField(max_length=60)
    title = models.CharField(max_length=60)

    def __str__(self):
        return self.title


class Category(models.Model):
    label = models.CharField(max_length=30)
    path = models.CharField(max_length=30)


    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.label

class Post(models.Model):
    slug = models.CharField(max_length=120)
    title = models.CharField(max_length=120)
    images = models.ManyToManyField(Image)
    updatedAt = models.CharField(max_length=30)
    categories = models.ManyToManyField(Category)
    content = RichTextField(blank=True, null=True)
    seo_title  = models.CharField(max_length=120)
    seo_description = models.TextField()
    seo_keywords = models.TextField()

    def __str__(self):
        return self.title


