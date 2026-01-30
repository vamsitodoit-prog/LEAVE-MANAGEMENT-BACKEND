from rest_framework import generics
from .serializers import LeaveRequestSerializer
from notifications.services import send_slack_notification
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .models import LeaveRequest
from audits.models import AuditLog
from accounts.utils import is_admin
from notifications.models import Notification



class LeaveRequestListCreateView(generics.ListCreateAPIView):
    serializer_class = LeaveRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # ADMIN / MANAGER → see all leaves
        if is_admin(user):
            return LeaveRequest.objects.all()

        # EMPLOYEE → see only their own leaves
        return LeaveRequest.objects.filter(user=user)

    def perform_create(self, serializer):
        leave = serializer.save(user=self.request.user)
        send_slack_notification(
            f"New leave request created by {leave.user}"
        )


class ApproveLeaveAPI(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        if not is_admin(request.user):
            raise PermissionDenied("Only admin can approve leave")

        leave = get_object_or_404(LeaveRequest, pk=pk)

        if leave.status not in ['PENDING', 'IN_DISCUSSION']:
            return Response(
                {"error": "Invalid state transition"},
                status=status.HTTP_400_BAD_REQUEST
            )

        leave.status = 'APPROVED'
        leave.save()

        # 🔔 CREATE NOTIFICATION FOR EMPLOYEE
        Notification.objects.create(
            receiver=leave.user,
            message=f"Your leave request (ID: {leave.id}) has been approved."
        )

        AuditLog.objects.create(
            user=request.user,
            action=f"Approved leave request {leave.id}"
        )

        return Response(
            {"message": "Leave approved successfully"},
            status=status.HTTP_200_OK
        )


class RejectLeaveAPI(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        if not is_admin(request.user):
            raise PermissionDenied("Only admin can reject leave")

        leave = get_object_or_404(LeaveRequest, pk=pk)

        if leave.status not in ['PENDING', 'IN_DISCUSSION']:
            return Response(
                {"error": "Invalid state transition"},
                status=status.HTTP_400_BAD_REQUEST
            )

        leave.status = 'REJECTED'
        leave.save()

        # 🔔 CREATE NOTIFICATION FOR EMPLOYEE
        Notification.objects.create(
            receiver=leave.user,
            message=f"Your leave request (ID: {leave.id}) has been rejected."
        )

        AuditLog.objects.create(
            user=request.user,
            action=f"Rejected leave request {leave.id}"
        )

        return Response(
            {"message": "Leave rejected successfully"},
            status=status.HTTP_200_OK
        )


class UpdateLeaveAPI(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        if not is_admin(request.user):
            raise PermissionDenied("Only admin can update leave")

        leave = get_object_or_404(LeaveRequest, pk=pk)

        if leave.status != 'IN_DISCUSSION':
            return Response(
                {"error": "Leave must be in discussion to update"},
                status=status.HTTP_400_BAD_REQUEST
            )

        leave.start_date = request.data.get('start_date', leave.start_date)
        leave.end_date = request.data.get('end_date', leave.end_date)
        leave.save()

        AuditLog.objects.create(
            user=request.user,
            action=f"Updated leave request {leave.id}"
        )

        return Response(
            {"message": "Leave updated successfully"},
            status=status.HTTP_200_OK
        )
