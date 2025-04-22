from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Index.urls') ,name='landing'),
    path('', include('Dashbords.urls'), name='Dashbords'),
    path('', include('Tasks.urls'), name='tasks'),
    path('', include('Users.urls'), name='users'),
    path('', include('Projects.urls'), name='projects'),
   
]