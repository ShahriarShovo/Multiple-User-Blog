from rest_framework import serializers
from categories.models import Categories, Sub_Categories


class Categories_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Categories
        fields='__all__'


class Sub_Categories_Serializers(serializers.ModelSerializer):
    sub_cat=Categories_Serializers(many=True, read_only=True)
    class Meta:
        model=Sub_Categories
        fields='__all__'
