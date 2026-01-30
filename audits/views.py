from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from .models import AuditLog
from .serializers import AuditLogSerializer
from accounts.utils import is_admin


class AuditLogListAPIView(generics.ListAPIView):
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # 🔐 Only ADMIN / MANAGER can view audit logs
        if not is_admin(user):
            raise PermissionDenied("You are not allowed to view audit logs")

        return AuditLog.objects.all().order_by("-timestamp")
