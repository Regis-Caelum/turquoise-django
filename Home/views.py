from django.contrib.auth.models import User
import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from Home.models import Article
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Register
def UserRegister(request):
    # Method Verification
    if request.method == 'POST':
        userData = json.loads(request.body)

        # DTO Validation
        if RegistrationValidation(userData):
            # create user object
            user = User.objects.create_user(username=userData['username'], password=userData['password'])
            user.save()
            response = JsonResponse({'success': True, 'error': None})
            response.status_code = 201
            return response

        response = JsonResponse({'success': False, 'error': 'Invalid Input'})
        response.status_code = 400
        return response

    response = JsonResponse({'success': False, 'error': 'HttpMethodNotAllowed'})
    response.status_code = 405
    return response


@csrf_exempt
# Login
def UserLogin(request):
    # Method Verification
    if request.method == "POST":
        userData = json.loads(request.body)

        # DTO validation
        if RegistrationValidation(userData):
            # authenticate user
            user = authenticate(username=userData['username'], password=userData['password'])

            if user is not None:
                login(request, user)
                response = JsonResponse({'success': True, 'error': None})
                response.status_code = 200
                return response

            response = JsonResponse({'success': False, 'error': 'Invalid username or password'})
            response.status_code = 401
            return response

    response = JsonResponse({'success': False, 'error': 'HttpMethodNotAllowed'})
    response.status_code = 405
    return response


@csrf_exempt
@login_required(login_url='/api/v1/login')
# Logout
def UserLogout(request):
    logout(request)
    response = JsonResponse({'success': True, 'error': None})
    response.status_code = 200
    return response


# Get all Blogs
def GetBlogs(request):
    # Method Verification
    if request.method == 'GET':
        # Retrieving all articles
        articles = list(Article.objects.all())

        response = JsonResponse({'success': True, 'payload': articles, 'error': None})
        response.status_code = 200
        return response

    response = JsonResponse({'success': False, 'error': 'HttpMethodNotAllowed'})
    response.status_code = 405
    return response


# Get blogs authored by username
def GetBlogByUsername(request, username):
   # Method Verification
    if request.method == 'GET':
        # Retrieving all articles published by username
        articles = list(Article.objects.filter(author__username=username))

        response = JsonResponse({'success': True, 'payload': articles, 'error': None})
        response.status_code = 200
        return response

    response = JsonResponse({'success': False, 'error': 'HttpMethodNotAllowed'})
    response.status_code = 405
    return response


# Get blogs authored by title
def GetBlogByTitle(request, title):
    # Method Verification
    if request.method == 'GET':
        # Retrieving all articles containing title
        articles = list(Article.objects.filter(title__contains=title))

        response = JsonResponse({'success': True, 'payload': articles, 'error': None})
        response.status_code = 200
        return response

    response = JsonResponse({'success': False, 'error': 'HttpMethodNotAllowed'})
    response.status_code = 405
    return response


@login_required(login_url='/api/v1/login')
# Post blog authored by username
def PostBlog(request):
    # Method Verification
    if request.method == 'POST':
        requestJson = json.loads(request.body)

        # Validating article DTO
        if ArticleValidation(requestJson):
            # Retrieving user by username
            author = User.objects.get(username=requestJson['username'])

            # Creating Article
            article = Article.objects.create(title=requestJson['title'], author=author, content=requestJson['content'])
            article.save()

            response = JsonResponse({'success': True, 'error': None})
            response.status_code = 200
            return response

        response = JsonResponse({'success': False, 'error': 'InternalServerError'})
        response.status_code = 500
        return response

    response = JsonResponse({'success': False, 'error': 'HttpMethodNotAllowed'})
    response.status_code = 405
    return response


# User Registration DTO Validation Function
def RegistrationValidation(userData):
    if userData['username'] == '' or userData['username'] is None or userData['password'] == '' or userData[
        'password'] is None:
        return False
    return True


# Article DTO validation Function
def ArticleValidation(articleData):
    if articleData['title'] == '' or articleData['title'] is None or articleData['content'] != '' or articleData[
        'content'] is None or articleData['username'] == '' or articleData['username'] is None:
        return False
    return True
