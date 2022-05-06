from django.contrib import admin
from .models import Shift, Seniority, Shiftbid

admin.site.register(Shiftbid)
admin.site.register(Seniority)
admin.site.register(Shift)