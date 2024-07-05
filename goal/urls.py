# goal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-goal', views.create_goal, name='create_goal'),
    # path('update-item/', views.update_item, name='update_item'),
    # path('delete-item/', views.delete_item, name='delete_item'),
    # path('delete-all-items/', views.delete_all_items, name='delete_all_items'),
]
