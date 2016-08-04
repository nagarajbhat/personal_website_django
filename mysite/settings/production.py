# -*- coding: utf-8 -*-


# """
# Django settings for mysite project.

# Generated by 'django-admin startproject' using Django 1.9.8.

# For more information on this file, see
# https://docs.djangoproject.com/en/1.9/topics/settings/

# For the full list of settings and their values, see
# https://docs.djangoproject.com/en/1.9/ref/settings/
# """
# import os
from django.conf import settings    


DEBUG = False
TEMPLATE_DEBUG = True

DATABASES = settings.DATABASES

# # ALLOWED_HOSTS = ['nagarajbhat.herokuapp.com']
ALLOWED_HOSTS = ['*']


# Update database configuration with $DATABASE_URL.
import dj_database_url
db_from_env = dj_database_url.config()
DATABASES['default'].update(db_from_env)




# STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'



SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')









