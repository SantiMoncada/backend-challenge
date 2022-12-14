[![backend-challenge](https://github.com/SantiMoncada/backend-challenge/actions/workflows/push.yml/badge.svg?branch=master)](https://github.com/SantiMoncada/backend-challenge/actions/workflows/push.yml)
## Try the Project online
https://santimoncada.github.io/backend-challenge/
![Diagram of the frontend](./img/LanbotFlow.png "Picture")
## Run Project Locally

Requirements

-ngrok

-python 3.10.6

-pip

```
pip install -r requirements.txt

python manage.py migrate --run-syncdb 

#Each in one terminal

    docker run -p 5672:5672 rabbitmq

    celery -A UmiShopApi worker -l INFO

    python manage.py runserver

    ngrok http :8000
```

## Run Project Witch Docker
```
docker-compose up
```

### Enviroment variables

```
    SECRET_KEY=
    #0 or 1
    DEBUG=

    #allowed ip's separated by space
    ALLOWED_HOSTS=

    #Mail
    EMAIL_HOST=
    EMAIL_HOST_USER=
    EMAIL_HOST_PASSWORD=
    EMAIL_PORT =

    SLACK_TOKEN =

    #set to 0 if running outside docker set to 1 if running inside
    DOCKER= 
```
# Description

From UmiShop, we have concluded that we want to improve web sales using Landbot.

For this reason, you have to create a bot in Landbot that asks the client for their name, email, and phone number and later, using a Webhook node, send it to our API and register the new user.

> Hint: Ngrok will provide you an URL to your localhost.

From the product department, they insist on the importance of knowing the origin of customers.

All registered users should receive a welcome email after 1 minute.

On the other hand, the product department wants a system to be notified when a customer requests assistance from a bot. The bot will ask the client for the topic (Sales, Pricing,...). Then, you have to create a bot that will communicate through Webhook to our API and our API will send the question to the different channels depending on the selected topic.

``` 
Topic    | Channel   
----------------------
Sales    | Slack
Pricing  | Email
```

> Note: Slack and Email are suggestions. Select the channels that you like the most.

The product department has in mind to expand the topics and communication channels.

## The solution should:
- Be written in Python using DRF + Django + Celery
- App dockerized
- Have a clear structure
- Be easy to grow with new functionality

## Bonus Points For:
- Tests
- Useful comments
- Documentation
- CI
- Commit messages
- Clear scalability