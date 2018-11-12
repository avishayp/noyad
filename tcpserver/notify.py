import requests as r
from . import log

HOOK = 'https://hooks.slack.com/services/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'

"""
curl -d '{ "text": "test", "channel": "#ari", "icon_emoji": ":ari:", "username": "bot" }' \
'https://hooks.slack.com/services/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'
"""


def monitor(msg, *args):
    log.info(msg, *args)
    notify(msg % args)


def notify(msg, channel='#ari', user='ari-bot', icon=':ari:', hook=HOOK):
    r.post(hook, json = {
            "text": msg,
            "channel": channel,
            "username": user,
            "icon_emoji": icon
        }
    )
