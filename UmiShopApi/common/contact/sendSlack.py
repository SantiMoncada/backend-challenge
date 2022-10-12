from cgitb import text
import slack
import os
from pathlib import Path

# TODO env
token = "xoxb-4214307256676-4214331105828-M6tmLRTz9MXI7JHEvfUSnXAP"
client = slack.WebClient(token)


def contactBySlack(channel, message):
    client.chat_postMessage(channel=channel, text=message)
