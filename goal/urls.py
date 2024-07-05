# goal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-goal', views.create_goal, name='create_goal'),
    path('update-goal', views.update_goal, name='update_goal'),
]
