from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UmiShopApi.settings')

if (os.environ.get('DOCKER') == 1):
    app = Celery('UmiShopApi', broker="amqp://rabbitmq")
else:
    app = Celery('UmiShopApi')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
