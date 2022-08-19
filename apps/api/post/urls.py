from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

posts_urlpatterns = [
    path('posts/', views.PostListCreationView.as_view()),
]