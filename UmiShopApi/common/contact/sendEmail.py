from django.core.mail import send_mail


def contactByEmail(subject, message, from_email, recipient_list, html_message=None):
    if (html_message):
        send_mail(subject, message, from_email,
                  recipient_list, html_message=html_message)
    else:
        send_mail(subject, message, from_email,
                  recipient_list)
