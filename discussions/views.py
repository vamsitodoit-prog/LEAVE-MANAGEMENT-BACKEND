from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import LeaveDiscussion
from .serializers import LeaveDiscussionSerializer
from django.shortcuts import get_object_or_404
from leaves.models import LeaveRequest
from notifications.models import Notification

class LeaveDiscussionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LeaveDiscussionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        leave_id = self.kwargs['leave_id']
        return LeaveDiscussion.objects.filter(
            leave_request_id=leave_id
        )

    def perform_create(self, serializer):
        leave = get_object_or_404(LeaveRequest, id=self.kwargs['leave_id'])

        discussion = serializer.save(
            sender=self.request.user,
            leave_request=leave
        )

    # 🔔 Decide receiver
        if self.request.user == leave.user:
        # Employee sent message → notify admin
            receiver = leave.user.manager if hasattr(leave.user, "manager") else None
        else:
        # Admin sent message → notify employee
            receiver = leave.user

        if receiver:
            Notification.objects.create(
                receiver=receiver,
                message=f"New discussion message on Leave ID {leave.id}"
            )

    
