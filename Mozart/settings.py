from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP

import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(os.path.realpath(__file__))

SECRET_KEY = os.environ.get("MOZART_SECRET_KEY", None)

DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = (
    os.path.join(PROJECT_PATH,'templates'),
)

ALLOWED_HOSTS = ['*']

INSTALLED_APPS = (
    'djangular',
    'material',
    'material.admin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'sorl.thumbnail',
    'django_countries',
    'haystack',
    'rest_framework',
    'social.apps.django_app.default',
    'disqus',
    'Thirdauth',
    'Works',
    'Profiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.static',
    'django.core.context_processors.tz',
    'django.contrib.messages.context_processors.messages',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    'django.core.context_processors.request',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

ROOT_URLCONF = 'Mozart.urls'

WSGI_APPLICATION = 'Mozart.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1

STATIC_URL = '/static/'
STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = (
    os.path.join(PROJECT_PATH,'static/dist'),
)

MEDIA_ROOT = os.path.join(PROJECT_PATH,'media')
MEDIA_URL = '/media/'

THUMBNAIL_DEBUG = True

LOGIN_REDIRECT_URL = 'works:work_list'
LOGIN_URL = 'login'

#Facebook Keys
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("MOZART_SOCIAL_AUTH_FACEBOOK_KEY", None)
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("MOZART_SOCIAL_AUTH_FACEBOOK_SECRET", None)

# Twitter Keys
SOCIAL_AUTH_TWITTER_KEY = os.environ.get("MOZART_SOCIAL_AUTH_TWITTER_KEY", None)
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get("MOZART_SOCIAL_AUTH_TWITTER_SECRET", None)

# Google Keys
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get("MOZART_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY", None)
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get("MOZART_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET", None)

# Social Auth Pipeline
SOCIAL_AUTH_PIPELINE = (    
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'Thirdauth.pipeline.save_extra_params',
)

# Disqus Keys
DISQUS_API_KEY = os.environ.get("DISQUS_API_KEY", None)
DISQUS_WEBSITE_SHORTNAME = os.environ.get("DISQUS_WEBSITE_SHORTNAME", None)

HAYSTACK_CONNECTIONS = {
    'default': {
        'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
        'URL': 'http://mozart.com:8000/',
        'INDEX_NAME': 'haystack',
    },
}
