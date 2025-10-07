# trackher/settings_ci.py
from .settings import *  # reuse your normal settings

# Use SQLite in CI so tests run anywhere
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "test_db.sqlite3",
    }
}

# Make CI predictable even if SECRET_KEY isn't set
SECRET_KEY = globals().get("SECRET_KEY", "ci-secret-key")
DEBUG = False
ALLOWED_HOSTS = ["*"]
