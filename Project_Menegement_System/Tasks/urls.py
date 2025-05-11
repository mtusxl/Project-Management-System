from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import TaskAPI, TaskDetailAPI


urlpatterns = [
    path("api/tasks/", TaskAPI.as_view(), name="tasks"),
    path("api/tasks/<int:id>/", TaskDetailAPI.as_view(), name="task_detail"),
    
]
    
