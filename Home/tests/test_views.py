from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from Home.models import Article


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.getBlogs_url = reverse('getBlogs')
        self.getBlogByUsername_url = reverse('getBlogByUsername', args=['some-slug'])
        self.getBlogByTitle_url = reverse('getBlogByTitle', args=['some-slug'])
        self.postBlogs_url = reverse('postBlog')
        self.demoUser = User.objects.create_user(username='test1', password='test2')
        self.client.force_login(self.demoUser)
        self.demoArticle = Article.objects.create(title='Hello World', content='kasweufghuergfcyuvegrdy78wg')

    def test_home_register_POST_user_is_created(self):
        response = self.client.post(self.register_url, {
            'username': 'test_username',
            'password': 'test_password'
        }, content_type='application/json')

        self.assertEquals(response.status_code, 201)

    def test_home_getBlogs_GET(self):
        response = self.client.get(self.getBlogs_url)

        self.assertEqual(response.status_code, 200)

    def test_home_getBlogsByUsername_GET(self):
        response = self.client.get(self.getBlogByUsername_url)

        self.assertEqual(response.status_code, 200)

    def test_home_getBlogsByTitle_GET(self):
        response = self.client.get(self.getBlogByTitle_url)

        self.assertEqual(response.status_code, 200)

    def test_home_postBlogs_POST_article_is_created(self):
        response = self.client.post(self.postBlogs_url, {
            'username': self.demoUser.username,
            'title': 'hello',
            'content': 'sfhoesawhfoehr'
        }, content_type='application/json')

        article = Article.objects.get(title__exact='hello')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(article.author.first().username, self.demoUser.username)
