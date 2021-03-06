import os
gettext = lambda s: s
DATA_DIR = os.path.dirname(os.path.dirname(__file__))
"""
Django settings for djcmsmysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY","")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition





ROOT_URLCONF = 'djcmsmysite.urls'

WSGI_APPLICATION = 'djcmsmysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases



# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Europe/Amsterdam'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(DATA_DIR, 'media')
STATIC_ROOT = os.path.join(DATA_DIR, 'static')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'djcmsmysite', 'static'),
)
SITE_ID = 1

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.doc.XViewMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.i18n',
    'django.core.context_processors.debug',
    'django.core.context_processors.request',
    'django.core.context_processors.media',
    'django.core.context_processors.csrf',
    'django.core.context_processors.tz',
    'sekizai.context_processors.sekizai',
    'django.core.context_processors.static',
    'cms.context_processors.cms_settings'
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'djcmsmysite', 'templates'),
)

INSTALLED_APPS = (
    'djangocms_admin_style',
    'djangocms_text_ckeditor',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.messages',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_style',
    'djangocms_column',
    'djangocms_file',
    'djangocms_flash',
    'djangocms_googlemap',
    'djangocms_inherit',
    'djangocms_link',
    'djangocms_picture',
    'djangocms_teaser',
    'djangocms_video',
    'reversion',
    'djcmsmysite'
)

LANGUAGES = (
    ## Customize this
    ('en', gettext('en')),
    ('de', gettext('de')),
    ('nl', gettext('nl')),
    ('jp', gettext('jp')),
)

CMS_LANGUAGES = {
    ## Customize this
    1: [
        {
            'name': gettext('en'),
            'redirect_on_fallback': True,
            'code': 'en',
            'hide_untranslated': False,
            'public': True,
        },
        {
            'name': gettext('de'),
            'redirect_on_fallback': True,
            'code': 'de',
            'hide_untranslated': False,
            'public': True,
        },
        {
            'name': gettext('nl'),
            'redirect_on_fallback': True,
            'code': 'nl',
            'hide_untranslated': False,
            'public': True,
        },
        {
            'name': gettext('jp'),
            'redirect_on_fallback': True,
            'code': 'jp',
            'hide_untranslated': False,
            'public': True,
        },
    ],
    'default': {
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': False,
    },
}

CMS_TEMPLATES = (
    ## Customize this
    ('fullwidth.html', 'Fullwidth'),
    ('sidebar_left.html', 'Sidebar Left'),
    ('sidebar_right.html', 'Sidebar Right')
)

CMS_PERMISSION = True

CMS_PLACEHOLDER_CONF = {}

on_heroku = False
if 'DYNO' in os.environ:
    on_heroku = True

#DATABASES = {
 #   'default': {
 #       'ENGINE': 'django.db.backends.sqlite3',
 #       'NAME': 'db.sqlite3',
 #   }
#}
if on_heroku:
    import dj_database_url
    DATABASES =  {'default': dj_database_url.config()}
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': os.getenv('DATABASE_NAME', 'superlists'),
            'USER': os.getenv('DATABASE_USER', 'superlists'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD', 'password'),
            'HOST': os.getenv('DATABASE_HOST', '127.0.0.1'),
            'PORT': os.getenv('DATABASE_PORT', '5432'),
        }
    }    



MIGRATION_MODULES = {
    'djangocms_column': 'djangocms_column.migrations_django',
    'djangocms_flash': 'djangocms_flash.migrations_django',
    'djangocms_googlemap': 'djangocms_googlemap.migrations_django',
    'djangocms_inherit': 'djangocms_inherit.migrations_django',
    'djangocms_link': 'djangocms_link.migrations_django',
    'djangocms_style': 'djangocms_style.migrations_django',
    'djangocms_file': 'djangocms_file.migrations_django',
    'djangocms_picture': 'djangocms_picture.migrations_django',
    'djangocms_teaser': 'djangocms_teaser.migrations_django',
    'djangocms_video': 'djangocms_video.migrations_django',
    'cms': 'cms.migrations_django',
}
