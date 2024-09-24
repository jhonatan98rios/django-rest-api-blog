from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from cms.models import Post, Image, Category

class AdminSiteTests(TestCase):
    def setUp(self):
        # Criação de um superusuário para acessar a área admin
        self.superuser = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='password'
        )
        self.client = APIClient()
        self.client.login(username='admin', password='password')

        # Criação de alguns objetos para os testes
        self.post = Post.objects.create(
            slug="post-1",
            title="Post 1",
            updatedAt="2024-09-23",
            content="Content of post 1",
            seo_title="SEO Title 1",
            seo_description="SEO Description 1",
            seo_keywords="keywords 1"
        )
        self.image = Image.objects.create(
            src="https://example.com/image.jpg",
            alt="Example image",
            title="Example Title"
        )
        self.category = Category.objects.create(
            label="Tech",
            path="tech"
        )

    def test_admin_post_list_view(self):
        """Testa se a lista de posts na área admin é exibida corretamente"""
        url = reverse('admin:cms_post_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post 1')

    def test_admin_image_list_view(self):
        """Testa se a lista de imagens na área admin é exibida corretamente"""
        url = reverse('admin:cms_image_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Example Title')

    def test_admin_category_list_view(self):
        """Testa se a lista de categorias na área admin é exibida corretamente"""
        url = reverse('admin:cms_category_changelist')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tech')

    def test_admin_post_change_view(self):
        """Testa se a página de alteração de um post é exibida corretamente"""
        url = reverse('admin:cms_post_change', args=[self.post.id]) # type: ignore
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Post 1')

    def test_admin_image_change_view(self):
        """Testa se a página de alteração de uma imagem é exibida corretamente"""
        url = reverse('admin:cms_image_change', args=[self.image.id]) # type: ignore
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Example Title')

    def test_admin_category_change_view(self):
        """Testa se a página de alteração de uma categoria é exibida corretamente"""
        url = reverse('admin:cms_category_change', args=[self.category.id]) # type: ignore
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Tech')
