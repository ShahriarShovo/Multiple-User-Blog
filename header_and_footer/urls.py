from django.urls import path
from header_and_footer import views

urlpatterns = [

    path('create_logo/', views.create_logo),
    path('update_logo/<int:pk>/', views.update_logo),
    path('delete_logo/<int:pk>/', views.delete_logo),
    path('get_logo/', views.get_logo),


    path('create_footer/', views.create_footer),
    path('update_footer/<int:pk>/', views.update_footer),

    path('delete_footer/<int:pk>/', views.delete_footer),
    path('get_footer/', views.get_footer),


    
]
