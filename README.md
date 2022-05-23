# Getting Started with TurquoiseAuto django app

The project was bootstrapped with `python manage.py startapp` command

## About

The project is a backend REST api feeder for a ReactJs base blogging application. Functionalities of the project are mentioned below:

- Register user
- Login user
- Logout user
- View articles
- Search articles by username
- Search articles by title

## To run the project in local development environment

Follow the below-mentioned steps to run the application locally in development mode:

- In the main directory of the application within the `settings.py` uncomment the following code:

```python
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
```
- Comment the following code
```python
    'ENGINE': 'django.db.backends.postgresql',
    'HOST': os.environ.get('DATABASE_URL'),
    'NAME': os.environ.get('DATABASE'),
    'USER': os.environ.get('USER'),
    'PASSWORD': os.environ.get('PASSWORD')
```
Reverse the steps for running the project in production environment.
Some sample requests are mentioned below.
### Register user

Url pattern - `https://localhost:8000/api/v1/register`

Request - 
```http request
    POST /api/v1/register HTTP/1.1
    Host: localhost:8000
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Content-Type: application/json

    {
        "username": "test_username",
        "password": "test_password"
    } 
```

Response Body - 
```json
    {
        "success": true,
        "error": null
    } 
```

### Login user

Url pattern - `https://localhost:8000/api/v1/login`

Request - 
```http request
    POST /api/v1/login HTTP/1.1
    Host: localhost:8000
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Content-Type: application/json

    {
        "username": "test_username",
        "password": "test_password"
    } 
```

Response Body - 
```json
    {
        "success": true,
        "error": null
    } 
```

### Logout user

Url pattern - `https://localhost:8000/api/v1/logout`

Request - 
```http request
    GET /api/v1/logout HTTP/1.1
    Host: localhost:8000
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Content-Type: application/json
```

Response Body - 
```json
     
```

### Get articles

Url pattern - `https://localhost:8000/api/v1/get/articles`

Request - 
```http request
    GET /api/v1/get/articles HTTP/1.1
    Host: localhost:8000
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Content-Type: application/json
```

Response Body -

```json
    {
      "success": true,
      "payload": [
        {
          "id": 1,
          "title": "test",
          "content": "test is a test"
        }
      ],
      "error": null
    } 
```

### Get articles by username

Url pattern - `https://localhost:8000/api/v1/get/articles/username/<str:username>`

Request - 
```http request
    GET /api/v1/get/articles/username/test_username HTTP/1.1
    Host: localhost:8000
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Content-Type: application/json
```

Response Body -

```json
    {
      "success": true,
      "payload": [
        {
          "id": 1,
          "title": "test",
          "content": "test is a test"
        }
      ],
      "error": null
    } 
```

### Get articles by title

Url pattern - `https://localhost:8000/api/v1/get/articles/title/<str:title>`

Request - 
```http request
    POST /api/v1/get/articles/title/test HTTP/1.1
    Host: localhost:8000
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Content-Type: application/json
```

Response Body -

```json
    {
      "success": true,
      "payload": [
        {
          "id": 1,
          "title": "test",
          "content": "test is a test"
        }
      ],
      "error": null
    } 
```

### Post Article

Url pattern - `https://localhost:8000/api/v1/post/articles`

Request - 
```http request
    POST /api/v1/post/articles HTTP/1.1
    Host: localhost:8000
    Accept: */*
    Accept-Encoding: gzip, deflate, br
    Connection: keep-alive
    Content-Type: application/json

    {
        "username": "test_username",
        "title": "test_title",
        "content": "hello world"
    }
```

Response Body -

```json
    {
      "success": true,
      "error": null
    } 
```

The project is deployed on heroku, [click here](https://django-backend-turquoise.herokuapp.com/) to visit the api.