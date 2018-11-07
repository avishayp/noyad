import requests as r
from . import log

HOOK = 'https://hooks.slack.com/services/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'


def monitor(msg, *args):
    formatted = msg % args
    log.info(msg, *args)
    notify(formatted)


def notify(msg, channel='#ari', user='ari-bot'):
    return post(HOOK, json = {
            "channel": channel,
            "username": user,
            "text": msg
        }
    ).text
