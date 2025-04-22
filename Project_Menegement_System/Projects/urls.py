# projects/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('project/<slug:slug>/update_project/', views.update_project, name='update_project'),
    path('project/<slug:slug>/', views.project_list, name='project'),
    path('create_project/', views.Create_project, name='create_project'),
    path('project/<slug:slug>/delete/', views.delete_project, name='delete_project'),
    
   

    #path('<int:id>/', views.project_detail, name='project_detail'),
]
