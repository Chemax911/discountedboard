from django.urls import path
from src.dashboard import views


urlpatterns = [
    path('profile/', views.ProfileView.as_view(), name='profile'),
]
