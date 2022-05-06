from django.urls import path
from .views import ShiftbidIndexView,ShiftbidCreateView

urlpatterns = [
    path('', ShiftbidIndexView.as_view(), name="shiftbid_index"),
    path('create',ShiftbidCreateView.as_view(), name="shiftbid_create"),
]