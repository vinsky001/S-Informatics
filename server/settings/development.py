from .base import *

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}

TEST_RUNNER = 'django.test.runner.DiscoverRunner'
TEST_DISCOVER_TOP_LEVEL = BASE_DIR
TEST_DISCOVER_ROOT = BASE_DIR / 'tests'
TEST_DISCOVER_PATTERN = 'test_*.py'


