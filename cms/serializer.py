from rest_framework import serializers
from cms.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'slug',
            'title',
            'banner_src',
            'banner_alt',
            'banner_title',
            'updatedAt',
            'categories',
            'content',
            'seo_title',
            'seo_description',
            'seo_keywords',
        ]

        