from django.urls import path
from . import views


urlpatterns = [
    path('tasks', views.all_tasks, name='all_tasks'),
]