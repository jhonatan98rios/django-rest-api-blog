from rest_framework import status
from rest_framework.test import APITestCase
from cms.models import Post, Image, Category
from datetime import date

class PostsViewSetTestCase(APITestCase):
    def setUp(self):
        self.post1 = Post.objects.create(
            slug="post-1",
            title="Post 1",
            updatedAt=date.today(),
            content="Content of post 1",
            seo_title="SEO Title 1",
            seo_description="SEO Description 1",
            seo_keywords="keywords 1"
        )
        self.post2 = Post.objects.create(
            slug="post-2",
            title="Post 2",
            updatedAt=date.today(),
            content="Content of post 2",
            seo_title="SEO Title 2",
            seo_description="SEO Description 2",
            seo_keywords="keywords 2"
        )
        self.url = '/posts/'  # Substitua pela URL real da sua viewset

    def test_get_posts(self):
        """Testa se a requisição GET para a lista de posts retorna uma resposta 200 OK"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # type: ignore
        self.assertEqual(response.data[0]['title'], self.post1.title) # type: ignore
        self.assertEqual(response.data[1]['title'], self.post2.title) # type: ignore


class ImageViewSetTestCase(APITestCase):
    def setUp(self):
        self.image = Image.objects.create(
            src="https://example.com/image.jpg",
            alt="Example image",
            title="Example Title"
        )
        self.url = '/images/'  # Substitua pela URL real da sua viewset

    def test_get_images(self):
        """Testa se a requisição GET para a lista de imagens retorna uma resposta 200 OK"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # type: ignore
        self.assertEqual(response.data[0]['title'], self.image.title)  # type: ignore


class CategoryViewSetTestCase(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(
            label="Tech",
            path="tech"
        )
        self.url = '/categories/'  # Substitua pela URL real da sua viewset

    def test_get_categories(self):
        """Testa se a requisição GET para a lista de categorias retorna uma resposta 200 OK"""
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1) # type: ignore
        self.assertEqual(response.data[0]['label'], self.category.label) # type: ignore