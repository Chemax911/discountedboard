from django.views.generic import TemplateView
from django.shortcuts import render


class ComingSoonView(TemplateView):

    template_name = 'pages/coming-soon.html'
