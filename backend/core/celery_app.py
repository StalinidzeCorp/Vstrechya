import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')
app.config_from_object('django.conf:settings')
app.conf.broker_url = 'redis://redis-qoovee/1'
app.conf.result_backend = 'redis://redis-qoovee/1'
app.autodiscover_tasks()
