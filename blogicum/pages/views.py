from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class AboutPage(TemplateView):
    template_name = 'pages/about.html'


class RulesPage(TemplateView):
    template_name = 'pages/rules.html'