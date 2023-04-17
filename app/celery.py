import os
from django.conf import settings
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.common")

app = Celery("app")

app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.timezone = settings.TIME_ZONE

from celery.schedules import crontab

CELERY_BEAT_SCHEDULE = {
    "sleepy": {
        "task": "app.tasks.sleepy",
        "schedule": crontab(minute="*/10"),
    },
}
