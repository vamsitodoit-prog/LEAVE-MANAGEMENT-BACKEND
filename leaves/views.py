from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
#from rest_framework.permissions import AllowAny

from .models import LeaveRequest
from .serializers import LeaveRequestSerializer
from notifications.services import send_slack_notification


class LeaveRequestListCreateView(generics.ListCreateAPIView):
    queryset = LeaveRequest.objects.all()
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]
    #permission_classes = [AllowAny] 
    def perform_create(self, serializer):
        leave = serializer.save(user=self.request.user)
        send_slack_notification(
            f"New leave request created by {leave.user}"
        )

