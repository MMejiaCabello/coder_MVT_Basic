from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio),
    path('familia/', views.family)
]