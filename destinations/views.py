from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from .models import Destination
from .serializers import DestinationSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
#from datapush.validators import validate_email, validate_website
from django.contrib.auth import logout,login
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# Create your views here.

class ListCreateDestinationAPIView(generics.ListCreateAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="List all Destinations",
        description="Get all Destinations",
        responses={200: DestinationSerializer(many=True)},
    )
    def get(self,request,*args,**kwargs):
        # Call the parent class's get method to list all destinations
        return super().get(request,*args,**kwargs)

    @extend_schema(
        summary="Create new Destinations",
        description="New Destination will be created",
        responses={200: DestinationSerializer(many=True)},
    )    
    def post(self,request,*args,**kwargs):
        # Call the parent class's post method to create a new destination
        return super().post(request,*args,**kwargs)

class UpdateRetriveDestroyDestinationAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="Retrieve, Update or Delete Destination",
        description="Get, update or delete a specific Destination by ID.",
        request=DestinationSerializer,
        responses={200: DestinationSerializer},
    )
    def get(self,request,*args,**kwargs):
        # Call the parent class's get method to retrieve a destination by ID
        return super().get(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        # Call the parent class's put method to update a destination by ID
        return super().put(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        # Call the parent class's patch method to partially update a destination by ID
        return super().patch(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        # Call the parent class's delete method to delete a destination by ID
        return super().delete(request,*args,**kwargs)




