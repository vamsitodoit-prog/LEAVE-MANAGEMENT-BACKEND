from rest_framework import serializers
from datetime import date
from .models import LeaveRequest, LeaveType


class LeaveTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveType
        fields = '__all__'


class LeaveRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeaveRequest
        fields = '__all__'
        read_only_fields = ['status', 'applied_at', 'updated_at']

    def validate(self, data):
        # 1️⃣ Start date cannot be after end date
        if data['start_date'] > data['end_date']:
            raise serializers.ValidationError(
                "Start date cannot be after end date"
            )

        # 2️⃣ Leave cannot start in the past
        if data['start_date'] < date.today():
            raise serializers.ValidationError(
                "Leave cannot start in the past"
            )

        # 3️⃣ Optional: overlapping leave check
        request = self.context.get('request')
        if request and request.user:
            overlap = LeaveRequest.objects.filter(
                user=request.user,
                start_date__lte=data['end_date'],
                end_date__gte=data['start_date']
            ).exists()

            if overlap:
                raise serializers.ValidationError(
                    "Overlapping leave request exists"
                )

        return data
