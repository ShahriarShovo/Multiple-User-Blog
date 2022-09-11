from django.urls import path
from categories import views

urlpatterns = [
    path('categories/', views.get_categories),
    path('create_categories/', views.create_categories),
    path('edit_categories/<int:pk>/', views.edit_categories),
    path('delete_categories/<int:pk>/', views.delete_categories),

    path('sub_categories/', views.get_sub_categories),
    path('sub_create_categories/', views.create_sub_categories),
    path('edit_sub_categories/<int:pk>/', views.edit_sub_categories),
    path('delete_sub_categories/<int:pk>/', views.delete_sub_categories),
]
