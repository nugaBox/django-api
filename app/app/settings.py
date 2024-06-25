from pathlib import Path
import os

# Default
BASE_DIR = Path(__file__).resolve().parent.parent
HOME_DIR = Path(__file__).resolve().parent.parent.parent
SECRET_KEY = 'django-insecure-34fif6ixo5)ey$azx^kf8ok6me#wmbq*%%0mgt1ym%n5jyev1c'
DEBUG = False


# 호출 허용된 주소
ALLOWED_HOSTS = ['*']


# HTTPS 허용
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# CORS
CORS_ORIGIN_WHITELIST = []
CORS_ALLOW_CREDENTIALS = True


# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'api'
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

ROOT_URLCONF = 'app.urls'

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

WSGI_APPLICATION = 'app.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
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


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Seoul'
USE_I18N = True
USE_TZ = True


# Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# if DEBUG:
#     STATICFILES_DIRS = [
#         os.path.join(BASE_DIR, 'static'),
#     ]
# else:
#     STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Public files (CSS, JavaScript, Images)
PUBLIC_ROOT = 'public/'


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s:%(message)s'
        }
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'file': {
            'level': 'DEBUG',
            'encoding': 'utf-8',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': BASE_DIR / 'logs/django-out.log',
            'when': "midnight",  # 매 자정마다
            'backupCount': 180,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'api': {
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}