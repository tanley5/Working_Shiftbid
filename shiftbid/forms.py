from dataclasses import field
from django import forms
from django.forms import ModelForm
from django import forms

from .models import Shiftbid, Shift

class ShiftbidCreateForm(forms.Form):
    shiftbid_name = forms.CharField(max_length=30)
    shift_file = forms.FileField()
    seniority_file = forms.FileField()

class ShiftbidResponseForm(forms.Form):
    Shiftbid = forms.ModelMultipleChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        self.pk = kwargs.pop('pk')
        super(ShiftbidResponseForm, self).__init__(*args, **kwargs)
        self.fields['Shiftbid'].queryset = Shift.objects.exclude(
            agent_email__contains='@').filter(shiftbid=Shiftbid.objects.get(pk=self.pk))
        self.fields["agent_email"] = forms.EmailField()
