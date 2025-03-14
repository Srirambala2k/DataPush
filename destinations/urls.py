from django.urls import path
from . import views
from .views import ListCreateDestinationAPIView, UpdateRetriveDestroyDestinationAPIView




urlpatterns = [
    # Destination Endpoints
        path('destinations/', ListCreateDestinationAPIView.as_view(), name='list-create-destination'),
        path('destinations/<int:pk>/', UpdateRetriveDestroyDestinationAPIView.as_view(), name='destination-detail'),
]