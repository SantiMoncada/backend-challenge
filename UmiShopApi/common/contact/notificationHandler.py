from .sendEmail import contactByEmail
from .sendSlack import contactBySlack


def notificationHandler(data):

    if (data['topic'] == 'Sales'):
        message = "Hi, customer: " + data['email'] + \
            " had an issue with " + data['topic'] + \
            " resides on " + data['address']
        contactBySlack('product', message)
        return
    elif (data['topic'] == 'Pricing'):
        message = "Hi, customer: " + data['email'] + \
            " had an issue with " + data['topic'] + \
            " resides on " + data['address']
        contactByEmail('Customer had an issue',
                       message, 'noreply@umishop.com', ['product@umishop.com'])
        return
    else:
        message = "the customer " + data['email'] + \
            " had an issue with unknown topic " + \
            " resides on " + data['address']
        contactByEmail('Customer had an issue',
                       message, 'noreply@umishop.com', ['product@umishop.com'])
        return

    return
