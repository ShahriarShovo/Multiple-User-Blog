from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from header_and_footer.serialiazers import Logo_Serialiazers, Footer_Serialiazers
from header_and_footer.models import Logo, Footer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import permission_classes

# Create your views here.


#create logo

@swagger_auto_schema(method='POST', request_body=Logo_Serialiazers)
@api_view(['POST'])
@permission_classes([IsAdminUser])
def create_logo(request):
    try:
        if request.method=='POST':
            create_logo= Logo_Serialiazers(data=request.data)
            if create_logo.is_valid():
                create_logo.save()
                return Response(create_logo.data)
            else:
                return Response(create_logo.errors)
    except Exception as e:
        print(e)



@swagger_auto_schema(method='PUT', request_body=Logo_Serialiazers)
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_logo(request,pk):
    try:
        get_logo=Logo.objects.get(pk=pk)
        update_logo=Logo_Serialiazers(instance=get_logo,data=request.data)
        if update_logo.is_valid():
            update_logo.save()
            return Response(update_logo.data)
        else:
            return Response(update_logo.errors)

    except Exception as e:
        print(e)


@swagger_auto_schema(method='DELETE')

@api_view(['DELETE'])
@permission_classes([IsAdminUser])

def delete_logo(request,pk):
    delete_logo=Logo.objects.get(pk=pk)
    delete_logo.delete()
    return Response({'message':'Successfully Deleted'})

@api_view(['GET'])
def get_logo(request):
    get_logo=Logo.objects.all()
    get_logo_serialiazers=Logo_Serialiazers(get_logo, many=True)
    return Response(get_logo_serialiazers.data)


#--------------------------------------------------------------------------


@swagger_auto_schema(method='POST', request_body=Footer_Serialiazers)
@api_view(['POST'])
@permission_classes([IsAdminUser])

def create_footer(request):
    try:
        if request.method=='POST':
            create_footer= Footer_Serialiazers(data=request.data)
            if create_footer.is_valid():
                create_footer.save()
                return Response(create_footer.data)
            else:
                return Response(create_footer.errors)
    except Exception as e:
        print(e)


@swagger_auto_schema(method='PUT', request_body=Footer_Serialiazers)
@api_view(['PUT'])
@permission_classes([IsAdminUser])

def update_footer(request,pk):
    try:
        get_footer=Footer.objects.get(pk=pk)
        update_footer=Footer_Serialiazers(instance=get_footer,data=request.data)
        if update_footer.is_valid():
            update_footer.save()
            return Response(update_footer.data)
        else:
            return Response(update_footer.errors)

    except Exception as e:
        print(e)


@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
@permission_classes([IsAdminUser])

def delete_footer(request,pk):
    delete_footer=Footer.objects.get(pk=pk)
    delete_footer.delete()
    return Response({'message':'Successfully Deleted'})

@api_view(['GET'])
@permission_classes([IsAdminUser])

def get_footer(request):
    get_footer=Footer.objects.all()
    get_footer_serialiazers=Footer_Serialiazers(get_footer, many=True)
    return Response(get_footer_serialiazers.data)





