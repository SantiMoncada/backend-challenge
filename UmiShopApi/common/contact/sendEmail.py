from django.core.mail import send_mail
from django.template.loader import render_to_string


def contactByEmail():

    html = render_to_string('emails/contactDepartment.html', {
        'name': 'test name',
        'content': 'Lorem impsum'
    })
    send_mail('test shubject', 'coollest message',
              'santiarcos2000@gmail.com', ['santiarcos2000@gmail.com'], html_message=html)
