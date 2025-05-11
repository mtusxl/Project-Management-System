import json

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from django.http import JsonResponse


from Tasks.serializers import TaskSerializers
from .models import Task
from Projects.models import Project



class TaskAPI(APIView):


    def post(self, request):
        data = request.data.copy()
        serializer = TaskSerializers(data=data)
        
        if serializer.is_valid():
            serializer.save()
            print("Задача создана")
            project = get_object_or_404(Project, id=data["project"])
            print(project)
            tasks_project = project.tasks.all()
            print(tasks_project)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        print("Ошибки валидации:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    
    
    

class TaskDetailAPI(APIView):

    def get_task(self, id):
        return get_object_or_404(Task, id=id)
    
    def get(self, request, id):
       
        task = self.get_task(id)
        print(task.id)
        serializer = TaskSerializers(task)
        return Response(serializer.data)

    def patch(self, request, id):  
        task = self.get_task(id)
        serializer = TaskSerializers(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        print("Validation errors:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        task = self.get_task(id)
        task.delete()
        return Response(status=status.HTTP_200_OK)