from django.urls import path
from .views import ShiftbidIndexView

urlpatterns = [
    path('', ShiftbidIndexView.as_view(), name="shiftbid_index"),
]