from django.views.generic.base import TemplateView
from django.shortcuts import render

class PagesIndexView(TemplateView):
    template_name = 'pages/index.html'