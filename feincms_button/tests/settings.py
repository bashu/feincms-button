SECRET_KEY = "DUMMY_SECRET_KEY"  # noqa: S105

# Application definition

PROJECT_APPS = ["feincms_button.tests", "feincms_button"]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.admin",
    "django.contrib.staticfiles",
    "feincms",
    "feincms.module.medialibrary",
    "feincms.module.page",
    "mptt",
    *PROJECT_APPS,
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "APP_DIRS": True,
    },
]

ROOT_URLCONF = "feincms_button.tests.urls"

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = "/static/"
