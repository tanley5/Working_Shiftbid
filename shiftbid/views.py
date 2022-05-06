from django.views.generic.base import TemplateView
from django.shortcuts import render

class ShiftbidIndexView(TemplateView):
    template_name = 'shiftbid/index.html'