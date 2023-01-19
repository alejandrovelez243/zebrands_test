import requests


def send_slack_message(message: str):
    url = "https://hooks.slack.com/services/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"
    response = requests.request("POST", url, json={"text": message})
    if response.ok:
        return True
    return False
