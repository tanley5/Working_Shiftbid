from django.urls import path
from .views import ShiftbidDeleteView, ShiftbidIndexView,ShiftbidCreateView, ShiftbidDisplayView, ShiftbidChangeStateView,ShiftbidResponseFormView

urlpatterns = [
    path('', ShiftbidIndexView.as_view(), name="shiftbid_index"),
    path('create',ShiftbidCreateView.as_view(), name="shiftbid_create"),
    path('delete/<int:pk>',ShiftbidDeleteView.as_view(), name='shiftbid_delete'),
    path('display/<int:pk>',ShiftbidDisplayView.as_view(), name='shiftbid_display'),
    path('change/<int:pk>', ShiftbidChangeStateView.as_view(), name='shiftbid_change'),
    path('response/<int:pk>', ShiftbidResponseFormView.as_view(), name='shiftbid_reponse_collection'),
]