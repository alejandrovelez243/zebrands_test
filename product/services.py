import requests
from django.conf import settings


def send_slack_message(message: str):
    url = settings.SLACK_URL
    response = requests.request("POST", url, json={"text": message})
    if response.ok:
        return True
    return False
