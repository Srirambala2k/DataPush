from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from .models import User,Role,Account 
from .serializers import UserSerializer,RoleSerializer,AccountSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from datapush.validators import validate_email, validate_website
from django.contrib.auth import logout,login
from rest_framework.permissions import IsAuthenticated,IsAdminUser


# Create your views here.

class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class ListUsersAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]

class UpdateRetriveDestroyUserAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


##Create a account
def create_account(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            # Validate the email for the User model
            validate_email(data['email'])
            
            # Validate the website for the Account model
            validate_website(data['website'])
            
           
            user = User.objects.create_user(
                username=data['email'],
                email=data['email'],
                password=data['password']
            )
            
            # Create Account instance
            account = Account.objects.create(
                user=user,  
                website=data['website'],
                
            )
            
            return JsonResponse({"message": "Account created successfully."}, status=201)
        except KeyError as e:
            return JsonResponse({"error": f"Missing field: {str(e)}"}, status=400)
        except ValidationError as e:
            return JsonResponse({"error": str(e)}, status=400)



class ListAccountAPIView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAdminUser]


class UpdateRetriveDestroyAccountAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="Retrieve, Update or Delete Account",
        description="Get, update or delete a specific account by ID.",
        request=AccountSerializer,
        responses={200: AccountSerializer},
    )
    def get(self,request,*args,**kwargs):
        return super().get(request,*args,**kwargs)

    def put(self,request,*args,**kwargs):
        return super().put(request,*args,**kwargs)

    def patch(self,request,*args,**kwargs):
        return super().patch(request,*args,**kwargs)

    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)

