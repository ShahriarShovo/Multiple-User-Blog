
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class User(AbstractUser):
    username=models.CharField(max_length=100, unique=True, null=True, blank=True)
    phone=models.CharField(max_length=20, unique=True, null=True, blank=True)
    email=models.EmailField(unique=True, null=True, blank=True)
    REQUIRED_FIELDS=['email','phone']

    def __str__(self) -> str:
        return self.email

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', null=True, blank=True)
    profile_image=models.ImageField(upload_to='profile_image', null=True, blank=True)
    profession=models.CharField(max_length=400, blank=True,null=True)
    motivation=models.CharField(max_length=1000, blank=True,null=True)
    bio=models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.user.email


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()