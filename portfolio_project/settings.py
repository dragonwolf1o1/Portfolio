import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def load_credentials(path):
    if not path.exists():
        return

    for line in path.read_text(encoding="utf-8").splitlines():
        clean_line = line.strip()
        if not clean_line or clean_line.startswith("#") or "=" not in clean_line:
            continue

        key, value = clean_line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_credentials(BASE_DIR / ".env.credentails")


def csv_env(name, default=""):
    return [
        value.strip()
        for value in os.getenv(name, default).split(",")
        if value.strip()
    ]


SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "replace-this-dev-only-secret-key")
DEBUG = os.getenv("DJANGO_DEBUG", "True").lower() in {"1", "true", "yes", "on"}
IS_VERCEL = bool(os.getenv("VERCEL") or os.getenv("VERCEL_ENV"))
ALLOWED_HOSTS = csv_env("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost,.vercel.app")
CSRF_TRUSTED_ORIGINS = csv_env("DJANGO_CSRF_TRUSTED_ORIGINS", "https://*.vercel.app")
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
SESSION_COOKIE_SECURE = not DEBUG
CSRF_COOKIE_SECURE = not DEBUG

if IS_VERCEL:
    SESSION_ENGINE = "django.contrib.sessions.backends.signed_cookies"


INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "portfolio",
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


ROOT_URLCONF = "portfolio_project.urls"


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "portfolio.context_processors.site_content",
            ],
        },
    },
]


WSGI_APPLICATION = "portfolio_project.wsgi.application"


DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
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


LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Kolkata"
USE_I18N = True
USE_TZ = True


STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles_build" / "static"
STATICFILES_DIRS = [BASE_DIR / "static"]


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
