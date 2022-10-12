from .sendEmail import contactByEmail
from django.template.loader import render_to_string


def contactDepartment(data):

    if (data['topic'] == 'Sales'):
        # contactBySlack(data)
        return
    elif (data['topic'] == 'Pricing'):
        message = "the customer " + data['email'] + \
            " had an issue with " + data['topic'] + "."
        contactByEmail('Customer had an issue',
                       message, 'noreply@umishop.com', ['product@umishop.com'])
        return
    else:
        message = "the customer " + data['email'] + \
            " had an issue with unknown topic."
        contactByEmail('Customer had an issue',
                       message, 'noreply@umishop.com', ['product@umishop.com'])
        return

    return
