from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

# default_router = DefaultRouter()
# default_router.register(r"phone", views.VerificationViewSet, basename="phone")
users_urlpatterns = [
    # twilio
    # path('phone/register/', views.VerificationViewSet.as_view({"post":"register"})),
    # path('phone/verify/', views.VerificationViewSet.as_view({"post":"verify"})),
    path('username-verification/', views.UsernameVerificationViewSet.as_view()),
    path('user-creation/', views.UserCreationView.as_view()),
    path('user/profile/<int:pk>/', views.UserProfileUpdateView.as_view()),
    path('users/', views.UserListView.as_view()),
    path('users/me/', views.UserRetrieveView.as_view()),
]