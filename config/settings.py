"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

from datetime import timedelta
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
USE_TZ = True
USE_I18N = True
TIME_ZONE = config("TIME_ZONE", default="Asia/Tehran")
LANGUAGE_CODE = 'en-us'
ROOT_URLCONF = 'config.urls'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DEBUG = config("DEBUG", cast=bool, default=True)
WSGI_APPLICATION = 'config.wsgi.application'
SECRET_KEY = config("SECRET_KEY", default="&(dj-hamidreza-secret_key%%django^^:):(//)$")
# media
MEDIA_URL = 'storage/media/'
STATIC_URL = 'storage/static/'
MEDIA_ROOT = BASE_DIR / 'storage/media'
STATIC_ROOT_PATH = BASE_DIR / "storage/static"
# media
ALLOWED_HOSTS = ["*"] if DEBUG else config("ALLOWED_HOSTS", cast=lambda hosts: hosts.split(','))
AUTH_USER_MODEL = 'account.User'

# Application definition
MY_APPS = ['core', 'comment', 'account', 'advertising', 'favorite', 'payment']
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # manager apps
    'rest_framework',
    'rest_framework_simplejwt',
    'drf_spectacular',
    # my_apps
    *list(map(lambda app: f'apps.{app}', MY_APPS))

]

# cash verify

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

if DEBUG:
    # Static
    STATICFILES_DIRS = [
        STATIC_ROOT_PATH,
    ]

    # Email
    # EMAIL_HOST = "smtp4dev"
    # EMAIL_PORT = 2525
    # EMAIL_HOST_USER = ""
    # EMAIL_HOST_PASSWORD = ""
    # EMAIL_USE_TLS = False

    EMAIL_HOST = 'smtp.gmail.com'  # e.g., 'smtp.gmail.com' for Gmail
    EMAIL_PORT = 587  # Use 465 for SSL
    EMAIL_USE_TLS = True  # Use True for TLS, False for SSL
    EMAIL_HOST_USER = 'hamedreza1992@gmail.com'
    EMAIL_HOST_PASSWORD = 'qmkj yfdk gmti bges'
    DEFAULT_FROM_EMAIL = 'hamedreza1992@gmail.com'

    # Database

    # DATABASES = {
    #     'default': {
    #         'ENGINE': 'django.db.backends.sqlite3',
    #         'NAME': BASE_DIR / 'db.sqlite3',
    #     }
    # }
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('POSTGRES_DB', default='postgres'),
            'USER': config('POSTGRES_USER', default='postgres'),
            'PASSWORD': config('POSTGRES_PASSWORD', default='<PASSWORD>'),
            'HOST': config('DB_HOST', default='db'),
            'PORT': config('POSTGRES_PORT', default='5432'),
        }
    }
    REDIS_HOST = config("REDIS_HOST")
    REDIS_PORT = config("REDIS_PORT")
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

    # Cache
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_URL,
        }
    }

    CORS_ALLOW_ALL_ORIGINS = True
else:
    # Statics
    STATIC_ROOT = STATIC_ROOT_PATH

    # Email
    EMAIL_HOST = config("EMAIL_HOST")
    EMAIL_PORT = config("EMAIL_PORT", cast=int)
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = config("EMAIL_USE_TLS", cast=bool)

    REDIS_HOST = config("REDIS_HOST")
    REDIS_PORT = config("REDIS_PORT")
    REDIS_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/0"

    # Database
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': config('POSTGRES_DB', default='postgres'),
            'USER': config('POSTGRES_USER', default='postgres'),
            'PASSWORD': config('POSTGRES_PASSWORD', default='<PASSWORD>'),
            'HOST': config('DB_HOST', default='db'),
            'PORT': config('POSTGRES_PORT', default='5432'),
        }
    }

    # Cache
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": REDIS_URL,
        }
    }

    # Security params:
    SECURE_HSTS_SECONDS = 12 * 30 * 24 * 60 * 60
    SECURE_HSTS_PRELOAD = True
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_SSL_REDIRECT = True
    SECURE_PROXY_SSL_HEADER = "HTTP_X_FORWARDED_PROTO", "https"
    USE_X_FORWARDED_HOST = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_REFERRER_POLICY = "strict-origin"
    X_FRAME_OPTIONS = "SAMEORIGIN"
    SESSION_COOKIE_AGE = 3 * 60 * 60
    SESSION_TIMEOUT = 24 * 60 * 60

    # CORS params
    CORS_ALLOW_ALL_ORIGINS = False
    CORS_ALLOWED_ORIGINS = config(
        "ALLOWED_HOSTS",
        cast=lambda hosts: hosts.split(','),
        default="http://0.0.0.0:8000, http://localhost:8000"
    )

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

# put on your settings.py file below INSTALLED_APPS
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 9,

    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],

    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',  # swager

}
# swager
# SPECTACULAR_SETTINGS = {
#     'TITLE': 'DIVAR',
#     'DESCRIPTION': ' it is divar project',
#     'VERSION': '1.0.0',
#     'SERVE_INCLUDE_SCHEMA': False,
#     # OTHER SETTINGS
# }
# end swager
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=120),
    'SLIDING_TOKEN_REFRESH_LIFETIME': timedelta(days=10),
}

REDIS_HOST = config("REDIS_HOST")
REDIS_PORT = config("REDIS_PORT")
# Celery conf
CELERY_BROKER_URL = f"redis://{REDIS_HOST}:{REDIS_PORT}/15"

# CELERY_RESULT_BACKEND = f"redis://{REDIS_HOST}:{REDIS_PORT}/15"
# CELERY_ACCEPT_CONTENT =config('CELERY_ACCEPT_CONTENT', default=True, cast=lambda contents:contents.split(',') )
# CELERY_TASK_SERIALIZER = config('CELERY_TASK_SERIALIZER', default='json')
# CELERY_RESULT_SERIALIZER = config('CELERY_RESULT_SERIALIZER', default='json')
# CELERY_TIMEZONE = config('CELERY_TIMEZONE', default='UTC')


# SIMPLE_JWT = {
#     'TOKEN_OBTAIN_SERIALIZER': 'apps.core.custom_token.CustomTokenObtainPairSerializer',
# }
# AUTHENTICATION_BACKENDS = [
#     "django.contrib.auth.backends.ModelBackend",
#     'apps.account.model_backends.CustomUserBackend'
# ]
# ZARINPALL
# SANDBOX  =  True
# CALL_BACK_URL = 'http://localhost:8000/comment/verify/'
# MERCHANT = "00000000-0000-0000-0000-000000000000"
# ZP_API_REQUEST = f"https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
# ZP_API_VERIFY = f"https://sandbox.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
# ZP_API_STARTPAY = f"https://sandbox.zarinpal.com/pg/StartPay/"
