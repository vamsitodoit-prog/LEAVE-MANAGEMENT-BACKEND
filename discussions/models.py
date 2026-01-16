from django.db import models
from django.conf import settings
from leaves.models import LeaveRequest

User = settings.AUTH_USER_MODEL


class LeaveDiscussion(models.Model):
    leave_request = models.ForeignKey(
        LeaveRequest,
        on_delete=models.CASCADE,
        related_name='discussions'
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Leave {self.leave_request.id} Message"

# Create your models here.
