from django.contrib import admin
from cms.models import Post

# Register your models here.
class Posts(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'categories')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title', 'categories')


admin.site.register(Post, Posts)