from django.core.mail import send_mail


def contactByEmail(subject, message, from_email, recipient_list, html=None):
    if (html):
        send_mail(subject, message, from_email,
                  recipient_list, html_message=html)
    else:
        send_mail(subject, message, from_email,
                  recipient_list)
