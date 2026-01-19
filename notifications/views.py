from django.http import JsonResponse
from .models import Notification

def notification_api(request):
    notifications = Notification.objects.all().order_by("-created_at")

    data = [
        {
            "id": n.id,
            "message": n.message,
            "is_read": n.is_read,
            "created_at": n.created_at,
        }
        for n in notifications
    ]

    return JsonResponse(data, safe=False)
