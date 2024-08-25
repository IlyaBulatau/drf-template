from os import getenv as ENV
from os import makedirs
from pathlib import Path

from rest_framework import ISO_8601


VERSION = 1

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ENV("SECRET_KEY")

DEBUG = ENV("DEBUG", None)

ROOT_URLCONF = "settings.urls"

WSGI_APPLICATION = "settings.wsgi.application"

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Minsk"

USE_I18N = False

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Список всех людей, которые получают уведомления об ошибках кода.
ADMINS = []

FIXTURE_DIRS = ["fixtures"]

APPEND_SLASH = True

if not DEBUG:
    CSRF_TRUSTED_ORIGINS = ENV("CSRF_TRUSTED_ORIGINS", "").split(",")

if not DEBUG:
    ALLOWED_HOSTS = ENV("ALLOWED_HOSTS", "").split(",")

if not DEBUG:
    # only https
    CSRF_COOKIE_SECURE = True

if not DEBUG:
    LANGUAGE_COOKIE_HTTPONLY = True

if not DEBUG:
    LANGUAGE_COOKIE_SECURE = True

if not DEBUG:
    USE_X_FORWARDED_HOST = True

if not DEBUG:
    SESSION_COOKIE_HTTPONLY = True

if not DEBUG:
    SESSION_COOKIE_SECURE = True

MODULES = []

THIRD_PARTY_APPS = ["rest_framework", "django_filters", "drf_spectacular"]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    *THIRD_PARTY_APPS,
    *MODULES,
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": ENV("DB_NAME"),
        "USER": ENV("DB_USER"),
        "PASSWORD": ENV("DB_PASSWORD"),
        "HOST": ENV("DB_HOST"),
        "PORT": ENV("DB_PORT"),
    }
}

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly"
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRendere",
    ],
    # набор парсеров при обращении к свойству request.data
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
    ],
    # throttle
    "DEFAULT_THROTTLE_CLASSES": ["rest_framework.throttling.AnonRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {"anon": "10/second"},
    # filter
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "SEARCH_PARAM": "search",
    "ORDERING_PARAM": "ordering",
    # pagination
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    # version
    "DEFAULT_VERSIONING_CLASS": "rest_framework.versioning.NamespaceVersioning",
    "DEFAULT_VERSION": "v1",
    # swagger
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    # datetime format
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S.%fZ",
    "DATETIME_INPUT_FORMATS": ["%Y-%m-%dT%H:%M:%S.%fZ", ISO_8601],
    # encoding
    "UNICODE_JSON": True,
    "COMPACT_JSON": False,
}

makedirs("logs", exist_ok=True)

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,  # не дизейблить остальные логгеры
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse",
        },
        "require_debug_true": {
            "()": "django.utils.log.RequireDebugTrue",
        },
    },
    "formatters": {
        "console": {
            "()": "django.utils.log.ServerFormatter",
            "format": "[{levelname}] {asctime} | {message}",
            "style": "{",
        },
        "file": {
            "format": "[{levelname}] {asctime} | {message} | {exc_info} | {pathname} | {lineno}",
            "style": "{",
        },
        "request": {
            "format": "[{levelname}] {asctime} | {message} | {status_code} | {request}",
            "style": "{",
        },
        "db": {
            "format": "[{levelname}] {asctime} | {message} | {sql} | {duration} | {params}",
            "style": "{",
        },
    },
    "handlers": {
        # консоль
        "console": {"level": "WARNING", "class": "logging.StreamHandler", "formatter": "console"},
        # сервер в консоль
        "django.server.console": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        # сервер в файл
        "django.server.file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "D",
            "interval": 10,
            "formatter": "request",
            "filename": "logs/django.server.log",
        },
        # запросы в консоль
        "django.request.console": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        # запросы в файл
        "django.request.file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "D",
            "interval": 10,
            "formatter": "request",
            "filename": "logs/django.request.log",
        },
        # бд в консоль
        "django.db.backends.console": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        # бд в файд
        "django.db.backends.file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "D",
            "interval": 10,
            "formatter": "db",
            "filename": "logs/django.db.backends.log",
        },
        # секьюрити в консоль
        "django.security.console": {
            "level": "WARNING",
            "class": "logging.StreamHandler",
            "formatter": "console",
        },
        # секьюрити в файл
        "django.security.file": {
            "level": "DEBUG",
            "class": "logging.handlers.TimedRotatingFileHandler",
            "when": "D",
            "interval": 10,
            "formatter": "file",
            "filename": "logs/django.security.log",
        },
        # админу
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console", "mail_admins"],
            "level": "INFO",
        },
        "django.server": {
            "handlers": ["django.server.console", "django.server.file"],
            "propagate": False,  # не наследовать параметры от родителя
        },
        "django.request": {
            "handlers": ["django.request.console", "django.request.file"],
            "propagate": False,
        },
        "django.db.backends": {
            "handlers": ["django.db.backends.console", "django.db.backends.file"],
            "propagate": False,
        },
        "django.security": {
            "handlers": ["django.security.console", "django.security.file"],
            "propagate": False,
        },
    },
}
