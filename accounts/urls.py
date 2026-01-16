from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MeAPIView

app_name = 'accounts'


urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('me/', MeAPIView.as_view(), name='me'),
]
       
    # Add your account-related URL patterns here
    # Example:
    # path('register/', views.RegisterView.as_view(), name='register'),
    # path('profile/', views.ProfileView.as_view(), name='profile'),

