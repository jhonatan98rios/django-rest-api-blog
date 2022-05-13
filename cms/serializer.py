from rest_framework import serializers
from cms.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'slug', 'title', 'banner', 'categories', 'content']