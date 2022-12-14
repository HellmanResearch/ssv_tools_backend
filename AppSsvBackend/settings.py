"""
Django settings for AppSsvBackend project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

from . import project_env

ENV = project_env.ENV

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'z!fuj+uc$%7m+&iqnsj%hh#nsp&up)q$082wukaju5h+k^%bd&'# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'rest_framework.authtoken',
    'django_celery_results',
    'django_prometheus',
    'devops_django',
    'ssv',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'AppSsvBackend.urls'

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

WSGI_APPLICATION = 'AppSsvBackend.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
        'devops_django.permissions.ViewLevel',
    ),
    'DEFAULT_PAGINATION_CLASS': 'devops_django.paginations.StandardResultsSetPagination',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    )
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '[{server_time}] {message}',
            'style': '{',
        },
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
            # ????????????
        }
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
        'ssv': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/ssv.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        'tasks': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/tasks.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        'dfinity': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/dfinity.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'encoding': 'utf-8',
            'formatter': 'standard',
        },
        'sync': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/sync.log',
            'maxBytes': 1024 * 1024 * 20,
            'backupCount': 5,
            'encoding': 'utf-8',
            'formatter': 'standard',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
        'django.db': {
            'handlers': ['console'] if ENV != "PRO" else [],
            'level': 'DEBUG',
            'propagate': False,
        },
        'ssv': {
            'handlers': ['ssv'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'tasks': {
            'handlers': ['tasks'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'dfinity': {
            'handlers': ['dfinity'],
            'level': 'DEBUG',
            'propagate': False,
        },
        'sync': {
            'handlers': ['sync'],
            'level': 'DEBUG',
            'propagate': False,
        }
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ssv',
        'USER': 'root',
        'PASSWORD': 'Ipfs@111',
        'HOST': '192.168.1.128',
        'PORT': '3306'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': '/tmp/AppSSVBackendCache',
    }
}

# CELERY_BROKER_URL = "amqp://dfinity_off_chain:dfinity_off_chain,1@192.168.1.128/dfinity_off_chain",
# CELERY_RESULT_BACKEND = "django-db"
# CELERY_PROMETHEUS_PORT = 9112

# DFINITY_NETWORK = "ic"
# DFINITY_NETWORK_ORIGIN = "https://ic0.app"
# DFINITY_WICP_CANISTER_ID = "wiasx-2yaaa-aaaai-aa2wq-cai"
# DFINITY_WICP_STORAGE_CANISTER_ID = "j5d6o-3iaaa-aaaah-qccra-cai"
# DFINITY_ZOMBIE_CANISTER_ID = "46emz-giaaa-aaaah-qcg4q-cai"
# DFINITY_ZOMBIE_STORAGE_ID = "4xhhf-qaaaa-aaaah-qcg5a-cai"
# DFINITY_PAGE_SIZE = 50
# DFINITY_PROJECT_PATH = "/Users/mmt/buf/dfinity_test"
# DFINITY_CALL_WICP_IDENTITY = "wicp_onwer"
# DFINITY_CALL_WICP_STORAGE_IDENTITY = "CCCAphlaOwner"
# DFINITY_CALL_ZOMBIE_IDENTITY = "zombie_test_default"
# DFINITY_CALL_ZOMBIE_STORAGE_IDENTITY = "zombie_test_default"



CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = (
    'accept',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'token',
)
