from django.urls import path
from .views import LeaveDiscussionListCreateAPIView

urlpatterns = [
    path(
        'leaves/<int:leave_id>/discussions/',
        LeaveDiscussionListCreateAPIView.as_view()
    ),
]
