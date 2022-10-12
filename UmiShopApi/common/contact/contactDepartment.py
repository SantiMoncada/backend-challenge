from .sendEmail import contactByEmail
from .sendSlack import contactBySlack


def contactDepartment(data):

    if (data['topic'] == 'Sales'):
        message = "the customer " + data['email'] + \
            " had an issue with " + data['topic'] + "."
        contactBySlack('product', message)
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
