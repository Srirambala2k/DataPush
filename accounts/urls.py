from django.urls import path
from . import views
from .views import (
    register,
    login_view,
    logout,
    ListCreateAccountMemberAPIView,
    UpdateRetriveDestroyAccountMemberAPIView
)

urlpatterns = [
    # login/logout/register
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),


    
    path('accountmembers/', ListCreateAccountMemberAPIView.as_view(), name='list-account'),
    path('accountmembers/<int:pk>/', UpdateRetriveDestroyAccountMemberAPIView.as_view(), name='list-account'),
    
]

