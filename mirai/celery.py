# Configure Celery to use the Django settings module
import os
from celery import Celery
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gfg.settings')

app = Celery('mirai')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()