from django.urls import path
from .views import LeaveRequestListCreateView
from .views import ApproveLeaveAPI, RejectLeaveAPI, UpdateLeaveAPI

urlpatterns = [
    path('<int:pk>/approve/', ApproveLeaveAPI.as_view()),
    path('<int:pk>/reject/', RejectLeaveAPI.as_view()),
    path('<int:pk>/update/', UpdateLeaveAPI.as_view()),
    path('', LeaveRequestListCreateView.as_view()),


]
