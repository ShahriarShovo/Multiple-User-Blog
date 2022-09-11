from django.urls import path
from accounts import views


urlpatterns = [
    path('signup/', views.User_Registration),
    path('login/', views.User_Login),
    path('profile/', views.get_profile),
    path('profile_update/<int:pk>/', views.update_profile),
    #path('Update_profile/<int:pk>/', views.update_profile),
]
