from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import blogs
from blogs.models import Blog, Comments
from blogs.serializers import Blog_Serializers, Comments_Serializers
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema


@api_view(['GET'])
def get_blogs(request):
   
    get_blogs=Blog.objects.all()
    serializers=Blog_Serializers(get_blogs, many=True)
    return Response(serializers.data, status=status.HTTP_200_OK)

       

@swagger_auto_schema(method='POST', request_body=Blog_Serializers)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def write_blogs(request):
    try:
        if request.method=='POST':
            current_user=request.user
            user=Blog(user=current_user)
            blog_post=Blog_Serializers(user,data=request.data)
            if blog_post.is_valid():
                blog_post.save()
                return Response(blog_post.data)
            else:
                return Response(blog_post.errors)
        else:
            return Response(blog_post.errors)
    except Exception as e:
        print(e)

@swagger_auto_schema(method='PUT', request_body=Blog_Serializers)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_blogs(request,pk):
    try:
        get_post=Blog.objects.get(pk=pk)
        edit_blog=Blog_Serializers(instance=get_post, data=request.data)
        if edit_blog.is_valid():
            edit_blog.save()
            return Response(edit_blog.data, status=status.HTTP_200_OK)
        else:
            return Response(edit_blog.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)


@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_blogs(request,pk):
    try:
        delt_blog=Blog.objects.get(pk=pk)
        delt_blog.delete()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        print(e)

@swagger_auto_schema(method='POST', request_body=Comments_Serializers)
@api_view(['POST'])
@permission_classes([IsAuthenticated])

def user_comments(request,pk):

    if request.method=='POST':
        get_blog=Blog.objects.get(pk=pk)
        user=request.user
        comments=Comments(user=user,blog=get_blog)
        
        user_comment=Comments_Serializers(comments,data=request.data)
        if user_comment.is_valid():

            user_comment.save()
            return Response(user_comment.data)
           
        else:
             return Response(user_comment.errors)


@swagger_auto_schema(method='PUT', request_body=Comments_Serializers)
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_comment(request,pk):
    try:
        get_comment=Comments.objects.get(pk=pk)
        edit_comment=Comments_Serializers(instance=get_comment, data=request.data)
        if edit_comment.is_valid():
            edit_comment.save()
            return Response(edit_comment.data, status=status.HTTP_200_OK)
        else:
            return Response(edit_comment.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        print(e)




@swagger_auto_schema(method='DELETE')
@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_comment(request,pk):
    try:
        delt_comment=Comments.objects.get(pk=pk)
        delt_comment.delete()
        return Response(status=status.HTTP_200_OK)
    except Exception as e:
        print(e)



