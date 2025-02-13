from pathlib import Path
from django.core.management.utils import get_random_secret_key
from django.conf import settings
import sys
import os


# Build paths inside the project
BASE_DIR = Path(__file__).resolve().parent.parent

# Environment setting
ENV = "dev"


# AUTHENTICATION_BACKENDS = [
#     "zango.auth.backends.ZangoAuthBackend",  # Zango authentication backend
# ]

# Security settings
SECRET_KEY = get_random_secret_key()

DEBUG = True
ALLOWED_HOSTS = []

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'zango.core',
    'zango',
    'workspaces.Issue_Tracker_App.IssueTracker',
]

# Add required middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',    # Required for admin
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Required for admin
    'django.contrib.messages.middleware.MessageMiddleware',    # Required for admin
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Add required template settings
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

ROOT_URLCONF = 'IssueTrackerApplication.urls'
WSGI_APPLICATION = 'IssueTrackerApplication.wsgi.application'

# Database settings
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'IssueTracker',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files
STATIC_URL = 'static/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # Ensure login redirection is set
# LOGIN_REDIRECT_URL = "/"
# LOGOUT_REDIRECT_URL = "/"

# Call setup_settings to initialize the settings
# settings_result = setup_settings(AttrDict(vars()), BASE_DIR)

# Setting Overrides
# Any settings that need to be overridden or added should be done below this line
# to ensure they take effect after the initial setup

# To change the media storage to S3 you can use the BACKEND class provided by the default storage
# To change the static storage to S3 you can use the BACKEND class provided by the staticfiles storage
# STORAGES = {
#     "default": {"BACKEND": "zango.core.storage_utils.S3MediaStorage"},
#     "staticfiles": {"BACKEND": "zango.core.storage_utils.S3StaticStorage"},
# }


# INTERNAL_IPS can contain a list of IP addresses or CIDR blocks that are considered internal.
# Both individual IP addresses and CIDR notation (e.g., '192.168.1.1' or '192.168.1.0/24') can be provided.

# # ROOT_URLCONF = 'IssueTrackerApplication.urls'

# # TEMPLATES = [
# #     {
# #         'BACKEND': 'django.template.backends.django.DjangoTemplates',
# #         'DIRS': [],
# #         'APP_DIRS': True,
# #         'OPTIONS': {
# #             'context_processors': [
# #                 'django.template.context_processors.debug',
# #                 'django.template.context_processors.request',
# #                 'django.contrib.auth.context_processors.auth',
# #                 'django.contrib.messages.context_processors.messages',
# #             ],
# #         },
# #     },
# # ]

# # WSGI_APPLICATION = 'IssueTrackerApplication.wsgi.application'

# # # Internationalization
# # # LANGUAGE_CODE = 'en-us'
# # # TIME_ZONE = 'UTC'
# # # USE_I18N = True
# # # USE_TZ = True

# # # Static files (CSS, JavaScript, Images)
# # # STATIC_URL = 'static/'

# # # Default primary key field type
# # # DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
