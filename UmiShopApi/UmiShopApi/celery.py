from __future__ import absolute_import, unicode_literals
import os
from pathlib import Path
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UmiShopApi.settings')

if (os.environ.get('DOCKER') == "0"):
    app = Celery('UmiShopApi')
else:
    app = Celery('UmiShopApi', broker="amqp://rabbitmq")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
