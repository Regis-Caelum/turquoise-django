from django.urls import path
from . import views

urlpatterns = [
    path('api/v1/register', views.UserRegister),
    path('api/v1/login', views.UserLogin),
    path('api/v1/logout', views.UserLogout),
    path('api/v1/get/articles', views.GetBlogs),
    path('api/v1/get/articles/username/<str:username>', views.GetBlogByUsername),
    path('api/v1/get/articles/title/<str:title>', views.GetBlogByTitle),
    path('api/v1/post/articles/', views.PostBlog),
]