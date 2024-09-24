from django.test import TestCase
from cms.models import Post, Image, Category
from datetime import date

class ImageModelTestCase(TestCase):
    def setUp(self):
        self.image = Image.objects.create(
            src="https://example.com/image.jpg",
            alt="Example image",
            title="Example Title"
        )

    def test_image_creation(self):
        """Testa se a instância do modelo Image foi criada corretamente"""
        self.assertEqual(self.image.title, "Example Title")
        self.assertEqual(self.image.alt, "Example image")
        self.assertEqual(self.image.src, "https://example.com/image.jpg")

    def test_image_str(self):
        """Testa se o método __str__ de Image retorna o título correto"""
        self.assertEqual(str(self.image), "Example Title")
        
class CategoryModelTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(
            label="Technology",
            path="tech"
        )

    def test_category_creation(self):
        """Testa se a instância do modelo Category foi criada corretamente"""
        self.assertEqual(self.category.label, "Technology")
        self.assertEqual(self.category.path, "tech")

    def test_category_str(self):
        """Testa se o método __str__ de Category retorna o rótulo correto"""
        self.assertEqual(str(self.category), "Technology")

class PostModelTestCase(TestCase):
    def setUp(self):
        # Criando instâncias de Image e Category para associá-las ao Post
        self.image1 = Image.objects.create(
            src="https://example.com/image1.jpg",
            alt="Image 1",
            title="Image Title 1"
        )
        self.image2 = Image.objects.create(
            src="https://example.com/image2.jpg",
            alt="Image 2",
            title="Image Title 2"
        )
        self.category1 = Category.objects.create(
            label="Tech",
            path="tech"
        )
        self.category2 = Category.objects.create(
            label="Lifestyle",
            path="lifestyle"
        )
        # Criando uma instância de Post e associando imagens e categorias
        self.post = Post.objects.create(
            slug="example-post",
            title="Example Post",
            updatedAt=date.today(),
            content="This is the content of the post.",
            seo_title="SEO Title Example",
            seo_description="This is the SEO description.",
            seo_keywords="example, post, seo"
        )
        self.post.images.set([self.image1, self.image2])
        self.post.categories.set([self.category1, self.category2])

    def test_post_creation(self):
        """Testa se a instância do modelo Post foi criada corretamente"""
        self.assertEqual(self.post.title, "Example Post")
        self.assertEqual(self.post.slug, "example-post")
        self.assertEqual(self.post.content, "This is the content of the post.")
        self.assertEqual(self.post.seo_title, "SEO Title Example")
        self.assertEqual(self.post.seo_description, "This is the SEO description.")
        self.assertEqual(self.post.seo_keywords, "example, post, seo")

    def test_post_images(self):
        """Testa se as imagens associadas ao Post estão corretas"""
        self.assertEqual(self.post.images.count(), 2)
        self.assertIn(self.image1, self.post.images.all())
        self.assertIn(self.image2, self.post.images.all())

    def test_post_categories(self):
        """Testa se as categorias associadas ao Post estão corretas"""
        self.assertEqual(self.post.categories.count(), 2)
        self.assertIn(self.category1, self.post.categories.all())
        self.assertIn(self.category2, self.post.categories.all())

    def test_post_str(self):
        """Testa se o método __str__ de Post retorna o título correto"""
        self.assertEqual(str(self.post), "Example Post")