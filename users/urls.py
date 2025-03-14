from django.urls import path
from . import views
from .views import (CreateUserAPIView, ListUsersAPIView, UpdateRetriveDestroyUserAPIView,ListAccountAPIView,
    UpdateRetriveDestroyAccountAPIView, create_account)


urlpatterns = [
    # User Endpoints
        path('users/', ListUsersAPIView.as_view(), name='list-users'),
        path('users/create/', CreateUserAPIView.as_view(), name='create-user'),
        path('users/<int:pk>/', UpdateRetriveDestroyUserAPIView.as_view(), name='user-detail'),
        ## create New Account
        path('api/create-account/', create_account, name='create-account'),
        
        path('accounts/<int:pk>/', UpdateRetriveDestroyAccountAPIView.as_view(), name='account-detail'),

        path('accounts/', ListAccountAPIView.as_view(), name='list-account'),
        path('accounts/<int:pk>/', UpdateRetriveDestroyAccountAPIView.as_view(), name='account-detail'),
]