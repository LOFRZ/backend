import os
import environ
from pathlib import Path
from datetime import timedelta

import cloudinary
import cloudinary.uploader
import cloudinary.api

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env()
environ.Env.read_env(str(BASE_DIR / ".env.dev"))

# Security
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = bool(int(os.environ.get("DEBUG", 0)))
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(" ")

# Custom User model
AUTH_USER_MODEL = 'useraccount.User'
SITE_ID = 1

# Website URL (used if needed elsewhere)
WEBSITE_URL = os.environ.get("WEBSITE_URL", "http://localhost:8000")

# JWT settings
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=60),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=7),
    "ROTATE_REFRESH_TOKEN": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": True,
    "SIGNING_KEY": "acomplexkhey",
    "ALGORITHM": "HS512",
}

# REST Auth
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = None

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    )
}

REST_AUTH = {
    "USE_JWT": True,
    "JWT_AUTH_HTTPONLY": False
}

# Cloudinary
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': os.environ.get('CLOUDINARY_CLOUD_NAME'),
    'API_KEY': os.environ.get('CLOUDINARY_API_KEY'),
    'API_SECRET': os.environ.get('CLOUDINARY_API_SECRET'),
}
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Static & media
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# Middleware
MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Installed apps
INSTALLED_APPS = [
    'daphne',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_simplejwt',

    'allauth',
    'allauth.account',

    'dj_rest_auth',
    'dj_rest_auth.registration',

    'corsheaders',

    'chat',
    'property',
    'useraccount',

    'cloudinary',
    'cloudinary_storage',
]

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Channels
ASGI_APPLICATION = 'djangobnb_backend.asgi.application'
WSGI_APPLICATION = 'djangobnb_backend.wsgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    },
}

# Database
DATABASES = {
    'default': {
        'ENGINE': os.environ.get("SQL_ENGINE"),
        'NAME': os.environ.get("SQL_DATABASE"),
        'USER': os.environ.get("SQL_USER"),
        'PASSWORD': os.environ.get("SQL_PASSWORD"),
        'HOST': os.environ.get("SQL_HOST"),
        'PORT': os.environ.get("SQL_PORT"),
    }
}

# Password validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# i18n
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# CORS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True              

CSRF_TRUSTED_ORIGINS = [
    'http://127.0.0.1:8000',
    'http://127.0.0.1:3000',
    'https://airbnb-clone-g42s.vercel.app',
    'https://airbnb-clone-g42s-2z5zxswed-issou24s-projects.vercel.app',
    'https://airbnb-clone-2-957822787686.europe-west9.run.app',
]




# Auto primary key
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
