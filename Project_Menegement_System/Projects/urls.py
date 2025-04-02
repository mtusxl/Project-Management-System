# projects/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('project/<slug:slug>/', views.project_list, name='project'),
    #path('<int:id>/', views.project_detail, name='project_detail'),
]
