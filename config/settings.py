from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-=&l*li&=rn!@$a^68y2khfq&w5zms466gvace@6_xa)kh=)%%+'
DEBUG = True
ROOT_URLCONF = 'config.urls'
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Tehran'
USE_I18N = True
USE_TZ = True
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
STATIC_URL = 'static/'
STATIC_ROOT_PATH = BASE_DIR / "storage/static"
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'storage/media'
AUTH_USER_MODEL = "accounts.User"
ALLOWED_HOSTS = []
CACHE_MIDDLEWARE_SECONDS = 5 * 60

APPLICATIONS = ['core', 'book', 'accounts']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party applications:
    "rest_framework",

    # Applications:
    *list(map(lambda app: f"apps.{app}", APPLICATIONS)),
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # 'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'apps.core.middleware.ResponseTimeMiddleware',
    'apps.core.middleware.DailyVisitMiddleware',
    'apps.core.middleware.UserActivityMiddleware',
    # 'apps.core.middleware.simple_middleware'
    # 'apps.core.middleware.SimpleMiddleware'
    # 'apps.core.middleware.BetterSimpleMiddleware'
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    # "activity": {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'activity-db.sqlite3',
    # }
}

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

CACHES = {
    # "default": {
    #     "BACKEND": "django.core.cache.backends.db.DatabaseCache",
    #     "LOCATION": "my_cache_table",
    # }
    "default": {
        "BACKEND": "django.core.cache.backends.filebased.FileBasedCache",
        "LOCATION": BASE_DIR / "cached_file",
    }
}

# DATABASE_ROUTERS = ["apps.core.db_router.CoreRouter"]

if DEBUG:
    STATICFILES_DIRS = [
        STATIC_ROOT_PATH,
    ]
else:
    STATIC_ROOT = STATIC_ROOT_PATH


DATETIME_FORMAT = "%Y/%b/%d %H:%M:%S"