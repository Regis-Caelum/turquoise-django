from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/register', views.UserRegister, name='register'),
    path('api/v1/login', views.UserLogin, name='login'),
    path('api/v1/logout', views.UserLogout, name='logout'),
    path('api/v1/get/articles', views.GetBlogs, name='getBlogs'),
    path('api/v1/get/articles/username/<str:username>', views.GetBlogByUsername, name='getBlogByUsername'),
    path('api/v1/get/articles/title/<str:title>', views.GetBlogByTitle, name='getBlogByTitle'),
    path('api/v1/post/articles', views.PostBlog, name='postBlog'),
]