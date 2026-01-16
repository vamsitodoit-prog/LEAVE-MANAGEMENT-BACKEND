from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .models import LeaveDiscussion
from .serializers import LeaveDiscussionSerializer

class LeaveDiscussionListAPIView(generics.ListAPIView):
    queryset = LeaveDiscussion.objects.all()
    serializer_class = LeaveDiscussionSerializer
    permission_classes = [AllowAny]

# Create your views here.
