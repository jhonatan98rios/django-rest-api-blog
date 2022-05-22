from django.contrib import admin
from cms.models import Post, Image, Category

# Register your models here.
class Posts(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class Images(admin.ModelAdmin):
    list_display = ('id', 'title', 'src', 'alt')
    list_display_links = ('id', 'title', 'src', 'alt')

class Categories(admin.ModelAdmin):
    list_display = ('id', 'label')
    list_display_links = ('id', 'label')



admin.site.register(Post, Posts)
admin.site.register(Image, Images)
admin.site.register(Category, Categories)