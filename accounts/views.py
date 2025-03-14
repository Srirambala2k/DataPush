from django.shortcuts import render
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from .models import  AccountMember
from .serializers import  AccountMemberSerializer
from rest_framework import status
from rest_framework.response import Response
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator
from django.contrib.auth import logout,login
from rest_framework.permissions import IsAuthenticated,IsAdminUser
#from datapush.validators import validate_email, validate_website


# Create your views here.



## validating the email
def is_valid_email(email):
    try:
        validator = EmailValidator()
        validator(email)
    except ValidationError:
        return False
    return True

## validating the domain
def valid_email_domain(email, allowed_domains=None):
    if allowed_domains:
        domain = email.split('@')[1]
        if domain not in allowed_domains:
            return False
    return True


## @csrf_exempt ---> dont use for production only for testing purpose
## Register or create a new user
@csrf_exempt
def register(request):
    if request.method == 'POST':
        try:
            # Parse JSON body
            data = json.loads(request.body.decode('utf-8'))  # Parse JSON request data

            username = data.get('email')  
            password = data.get('password') 
            email = data.get('email')  

            if not username or not password or not email:
                return JsonResponse({"error": "All fields are required."}, status=400)

            allowed_domains = ['gmail.com']
            if not valid_email_domain(email, allowed_domains):
                return JsonResponse({"error": f"Email domain must be one of {allowed_domains}."}, status=400)

            if User.objects.filter(email=email).exists():
                return JsonResponse({"error": "Email already exists."}, status=400)

            # Create a user
            user = User.objects.create_user(username=email, email=email, password=password)

            # Authenticate and log in the user
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return JsonResponse({"message": "Registration successful."}, status=201)
            else:
                return JsonResponse({"error": "Authentication failed."}, status=400)
        
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format."}, status=400)

    return JsonResponse({"error": "Only POST method is allowed."}, status=405)

       
## login View
def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('Password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request,user)
            return JsonResponse({'message': 'successfully loged in'})
        else:
            return JsonResponse({"error":"invalid username or password"}, status=400)
    return Json({"error":"only post method is allowed"}, status=400)


##Log out view
def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
        return JsonResponse({"message": "Logged out successfully."})
    else:
        return JsonResponse({"error": "User not logged in."}, status=400)




class ListCreateAccountMemberAPIView(generics.ListCreateAPIView):
    queryset = AccountMember.objects.all()
    serializer_class = AccountMemberSerializer
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="List all AccountMember",
        description="Get all accounts",
        responses={200: AccountMemberSerializer(many=True)},
    )
    def get(self,request,*args,**kwargs):
        return super().get(request,*args,**kwargs)

    @extend_schema(
        summary="Create new AccountMember",
        description="Get all accounts",
        responses={200: AccountMemberSerializer(many=True)},
    )
    def post(self,request,*args,**kwargs):
        return super().post(request,*args,**kwargs)

class UpdateRetriveDestroyAccountMemberAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccountMember.objects.all()
    serializer_class = AccountMemberSerializer  
    permission_classes = [permissions.IsAdminUser]

    @extend_schema(
        summary="Retrieve, Update or Delete AccountMember",
        description="Get, update or delete a specific accountmember by ID.",
        request=AccountMemberSerializer,
        responses={200: AccountMemberSerializer},
    )
    def get(self,request,*args,**kwargs):
        return super().get(request,*args,**kwargs)
    
    def put(self,request,*args,**kwargs):
        return super().put(request,*args,**kwargs)
    
    def patch(self,request,*args,**kwargs):
        return super().patch(request,*args,**kwargs)
    
    def delete(self,request,*args,**kwargs):
        return super().delete(request,*args,**kwargs)


