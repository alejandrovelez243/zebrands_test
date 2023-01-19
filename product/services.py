import requests


def send_slack_message(message: str):
    url = "https://hooks.slack.com/services/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"
    response = requests.request("POST", url, json={"text": message})
    if response.ok:
        return True
    return False
