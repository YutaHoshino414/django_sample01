from django.urls import path

from . import views

urlpatterns = [
    path('', views.Index, name='index'),
    path('detail/<int:post_id>/', views.Detail, name="detail"),
]