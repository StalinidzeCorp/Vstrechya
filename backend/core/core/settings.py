import datetime
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '0.0.0.0']
AUTH_USER_MODEL = 'account.UserAccount'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'djoser',
    'drf_spectacular',

    'account',
    'collection',
    'museum',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

DJOSER = {
    'USER_CREATE_PASSWORD_RETYPE': True,
    'LOGOUT_ON_PASSWORD_CHANGE': True,
    'LOGIN_FIELD': 'email',
    #'PASSWORD_RESET_CONFIRM_URL': 'password/reset/confirm/{uid}/{token}',
    #'USERNAME_RESET_CONFIRM_URL': 'email/reset/confirm/{uid}/{token}',
    'ACTIVATION_URL': 'auth/activate/{uid}/{token}/',
    'SEND_ACTIVATION_EMAIL': False,
    'SERIALIZERS': {
        "user_create": "account.serializers.UserCreateSerializer",
        #'current_user': 'backend.account.serializers.UserSerializer', #for /users/me endpoint
        'user': 'account.serializers.UserSerializer'
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = "smtp.mail.ru"
EMAIL_PORT = 2525
EMAIL_HOST_USER = os.environ.get("EMAIL_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_USE_SSL = False

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
SERVER_EMAIL = EMAIL_HOST_USER
EMAIL_ADMIN = EMAIL_HOST_USER

AWS_SECRET = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_ACCESS = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_URL = 'https://digital-portfolio.hb.ru-msk.vkcs.cloud/'
AWS_ENDPOINT_URL = 'https://hb.ru-msk.vkcs.cloud/'

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

WSGI_APPLICATION = 'core.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'pgdb',
        'PORT': 5432,
    }
}

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis-qoovee/0'",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        # 'rest_framework.permissions.IsAdminUser',
        'rest_framework.permissions.AllowAny',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        #'rest_framework.authentication.TokenAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
}

SIMPLE_JWT = {
    'AUTH_HEADER_TYPES': ('Bearer',),
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(days=2),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=5),
    "UPDATE_LAST_LOGIN": True,
    #"USER_AUTHENTICATION_RULE": "accounts.auth.default_user_authentication_rule",
}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Yats API',
    'DESCRIPTION': 'Yatspace API Endpoints',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}

LANGUAGE_CODE = 'ru'
TIME_ZONE = 'Europe/Moscow'
USE_I18N = True
USE_TZ = True

STATIC_ROOT = ''
STATIC_URL = '/static/'
# STATICFILES_DIRS = ('static',)

MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
