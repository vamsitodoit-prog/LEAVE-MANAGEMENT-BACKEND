from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import AuditLog
from .serializers import AuditLogSerializer

class AuditLogListAPIView(generics.ListAPIView):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [AllowAny]

# Create your views here.
