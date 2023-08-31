from django.urls import path
from .views import LoginView, SignUpView, LogoutView, UserAPIView

urlpatterns = [
    path('user/profile/', UserAPIView.as_view(), name="profile"),
    path('auth/signup/', SignUpView.as_view(), name='token-signup'),
    path('auth/login/', LoginView.as_view(), name='token-login'),
    path('auth/logout/', LogoutView.as_view(), name='token-logout'),
]
