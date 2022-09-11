from asyncio.windows_events import NULL
from rest_framework import serializers
from accounts.models import User, Profile
from django.contrib.auth.hashers import make_password


class User_Registration_Serializer(serializers.ModelSerializer):
    #create password 
        def create(self, validated_data):
            obj=self.Meta.model(**validated_data)
            password=validated_data['password']
            
            if password is not None:
                obj.password=make_password(password)
                obj.save()
                return obj


        class Meta:
            model=User
            fields=['username','email','phone','password']


class Login_Serializers(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','password']

class User_Profile_Serializer(serializers.ModelSerializer):
   
    class Meta:
        model=Profile
        fields=['bio','profile_image','profession','motivation']
        depth=1 

        def update(self,instance, validated_data):
            instance.profile_image=validated_data.get('profile_image', instance.profile_image)
            if instance.profile_image == None:
                instance.profile_image=instance.profile_image
                instance.save()
                return instance
            else:
                instance.save()
                return instance

       


class User_Serializer(serializers.ModelSerializer):
    profile=User_Profile_Serializer(required=False)
    class Meta:
        model=User
        fields=['id','first_name','last_name','username','email','phone','profile']

        def update(self,instance, validated_data):
            instance.profile= validated_data('profile', instance.profile)
            if instance.profile is not NULL:
                instance.save()
                return instance
            else:
                instance.save()
                return instance
                
            
        



