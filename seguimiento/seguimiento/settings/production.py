from django.core.exceptions import ImproperlyConfigured

from .base import *


def get_env_variable(var_name):
    """Get the environment variable or return exception."""
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = 'Set the {} environment variable'.format(var_name)
        raise ImproperlyConfigured(error_msg)


SECRET_KEY = get_env_variable('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = ['pislea.bolivia.bo']

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'HOST': '127.0.0.1',
        'NAME': get_env_variable('DATABASES_NAME'),
        'USER': get_env_variable('DATABASES_USER'),
        'PASSWORD': get_env_variable('DATABASES_PASSWORD'),
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

ADMINS = ('ernesto@rico-schmidt.name',)

MANAGERS = ADMINS

SERVER_EMAIL = 'noreply@rico-schmidt.name'

DEFAULT_FROM_EMAIL = 'ernesto@rico-schmidt.name'

SECURE_HSTS_SECONDS = 3600

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

SECURE_SSL_REDIRECT = True

SESSION_COOKIE_SECURE = True

X_FRAME_OPTIONS = 'DENY'

CSRF_COOKIE_SECURE = True

