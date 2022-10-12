from __future__ import absolute_import, unicode_literals
from celery.utils.log import get_task_logger

from UmiShopApi.celery import app
from common.contact.sendEmail import contactByEmail

from django.template.loader import render_to_string

logger = get_task_logger(__name__)


@app.task
def send_email(data):
    html = render_to_string('emails/welcomeEmail.html', {
        'name': data['name']
    })
    contactByEmail('Welcome', 'Welcome to Umi Shop',
                   'noreply@umishop.com', [data['email']], html_message=html)
    logger.info("email sent")
    return True
