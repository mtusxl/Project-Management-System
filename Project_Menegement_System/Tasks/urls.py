from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import all_tasks, task_in_progress, edit_task, delete_task, create_task


urlpatterns = [
    path("task/<int:project_id>/create_task/", create_task, name="create_task"),
    path("task/<int:task_id>/in_progress/", task_in_progress, name="task_in_progress"),
    path('task/<int:task_id>/edit/', edit_task, name='edit_task'),
    path("task/<int:task_id>/delete/", delete_task, name="delete_task"),
]
    
