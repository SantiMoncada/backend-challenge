from __future__ import absolute_import, unicode_literals
from celery import shared_task
from celery.utils.log import get_task_logger

from UmiShopApi.celery import app
from common.contact.sendEmail import contactByEmail

logger = get_task_logger(__name__)


@app.task
def send_email():
    contactByEmail()
    logger.info("email sent")
    return "helllou"
