from rest_framework import serializers
from header_and_footer.models import Logo, Footer

class Logo_Serialiazers(serializers.ModelSerializer):
    class Meta:
        model=Logo
        fields=['site_name','site_logo']

        def update(self,instance, validat_data):
            instance.site_logo=validat_data('site_logo', instance.site_logo)
            if instance.site_logo==None:
                instance.site_logo=instance.site_logo
                instance.site_logo.save()
                return instance
            else:
                instance.site_logo.save()
                return instance


class Footer_Serialiazers(serializers.ModelSerializer):
    class Meta:
        model=Footer
        fields='__all__'