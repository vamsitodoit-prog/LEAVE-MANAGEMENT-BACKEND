from django.contrib import admin
from .models import LeaveType, LeaveRequest

admin.site.register(LeaveType)

# Register your models here.
@admin.register(LeaveRequest)
class LeaveRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'leave_type', 'status', 'start_date')
