from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Home.views import UserLogout, UserLogin, UserRegister, PostBlog, GetBlogs, GetBlogByUsername, GetBlogByTitle


class TestUrls(SimpleTestCase):

    def test_register_urls_is_resolves(self):
        url = reverse('register')
        result = resolve(url)
        self.assertEqual(result.func, UserRegister)

    def test_login_urls_is_resolves(self):
        url = reverse('login')
        result = resolve(url)
        self.assertEqual(result.func, UserLogin)

    def test_logout_urls_is_resolves(self):
        url = reverse('logout')
        result = resolve(url)
        self.assertEqual(result.func, UserLogout)

    def test_getBlogs_urls_is_resolves(self):
        url = reverse('getBlogs')
        result = resolve(url)
        self.assertEqual(result.func, GetBlogs)

    def test_getBlogByUsername_urls_is_resolves(self):
        url = reverse('getBlogByUsername', args=['some-slug'])
        result = resolve(url)
        self.assertEqual(result.func, GetBlogByUsername)

    def test_getBlogByTitle_urls_is_resolves(self):
        url = reverse('getBlogByTitle', args=['some-slug'])
        result = resolve(url)
        self.assertEqual(result.func, GetBlogByTitle)

    def test_postBlog_urls_is_resolved(self):
        url = reverse('postBlog')
        result = resolve(url)
        self.assertEqual(result.func, PostBlog)
