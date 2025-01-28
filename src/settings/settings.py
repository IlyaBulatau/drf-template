from os import getenv as ENV
from os import makedirs
from pathlib import Path

from rest_framework import ISO_8601


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = ENV("SECRET_KEY")

DEBUG = ENV("DEBUG", None)

ROOT_URLCONF = "settings.urls"

WSGI_APPLICATION = "settings.wsgi.application"

LANGUAGE_CODE = "ru-RU"

TIME_ZONE = "Europe/Minsk"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

APPEND_SLASH = True

FIXTURE_DIRS = ["fixtures"]

if DEBUG:
    ALLOWED_HOSTS = ["*"]
    CORS_ALLOW_ALL_ORIGINS = True
else:
    CSRF_TRUSTED_ORIGINS = ENV("CSRF_TRUSTED_ORIGINS", "").split(",")
    ALLOWED_HOSTS = ENV("ALLOWED_HOSTS", "").split(",")
    CORS_ALLOWED_ORIGINS = ENV("CORS_ALLOWED_ORIGINS", "").split(",")
    CSRF_COOKIE_SECURE = True
    LANGUAGE_COOKIE_HTTPONLY = True
    LANGUAGE_COOKIE_SECURE = True
    USE_X_FORWARDED_HOST = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SECURE = True

CORS_ALLOW_HEADERS = ["*"]

MODULES = ["core", "users"]

THIRD_PARTY_APPS = [
    "rest_framework",
    "django_filters",
    "drf_spectacular",
    "drf_spectacular_sidecar",
    "storages",
    "corsheaders",
    "drf_standardized_errors",
]

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
    "corsheaders.middleware.CorsMiddleware",
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

REDIS_HOST = ENV("REDIS_HOST")
REDIS_PORT = ENV("REDIS_PORT")

CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        },
    }
}

AWS_S3_ENDPOINT_URL = ENV("AWS_S3_ENDPOINT_URL")
AWS_S3_ACCESS_KEY_ID = ENV("AWS_S3_ACCESS_KEY_ID")
AWS_S3_SECRET_ACCESS_KEY = ENV("AWS_S3_SECRET_ACCESS_KEY")
AWS_S3_REGION_NAME = ENV("AWS_S3_REGION_NAME")
AWS_STORAGE_BUCKET_NAME = ENV("AWS_STORAGE_BUCKET_NAME", "static")

DEFAULT_FILE_STORAGE = "storages.backends.s3.S3Storage"
STATICFILES_STORAGE = "storages.backends.s3.S3Storage"


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

AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.ModelBackend",
]

SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 1 week in seconds
SESSION_COOKIE_NAME = "sessionid"
SESSION_SAVE_EVERY_REQUEST = True

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_RENDERER_CLASSES": [
        "rest_framework.renderers.JSONRenderer",
    ],
    "EXCEPTION_HANDLER": "drf_standardized_errors.handler.exception_handler",
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        "rest_framework.parsers.MultiPartParser",
        "rest_framework.parsers.FormParser",
    ],
    "DEFAULT_THROTTLE_CLASSES": ["rest_framework.throttling.AnonRateThrottle"],
    "DEFAULT_THROTTLE_RATES": {"anon": "10/second"},
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
    "SEARCH_PARAM": "search",
    "ORDERING_PARAM": "ordering",
    "DEFAULT_PAGINATION_CLASS": "core.paginators.LimitOffsetPagination",
    "PAGE_SIZE": 100,
    "DEFAULT_VERSION": "v1",
    "DEFAULT_SCHEMA_CLASS": "drf_standardized_errors.openapi.AutoSchema",
    "DATETIME_FORMAT": "%Y-%m-%dT%H:%M:%S.%fZ",
    "DATETIME_INPUT_FORMATS": ["%Y-%m-%dT%H:%M:%S.%fZ", ISO_8601],
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

SPECTACULAR_SETTINGS = {
    "TITLE": "Accounts API",
    "VERSION": "0.0.1",
    "SERVE_INCLUDE_SCHEMA": False,
    "SWAGGER_UI_DIST": "SIDECAR",
    "SWAGGER_UI_FAVICON_HREF": "SIDECAR",
    "REDOC_DIST": "SIDECAR",
    "COMPONENT_SPLIT_REQUEST": True,
    "ENUM_NAME_OVERRIDES": {
        "ValidationErrorEnum": "drf_standardized_errors.openapi_serializers.ValidationErrorEnum.choices",
        "ClientErrorEnum": "drf_standardized_errors.openapi_serializers.ClientErrorEnum.choices",
        "ServerErrorEnum": "drf_standardized_errors.openapi_serializers.ServerErrorEnum.choices",
        "ErrorCode401Enum": "drf_standardized_errors.openapi_serializers.ErrorCode401Enum.choices",
        "ErrorCode403Enum": "drf_standardized_errors.openapi_serializers.ErrorCode403Enum.choices",
        "ErrorCode404Enum": "drf_standardized_errors.openapi_serializers.ErrorCode404Enum.choices",
        "ErrorCode405Enum": "drf_standardized_errors.openapi_serializers.ErrorCode405Enum.choices",
        "ErrorCode406Enum": "drf_standardized_errors.openapi_serializers.ErrorCode406Enum.choices",
        "ErrorCode415Enum": "drf_standardized_errors.openapi_serializers.ErrorCode415Enum.choices",
        "ErrorCode429Enum": "drf_standardized_errors.openapi_serializers.ErrorCode429Enum.choices",
        "ErrorCode500Enum": "drf_standardized_errors.openapi_serializers.ErrorCode500Enum.choices",
    },
    "POSTPROCESSING_HOOKS": ["drf_standardized_errors.openapi_hooks.postprocess_schema_enums"],
}

if DEBUG:
    MIDDLEWARE.append("silk.middleware.SilkyMiddleware")
    INSTALLED_APPS.append("silk")
