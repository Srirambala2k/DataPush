from django.urls import path
from .views import DataHandlerView

urlpatterns = [
    path("receive-data/", DataHandlerView.as_view(), name="data_handler"),
]