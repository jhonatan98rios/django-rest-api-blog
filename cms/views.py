from rest_framework import viewsets
from cms.models import Post
from cms.serializer import PostSerializer

class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    http_method_names = ['get', 'head']


    