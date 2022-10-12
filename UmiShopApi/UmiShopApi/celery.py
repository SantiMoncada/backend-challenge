from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UmiShopApi.settings')

app = Celery('UmiShopApi', broker="amqp://rabbitmq")
# app = Celery('UmiShopApi') #TODO env uncomment for local run outside docker

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
