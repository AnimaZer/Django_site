# pages/urls.py
from django.urls import path
from .views import HomePageView, LoadDataView, processing_run
from .forms import FaceFinderForm

urlpatterns = [
    path('', LoadDataView.as_view(), name='home'),
    path('processing_run/', processing_run, name='processing_run')
]
