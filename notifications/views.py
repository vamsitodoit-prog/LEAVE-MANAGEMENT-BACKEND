from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404


class NotificationListAPIView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # User can see ONLY their notifications
        return Notification.objects.filter(
            receiver=self.request.user
        ).order_by("-created_at")
class MarkNotificationReadAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        notification = get_object_or_404(
            Notification,
            pk=pk,
            receiver=request.user
        )

        notification.is_read = True
        notification.save()

        return Response(
            {"message": "Notification marked as read"},
            status=status.HTTP_200_OK
        )