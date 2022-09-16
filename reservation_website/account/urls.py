from django.urls import path

from .views import SignUpView, profile, ChangePasswordView


urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/<username>', profile, name='profile'),
    path('password-change/', ChangePasswordView.as_view(), name='password_change')
]