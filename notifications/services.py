from .models import Notification

def send_slack_notification(message):
    # temporary placeholder
    print("Slack Notification:", message)


def create_notification(user, message):
    Notification.objects.create(
        receiver=user,
        message=message
    )
