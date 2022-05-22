from rest_framework import serializers
from cms.models import Post, Image, Category

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = [
            'src',
            'alt',
            'title',
        ]

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'label',
            'path'
        ]

class PostSerializer(serializers.ModelSerializer):

    images = ImageSerializer(read_only=True, many=True)
    categories = CategorySerializer(read_only=True, many=True)
    class Meta:
        model = Post
        fields = [
            'slug',
            'title',
            'images',
            'updatedAt',
            'categories',
            'content',
            'seo_title',
            'seo_description',
            'seo_keywords',
        ]



