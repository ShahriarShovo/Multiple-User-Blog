from asyncore import read
from rest_framework import serializers
from blogs.models import Blog, Comments



class Comments_Serializers(serializers.ModelSerializer):
  
    class Meta:
        model=Comments
        fields='__all__'
       


class Blog_Serializers(serializers.ModelSerializer):
    comment= Comments_Serializers(many=True, read_only=True)
    class Meta:
        model=Blog
        fields='__all__'
       
        def update(self, instance, validate_data):
            instance.blog_image=validate_data('blog_image',instance.blog_image)
            if instance.blog_image == None:
                instance.blog_image= instance.blog_image
                instance.save()
                return instance
            else:
                instance.save()
                return instance