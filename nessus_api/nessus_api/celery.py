# celery.py
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'nessus_api.settings')

app = Celery('nessus_api')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
