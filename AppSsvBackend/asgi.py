"""
ASGI config for AppSsvBackend project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
from . import project_env

from django.core.asgi import get_asgi_application

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'AppSsvBackend.settings')

settings = project_env.get_django_settings()
os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings)

application = get_asgi_application()
