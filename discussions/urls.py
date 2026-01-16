from django.urls import path
from .views import LeaveDiscussionListAPIView

urlpatterns = [
    path('', LeaveDiscussionListAPIView.as_view()),
]
