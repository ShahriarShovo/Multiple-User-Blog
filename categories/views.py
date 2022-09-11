from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from categories.serializers import Categories_Serializers, Sub_Categories_Serializers
from categories.models import Categories, Sub_Categories
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from drf_yasg.utils import swagger_auto_schema



@api_view(['GET'])
def get_categories(request):
    try:
        get_categories=Categories.objects.all()
        get_categories_ser=Categories_Serializers(get_categories, many=True)
        return Response(get_categories_ser.data)
    except Exception as e:
        print(e)


@swagger_auto_schema(method='POST', request_body=Categories_Serializers)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_categories(request):
    try:
        if request.method=='POST':
            categories=Categories_Serializers(data=request.data)
            if categories.is_valid():
                categories.save()
                return Response(categories.data)
            else:
                return Response(categories.errors)
        else:
            return None
    except Exception as e:
        print(e)


@swagger_auto_schema(method='PUT', request_body=Categories_Serializers)
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_categories(request,pk):
    try:
        edit_cat=Categories.objects.get(pk=pk)
        edit_cat_sr= Categories_Serializers(edit_cat,data=request.data)
        if edit_cat_sr.is_valid():
            edit_cat_sr.save()
            return Response(edit_cat_sr.data)
        else:
            return Response(edit_cat_sr.errors)
    except Exception as e:
        print(e)

@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_categories(request,pk):
    delt_cat=Categories.objects.get(pk=pk)
    delt_cat.delete()
    return Response(status=status.HTTP_200_OK)




# Sub Categories--------------------------------------------------------------------

@api_view(['GET'])
def get_sub_categories(request):
    try:
        get_sub_categories=Sub_Categories.objects.all()
        get_sub_categories_ser=Sub_Categories_Serializers(get_sub_categories, many=True)
        return Response(get_sub_categories_ser.data)
    except Exception as e:
        print(e)

@swagger_auto_schema(method='POST', request_body=Sub_Categories_Serializers)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_sub_categories(request):
    try:
        if request.method=='POST':
            sub_categories=Sub_Categories_Serializers(data=request.data)
            if sub_categories.is_valid():
                sub_categories.save()
                return Response(sub_categories.data)
            else:
                return Response(sub_categories.errors)
        else:
            return None
    except Exception as e:
        print(e)


@swagger_auto_schema(method='PUT', request_body=Sub_Categories_Serializers)
@api_view(['PUT'])
@permission_classes([IsAdminUser])
def edit_sub_categories(request,pk):
    try:
        edit_sub_cat=Sub_Categories.objects.get(pk=pk)
        edit_sub_cat_sr= Sub_Categories_Serializers(edit_sub_cat,data=request.data)
        if edit_sub_cat_sr.is_valid():
            edit_sub_cat_sr.save()
            return Response(edit_sub_cat_sr.data)
        else:
            return Response(edit_sub_cat_sr.errors)
    except Exception as e:
        print(e)

@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_sub_categories(request,pk):
    delt_sub_cat=Sub_Categories.objects.get(pk=pk)
    delt_sub_cat.delete()
    return Response(status=status.HTTP_200_OK)









