import requests
from django.conf import settings


def send_slack_notification(message):
    webhook_url = settings.SLACK_WEBHOOK_URL

    # Safety check
    if not webhook_url:
        print("⚠️ Slack webhook URL not configured")
        return

    payload = {
        "text": message
    }

    try:
        response = requests.post(webhook_url, json=payload, timeout=5)

        if response.status_code != 200:
            print(
                f"❌ Slack notification failed: "
                f"{response.status_code} {response.text}"
            )

    except Exception as e:
        print("❌ Slack notification error:", str(e))
