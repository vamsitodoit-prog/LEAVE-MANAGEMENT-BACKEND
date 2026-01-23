from rest_framework import serializers
from .models import LeaveDiscussion

class LeaveDiscussionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveDiscussion
        fields = [
            'id',
            'message',
            'sender',
            'leave_request',
            'created_at',
        ]
        read_only_fields = [
            'sender',
            'leave_request',
            'created_at',
        ]
