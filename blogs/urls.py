from django.urls import path
from blogs import views



urlpatterns = [
    path('', views.get_blogs ),
    path('write_blogs/', views.write_blogs),
    path('edit_blogs/<int:pk>/', views.edit_blogs),
    path('delete_blogs/<int:pk>/', views.delete_blogs),
    path('comment_blogs/<int:pk>/', views.user_comments),
    path('delete_comment/<int:pk>/', views.delete_comment),
    path('edit_comment/<int:pk>/', views.edit_comment),
]
