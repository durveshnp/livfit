from django.urls import path
from . import views

urlpatterns = [
    path("", views.lauchpage, name='livfithome'),
    path("profile/", views.home, name='livfitprofile'),
    path('exercise-form/', views.add_exercise, name='add-exercise'),
    path('food-form/', views.add_food, name='add-food'),
    path('exercise/', views.exercise_page, name='exercise'),
    path('food/', views.food_page, name='food'),
    path('team/', views.team, name='team'),
]
