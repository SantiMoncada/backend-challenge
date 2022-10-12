from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger

from UmiShopApi.celery import app
from common.contact.contactDepartment import contactDepartment

logger = get_task_logger(__name__)


@app.task
def contact_product(data):
    # TODO check for fields
    contactDepartment(data)
    logger.info("notification sent")
    return True
