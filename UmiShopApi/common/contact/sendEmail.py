from django.core.mail import send_mail
from django.template.loader import render_to_string


def contactByEmail(data):
    html = render_to_string('emails/welcomeEmail.html', {
        'name': data['name']
    })
    send_mail('test shubject', 'coollest message',
              'noreply@umihop.com', [data['email']], html_message=html)
