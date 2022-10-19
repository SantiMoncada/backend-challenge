import slack
import os

# TODO env
token = os.environ.get('SLACK_TOKEN', '')
client = slack.WebClient(token)


def contactBySlack(channel, message):
    client.chat_postMessage(channel=channel, text=message)
