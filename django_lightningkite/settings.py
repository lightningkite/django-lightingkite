import environ
import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

env = environ.Env()


def settings(BASE_DIR=os.getcwd()):
    # Load operating system environment variables and then prepare to use them
    READ_DOT_ENV_FILE = env.bool('DJANGO_READ_DOT_ENV_FILE', default=True)
    if READ_DOT_ENV_FILE:
        # Operating System Environment variables have precedence over variables defined in the .env file,
        # that is to say variables from the .env files will only be used if not defined
        # as environment variables.
        env_file = os.path.join(BASE_DIR, '.env')
        env.read_env(env_file)

    if env("DJANGO_SECRET_KEY") is None:
        raise Exception(
            'DJANGO_SECRET_KEY must be defined in Environment or .env file')

    # SECRET CONFIGURATION
    # ------------------------------------------------------------------------------
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
    # Raises ImproperlyConfigured exception if DJANGO_SECRET_KEY not in os.environ
    SECRET_KEY = env("DJANGO_SECRET_KEY")

    # DEBUG
    # See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
    DEBUG = env.bool('DJANGO_DEBUG', False)

    # ENVIRONMENT (staging, dev, production etc..)
    ENVIRONMENT = env('DJANGO_ENVIRONMENT', default='production')

    ALLOWED_HOSTS = env('DJANGO_ALLOWED_HOSTS', default=['.localhost'])

    # Sentry
    sentry_sdk.init(
        dsn=env('SENTRY_DSN', default=''),
        integrations=[DjangoIntegration()]
    )

    # Password validation
    # https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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

    # Database
    # https://docs.djangoproject.com/en/2.1/ref/settings/#databases
    protocol = env('DJANGO_DB_ENGINE', default='postgres')
    db = env('DJANGO_DATABASE_NAME', default='postgres')
    user = env('DJANGO_DATABASE_USER', default='postgres')
    host = env('DJANGO_DB_HOST', default='postgres')
    password = env('DJANGO_DATABASE_PASSWORD', default='postgres')
    port = env('DJANGO_DATABASE_PORT', default=5432)

    DATABASES = {
        'default': env.db('DATABASE_URL', default='{}://{}:{}@{}:{}/{}'.format(protocol, user, password, host, port, db)),
    }

    # Internationalization
    # https://docs.djangoproject.com/en/2.0/topics/i18n/
    LANGUAGE_CODE = 'en-us'
    TIME_ZONE = 'UTC'
    USE_L10N = True
    USE_TZ = True

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/2.0/howto/static-files/
    STATIC_ROOT = env('DJANGO_STATIC_ROOT', default=os.path.join(BASE_DIR, 'static'))
    STATIC_URL = env('DJANGO_STATIC_URL', default='/static/')

    # Email
    EMAIL_HOST = env('EMAIL_HOST', default='localhost')
    EMAIL_HOST_USER = env('EMAIL_HOST_USER', default=None)
    EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default=None)
    EMAIL_PORT = env.int('EMAIL_PORT', default=1025)
    EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND',
                        default='django.core.mail.backends.console.EmailBackend')

    # Template loading
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
    return vars()
