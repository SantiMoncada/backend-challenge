from cgitb import text
import slack

# TODO env
token = "xoxb-4214307256676-4214331105828-ehkdbSODyvPBItQWXdpMNjUd"
client = slack.WebClient(token)


def contactBySlack(channel, message):
    client.chat_postMessage(channel=channel, text=message)
