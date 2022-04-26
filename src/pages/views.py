from django.views.generic import TemplateView
from django.shortcuts import render


class ComingSoonView(TemplateView):
    """
    Coming soon page view
    """
    template_name = 'pages/coming-soon.html'


class HomePageView(TemplateView):
    """
    Home page view
    """
    template_name = 'pages/home_page.html'


class AboutPageView(TemplateView):
    """
    About page view
    """
    template_name = 'pages/about.html'
