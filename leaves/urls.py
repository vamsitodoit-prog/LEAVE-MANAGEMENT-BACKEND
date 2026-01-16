from django.urls import path
from .views import LeaveRequestListCreateView

urlpatterns = [
    path('', LeaveRequestListCreateView.as_view()),
]
