from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import LeaveDiscussion
from .serializers import LeaveDiscussionSerializer
from django.shortcuts import get_object_or_404
from leaves.models import LeaveRequest
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
        serializer.save(
            sender=self.request.user,
            leave_request=leave
    )
    
