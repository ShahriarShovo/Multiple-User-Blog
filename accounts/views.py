
from accounts.serializers import User_Registration_Serializer,User_Profile_Serializer, User_Serializer,Login_Serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from accounts.models import Profile, User
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from drf_yasg.utils import swagger_auto_schema

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# Create your views here.

# User Sign Up function or view

@swagger_auto_schema(method='POST', request_body=User_Registration_Serializer)
@api_view(['POST'])
def User_Registration(request):
    if request.method=='POST':
        user=User_Registration_Serializer(data=request.data)
        if user.is_valid():
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(data=user.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        return Response(data=user.errors, status=status.HTTP_400_BAD_REQUEST)


# User Login
@swagger_auto_schema(method='POST', request_body=Login_Serializers)
@api_view(['POST'])
def User_Login(request):
    if request.method=='POST':
        user=authenticate(request, username=request.data.get('username'), password=request.data.get('password'))
        if user is not None:
            token=get_tokens_for_user(user)
            #login(request,aut)
            return Response({"token":token}, status=status.HTTP_200_OK)
        else:
            print("Not Found")
            return Response(status=status.HTTP_302_FOUND)
    else:
         return Response(status=status.HTTP_400_BAD_REQUEST)


# # #get user profile

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    current_user=request.user.profile.id
    profile=get_object_or_404(User,profile__id=current_user)
    get_profile=User_Serializer(profile)
    return Response(get_profile.data)





#get user profile
@swagger_auto_schema(method='PUT', request_body=User_Serializer)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request,pk):
    try:
        get_profile=User.objects.get(pk=pk)
        get_user_data=User_Serializer(instance=get_profile, data=request.data)
        if get_user_data.is_valid():
            get_user_data.save()
            return Response(get_user_data.data)
        else:
            return Response(get_user_data.errors)

    except Exception as e:
        print(e)




    




