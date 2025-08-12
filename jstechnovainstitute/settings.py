from pathlib import Path
from dotenv import load_dotenv
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()


SECRET_KEY = os.environ['SECRET_KEY']
PRODUCTION = os.environ["PRODUCTION"]  # whether production of developement

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = (PRODUCTION == 'N')  # debug = False if production server

ALLOWED_HOSTS = ["*"] if DEBUG else ["www.institute.jstechnova.in", "institute.jstechnova.in"]

CSRF_TRUSTED_ORIGINS = [] if DEBUG else ["https://www.institute.jstechnova.in","https://institute.jstechnova.in"]
CSRF_COOKIE_SECURE = True
CSRF_COOKIE_NAME = "institute_csrftoken"
CSRF_COOKIE_PATH = "institute.jstechnova.in/"
# Application definition

INSTALLED_APPS = [
    'django_database_prefix',    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'institute',
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

ROOT_URLCONF = 'jstechnovainstitute.urls'

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

WSGI_APPLICATION = 'jstechnovainstitute.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "OPTIONS": {
            "user": os.environ['DB_USER'],
            "database": os.environ['DB_NAME'],
            "password": os.environ['DB_PASS'],
        },
    }
}

DB_PREFIX = "jstechnova_institute_"

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = "/home/azhm1wt0yj3c/public_html/institute.jstechnova.in/static"

MEDIA_URL = 'media/'
MEDIA_ROOT = "/home/azhm1wt0yj3c/public_html/institute.jstechnova.in/media"
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]
