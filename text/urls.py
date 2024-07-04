from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_profile, name='user_profile'),
    path('user_profile/<int:id>/', views.user_profile_edit, name='user_profile_edit'),
    path('delete_user/<int:id>/', views.delete_user, name='delete_user'),
]
