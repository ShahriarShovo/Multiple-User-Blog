from multiprocessing import set_forkserver_preload
from django.db import models

# Create your models here.

class Logo(models.Model):
    site_name=models.CharField(max_length=100, blank=True, null=True)
    site_logo=models.ImageField(upload_to='site_logo', blank=True, null=True)

    def __str__(self) -> str:
        return self.site_name

class Footer(models.Model):
    facebook=models.URLField(max_length=2000, blank=True,null=True)
    twitter=models.URLField(max_length=2000, blank=True,null=True)
    instagram=models.URLField(max_length=2000, blank=True,null=True)
    youtube=models.URLField(max_length=2000, blank=True,null=True)
    vk=models.URLField(max_length=2000, blank=True,null=True)

    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=100,blank=True, null=True)

    term_and_condition=models.TextField(blank=True, null=True)

    developer= models.CharField(max_length=100,blank=True, null=True)

    def __str__(self) -> str:
        return str(self.id)

