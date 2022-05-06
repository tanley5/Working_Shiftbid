from dataclasses import field
from django import forms
from django.forms import ModelForm
from django import forms

from .models import Shiftbid

class ShiftbidCreateForm(forms.Form):
    shiftbid_name = forms.CharField(max_length=30)
    shift_file = forms.FileField()
    seniority_file = forms.FileField()
