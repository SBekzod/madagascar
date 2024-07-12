from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('create-plan', views.create_plan_view, name='create_plan'),
    path('update-plan', views.update_plan_view, name='update_plan'),
    path('delete-plan', views.delete_plan_view, name='delete-plan'),
    path('delete-all-plans', views.delete_all_plans_view, name='delete_all_plans'),
]
