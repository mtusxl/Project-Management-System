from django.urls import path
from . import views

urlpatterns = [
    path('create_project/', views.Create_project, name='create_project'),
]
