from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Shiftbid

class ShiftbidIndexView(ListView):
    template_name = 'shiftbid/index.html'
    model = Shiftbid