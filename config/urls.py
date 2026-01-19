from notifications.views import notification_api
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from notifications.views import notification_api


def home(request):
    return HttpResponse("Leave Management System Backend is Running")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),

    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/v1/auth/', include('accounts.urls')),
    path('api/v1/leaves/', include('leaves.urls')),

    path('api/notifications/', notification_api),
]
