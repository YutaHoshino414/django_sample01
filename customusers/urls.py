from django.urls import path
from customusers import views

urlpatterns = [
    path('profile/',views.ProfileView.as_view(), name='profile')
]