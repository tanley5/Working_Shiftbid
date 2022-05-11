from django.urls import path
from .views import ShiftbidDeleteView, ShiftbidIndexView,ShiftbidCreateView, ShiftbidDisplayView

urlpatterns = [
    path('', ShiftbidIndexView.as_view(), name="shiftbid_index"),
    path('create',ShiftbidCreateView.as_view(), name="shiftbid_create"),
    path('delete/<int:pk>',ShiftbidDeleteView.as_view(), name='shiftbid_delete'),
    path('display/<int:pk>',ShiftbidDisplayView.as_view(), name='shiftbid_display'),
]