from rest_framework import serializers
from .models import LeaveDiscussion

class LeaveDiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveDiscussion
        fields = '__all__'
