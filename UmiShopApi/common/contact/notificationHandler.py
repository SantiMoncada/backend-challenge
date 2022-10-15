from .sendEmail import contactByEmail
from .sendSlack import contactBySlack


def notificationHandler(data):
    message = f'Hello,\n\
New issue with ID:{data["id"]} has been created.\n\
Topic: {data["topic"]}\n\
User: {data["email"]}\n\
User Location: {data["address"]}\n\
\n\
Please take action to resolve the customer issue.\n\
\n\
\n:D'

    if (data['topic'].lower() == 'sales'):
        contactBySlack('product', message)
        return
    elif (data['topic'].lower() == 'pricing'):
        contactByEmail('Customer had an issue',
                       message, 'noreply@umishop.com', ['product@umishop.com'])
        return
    else:
        contactByEmail('Customer had an issue',
                       message, 'noreply@umishop.com', ['product@umishop.com'])
        return

    return
