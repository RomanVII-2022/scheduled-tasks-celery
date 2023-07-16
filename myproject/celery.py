from __future__ import absolute_import, unicode_literals
import os
from django.conf import settings
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')

app = Celery('myproject')

app.conf.enable_utc = False

app.conf.update(timezone='Africa/Nairobi')

app.config_from_object(settings, namespace='CELERY')

app.conf.beat_schedule = {
    'sheduled_email_now': {
        'task': 'myapp.tasks.scheduled_mail',
        'schedule': crontab(hour=9, minute=53),
    }
}

app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')