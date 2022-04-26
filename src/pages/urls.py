from django.urls import path

from .views import ComingSoonView, HomePageView, AboutPageView

urlpatterns = [
    path('comingsoon', ComingSoonView.as_view(), name='coming-soon_view'),
    path('', HomePageView.as_view(), name='home_view'),
    path('about', AboutPageView.as_view(), name='about_view'),
]
