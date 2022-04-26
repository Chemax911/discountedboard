from django.contrib.auth import views
from django.urls import path
from django.views.generic import TemplateView

from src.users.views import (
    LoginView,
    EmailVerifyView,
    SignupPageView,
    PasswordResetView,
    PasswordResetConfirmView
)


urlpatterns = [
    path('login', LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('invalid_verify/', TemplateView.as_view(
        template_name='registration/invalid_verify.html'),
        name='invalid_verify'),
    path('verify_email/<uidb64>/<token>/', EmailVerifyView.as_view(), name='verify_email'),
    path('confirm_email/', TemplateView.as_view(
        template_name='registration/confirm_email.html'),
        name='confirm_email'),
    path('signup', SignupPageView.as_view(), name='signup'),
    path('password_change/', views.PasswordChangeView.as_view(), name='password_change'),
    path('password_change/done', views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
