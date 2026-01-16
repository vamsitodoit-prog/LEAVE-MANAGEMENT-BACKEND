from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListAPIView(generics.ListAPIView):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [AllowAny]

# Create your views here.
