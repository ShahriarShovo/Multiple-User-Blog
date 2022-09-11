from django.db import models
from accounts.models import User
from categories.models import Categories, Sub_Categories

# Create your models here.

class Blog(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True, blank=True)
    category=models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='category', null=True, blank=True)
    sub_category=models.ForeignKey(Sub_Categories, on_delete=models.CASCADE, related_name='sub_category', null=True, blank=True)
    blog_name=models.CharField(max_length=100, null=True, blank=True)
    blog_title=models.CharField(max_length=200, null=True, blank=True)
    blog_image=models.ImageField(upload_to='blog_image',null=True, blank=True)
    blog_body=models.TextField(null=True, blank=True)
    blog_created_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    blog_updated_at=models.DateTimeField(auto_now=True, null=True, blank=True)
    def __str__(self) -> str:
        return self.blog_name


class Comments(models.Model):
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comment')
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comment')
    comment=models.TextField()
    commented_at=models.DateTimeField(auto_now_add=True, null=True, blank=True)
    commented_updated=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.blog.blog_name

    
