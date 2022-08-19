"""
Base settings to build other settings files upon.
"""
from pathlib import Path
import os

ROOT_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = str(ROOT_DIR) + "/apps/"



DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sites",
    "django.contrib.postgres",
]

LOCAL_APPS = [
    "apps.user.apps.UserConfig",
    "apps.rating.apps.RatingConfig",
    "apps.comment.apps.CommentConfig",
    "apps.post.apps.PostConfig",
]
THIRD_PARTY_APPS = [
    "phonenumber_field",
    "rest_framework",
    "imagekit",
    'oauth2_provider',
    
]

INSTALLED_APPS = DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["front-end/templates/"],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.copostm/en/3.2/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
        'PORT': os.environ.get('POSTGRES_PORT'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/front-end/static/'
STATICFILES_DIRS = (
    os.path.join(os.path.join(str(ROOT_DIR), 'front-end'), 'static'),
)
# https://docs.djangoproject.com/en/4.0/ref/settings/#std-setting-MEDIA_ROOT

MEDIA_ROOT = os.path.join(os.path.join(str(ROOT_DIR), 'front-end'), 'media')
MEDIA_URL = '/front-end/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = "user.User"

SITE_ID=1



REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 50
}

# PHONE_VERIFICATION = {
#     "BACKEND": "config.phoneValidation.backends.twilio.TwilioBackend",
#     "OPTIONS": {
#         "SID": os.environ.get('PHONE_VERIFICATION_SID'),
#         "SECRET": os.environ.get('PHONE_VERIFICATION_TOKEN'),
#         "FROM": os.environ.get('PHONE_VERIFICATION_PHONE_NUMBER'),
#         # "SANDBOX_TOKEN": os.environ.get('PHONE_VERIFICATION_TOKEN'),
#     },
#     "TOKEN_LENGTH": 6,
#     "MESSAGE": "Welcome to {app}! Please use security code {security_code} to proceed.",
#     "APP_NAME": "AnonRate",
#     "SECURITY_CODE_EXPIRATION_TIME": 3600,  # In seconds only
#     "VERIFY_SECURITY_CODE_ONLY_ONCE": False,  # If False, then a security code can be used multiple times for verification
# }