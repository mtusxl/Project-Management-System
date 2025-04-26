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
    
    def get_task(self, id):
        return get_object_or_404(Task, id=id)

   
    def get(self, request):
        print(request)
        all_tasks = Task.objects.all()
        serializer = TaskSerializers(all_tasks, many=True)
        return Response(serializer.data)
    

    def post(self, request):
        data = request.data.copy()
        serializer = TaskSerializers(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        print("Ошибки валидации:", serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
 
    
    
    

class TaskDetailAPI(APIView):

    def get_task(self, id):
        return get_object_or_404(Task, id=id)

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


# def edit_task(request, task_id):
#     if request.method == 'POST':
#         task = get_object_or_404(Task, id=task_id)
#         print(f"Задача проекта: {task}")
#         task.name = request.POST.get('title', task.name)
#         task.description = request.POST.get('description', task.description)
#         task.status = request.POST.get('status', task.status)
#         task.save()
#     return JsonResponse({'success': True}, status=200) 

# # Функция: Удаление задачи
# def delete_task(request, task_id):
#     task = get_object_or_404(Task, id=task_id)
#     task.delete()
#     return JsonResponse({'success': True}) 

# def create_task(request, project_id):
#     if request.method == 'POST':
#         data = json.loads(request.body)
#         project = get_object_or_404(Project, id=project_id)

#         task = Task.objects.create(
#             name=data.get('title'),
#             description=data.get('description'),
#             project=project,
#             status="to_do",
#             due_date=data.get('due_date') or None,
#         )

#         if data.get("assigned_to"):
#             task.assigned_to_id = data.get("assigned_to")
#             task.save()

#         return JsonResponse({
#             "id": task.id,
#             "title": task.name,
#             "description": task.description,
#             "due_date": task.due_date
#         })

#     return JsonResponse({"error": "Invalid request"}, status=400)