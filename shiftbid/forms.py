from django.forms import ModelForm

from .models import Shiftbid

class ShiftbidCreateForm(ModelForm):
    class Meta:
        model = Shiftbid
        fields = ["shiftbid_name","shift_status"]
