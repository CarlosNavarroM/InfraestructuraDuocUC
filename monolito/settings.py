from pathlib import Path
import os
LOGIN_URL = '/login/'

# settings.py
TRANSBANK_COMMERCE_CODE = "597055555532"  # Código de comercio de pruebas
TRANSBANK_API_KEY = "579B532A7440BB0C9079DED94D31EA1615BACEB56610332264630D42D0A36B1C"  # Llave secreta de pruebas
TRANSBANK_ENVIRONMENT = "integration"  # Usar 'integration' para pruebas


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'django-insecure-a86v(!4=@bx^@e@5s1xe98i%bu(aubtyhgs!^t-%ma646^4te4')
DEBUG = os.getenv('DJANGO_DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['localhost', '127.0.0.1', '0.0.0.0']

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'monolito',
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

ROOT_URLCONF = 'monolito.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'monolito' / 'templates'],
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

WSGI_APPLICATION = 'monolito.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',  # Tu nombre de base de datos
        'USER': 'myuser',       # Tu usuario de base de datos
        'PASSWORD': 'mypassword',  # Tu contraseña de base de datos
        'HOST': 'db',    # Conexión docker 'db' / para desarrollo 127.0.0.1
        'PORT': '3306',         # Puerto docker '3306' / para desarrollo 3307
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'monolito' / 'templates' / 'frontend' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files (para imágenes y otros uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'monolito' / 'templates' / 'frontend' / 'static' / 'assets' / 'image'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
