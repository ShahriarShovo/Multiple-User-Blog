from django.db import models


# Create your models here.


class Categories(models.Model):

    cat_name=models.CharField(max_length=100, null=True, blank=True)
    cat_title=models.CharField(max_length=200, null=True, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.cat_name

class Sub_Categories(models.Model):
    category= models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='sub_cat', null=True, blank=True)
    sub_cat_name=models.CharField(max_length=100, null=True, blank=True)
    sub_cat_title=models.CharField(max_length=200, null=True, blank=True)
    created_at= models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at= models.DateTimeField(auto_now=True, null=True, blank=True)

    def __str__(self) -> str:
        return self.sub_cat_name


