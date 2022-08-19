from django.urls import path
from . import views


rating_urlpatterns = [

    path('ratings/', views.RatingListCreateView.as_view()),

]