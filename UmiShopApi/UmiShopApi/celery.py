from __future__ import absolute_import, unicode_literals
import os
from pathlib import Path
from celery import Celery
import dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
envPath = os.path.join(BASE_DIR, '.env')

dotenv.read_dotenv(envPath)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'UmiShopApi.settings')

if (os.environ.get('DOCKER') == "0"):
    app = Celery('UmiShopApi')
else:
    app = Celery('UmiShopApi', broker="amqp://rabbitmq")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
