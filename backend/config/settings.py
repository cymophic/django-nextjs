from pathlib import Path

import dj_database_url
from decouple import Csv, config
from django.core.management.utils import get_random_secret_key
from django.templatetags.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

# ------------------------------------
# Base Directory and Environment
# ------------------------------------
BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------
# Security
# ------------------------------------
DEBUG = config("DEBUG", default=True, cast=bool)
ALLOWED_HOSTS = config("ALLOWED_HOSTS", cast=Csv())

if DEBUG:
    SECRET_KEY = config("SECRET_KEY", default="") or get_random_secret_key()
    ALLOWED_HOSTS += ["127.0.0.1", "localhost"]
    ALLOWED_HOSTS = list(set(ALLOWED_HOSTS))
else:
    SECRET_KEY = config("SECRET_KEY")

# ------------------------------------
# Database Configuration
# ------------------------------------
DATABASES = {}

if DEBUG:
    # Use local database for development
    DEV_DB_URL = config("DATABASE_DEV")
    DATABASES["default"] = dj_database_url.parse(DEV_DB_URL)

else:
    # Use production database for production
    PROD_DB_URL = config("DATABASE_PROD")
    DATABASES["default"] = dj_database_url.parse(PROD_DB_URL, conn_max_age=600)

# ------------------------------------
# Applications
# ------------------------------------
INSTALLED_APPS = [
    # Third-party Packages
    "unfold",
    "corsheaders",
    # Core Django Apps
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Project Apps
]

# ------------------------------------
# Middleware
# ------------------------------------
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "corsheaders.middleware.CorsMiddleware",  # CORS Middleware
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# ------------------------------------
# URL & WSGI
# ------------------------------------
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

# ------------------------------------
# Templates
# ------------------------------------
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# ------------------------------------
# Password Validation
# ------------------------------------
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

# ------------------------------------
# Internationalization
# ------------------------------------
TIME_ZONE = "Asia/Manila"

LANGUAGE_CODE = "en-us"
USE_I18N = True
USE_TZ = True

# ------------------------------------
# Static & Media Files
# ------------------------------------
STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]
if DEBUG:
    STATIC_ROOT = BASE_DIR / "staticfiles"
else:
    STATIC_ROOT = config("STATIC_ROOT")

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"

# ------------------------------------
# Default Primary Key
# ------------------------------------
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ------------------------------------
# CORS Configuration
# ------------------------------------
if DEBUG:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ]
else:
    CORS_ALLOWED_ORIGINS = config("CSRF_TRUSTED_ORIGINS", cast=Csv())

CORS_ALLOW_CREDENTIALS = True

# ------------------------------------
# Unfold Configuration
# ------------------------------------
UNFOLD = {
    "SITE_TITLE": "Site Admin",
    "SITE_HEADER": "Site Admin",
    "SITE_SUBHEADER": "Django Admin Panel",
    "THEME": "light",
    "SITE_URL": "/",
    "COLORS": {
        "primary": {
            "50": "#fafafa",
            "100": "#f5f5f5",
            "200": "#e5e5e5",
            "300": "#d4d4d4",
            "400": "#a3a3a3",
            "500": "#737373",
            "600": "#525252",
            "700": "#404040",
            "800": "#262626",
            "900": "#171717",
            "950": "#0a0a0a",
        },
    },
    "SIDEBAR": {
        "show_search": True,
        "show_all_applications": False,
        "navigation": [
            {
                "title": _("Overview"),
                "items": [
                    {
                        "link": reverse_lazy("admin:index"),
                        "title": _("Dashboard"),
                        "icon": "dashboard",
                        "permission": lambda request: request.user.is_authenticated,
                    },
                ],
            },
            {
                "title": _("Users & Roles"),
                "collapsible": True,
                "permission": lambda request: request.user.is_superuser,
                "items": [
                    {
                        "link": reverse_lazy("admin:auth_user_changelist"),
                        "title": _("Users"),
                        "icon": "person",
                        "permission": lambda request: request.user.is_authenticated,
                    },
                    {
                        "link": reverse_lazy("admin:auth_group_changelist"),
                        "title": _("Groups"),
                        "icon": "admin_panel_settings",
                        "permission": lambda request: request.user.is_authenticated,
                    },
                ],
            },
        ],
    },
}
