import requests
from django.conf import settings


def send_slack_message(message: str):
    """
    It sends a message to a Slack channel

    :param message: The message you want to send to Slack
    :type message: str
    :return: True or False
    """
    url = settings.SLACK_URL
    response = requests.request("POST", url, json={"text": message})
    if response.ok:
        return True
    return False
