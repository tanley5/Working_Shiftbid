from django.urls import path
from .views import PagesIndexView

urlpatterns = [
    path('', PagesIndexView.as_view(), name='pages_index'),
]