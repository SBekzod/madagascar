from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-goal', views.create_goal_view, name='create_goal'),
    path('update-goal', views.update_goal_view, name='update_goal'),
    path('delete-goal', views.delete_goal_view, name='delete-goal'),
    path('delete-all-goals', views.delete_all_goals_view, name='delete_all_goals'),
]
