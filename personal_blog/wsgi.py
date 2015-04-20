"""
WSGI config for personal_blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "personal_blog.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.conf import settings
if not settings.DEBUG:
    from dj_static import Cling
    from whitenoise.django import DjangoWhiteNoise
    application = DjangoWhiteNoise(application)

