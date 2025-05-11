from django.shortcuts import render, get_object_or_404, redirect
from pytils.translit import slugify
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Q

from Projects.seriallizer import ProjectSerializer
from .models import Project
from Tasks.models import Task

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer



class project_detailAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'project.html'


    def get_project(self, slug):
        return get_object_or_404(Project, slug=slug)
    
    def get(self, request, slug):
        project = self.get_project(slug)
        if project.author==request.user or request.user.is_superuser:
            tasks = project.tasks.filter(project=project )
        else:
            tasks = project.tasks.filter(assigned_to=request.user)
        tasks_todo = tasks.filter(status="to_do")
        tasks_in_progress = tasks.filter(status="in_progress")
        tasks_done = tasks.filter(status="done")
        
        # Получаем всех участников проекта
        members = project.members.all()
        
        # Подготавливаем данные для ответа
        data = {
            "project": {
                "id": project.id,
                "name": project.name,
                "slug": project.slug,
                "description": project.description,
                "created_at": project.created_at.strftime("%d.%m.%Y"),
                "author": {
                    "id": project.author.id,
                    "username": project.author.username
                },
                "members": [
                    {
                        "id": member.id,
                        "username": member.username
                    } for member in members
                ]
            },
            "tasks": [
                {                                   
                    "id": task.id,
                    "name": task.name,  # Обратите внимание - в шаблоне ожидается name, а не title
                    "status": task.status,
                    "assigned_to": {
                        "id": task.assigned_to.id,
                        "username": task.assigned_to.username
                    } if task.assigned_to else None,
                    # добавьте другие поля задачи по необходимости
                } for task in tasks
            ],
            "tasks_todo": [
                {"id": task.id, "name": task.name} 
                for task in tasks_todo
            ],
            "tasks_in_progress": [
                {"id": task.id, "name": task.name} 
                for task in tasks_in_progress
            ],
            "tasks_done": [
                {"id": task.id, "name": task.name} 
                for task in tasks_done
            ]
        }
        
        return Response(data, status=status.HTTP_200_OK)
    

    def patch(self, request, slug):
        project = self.get_project(slug)
        serializer = ProjectSerializer(project, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, slug):
        project = self.get_project(slug)
        if project.author == request.user:
            project.delete()
            return Response(status=status.HTTP_200_OK)
        else: return Response(status=status.HTTP_403_FORBIDDEN)


class ProjectAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]
    template_name = 'project_form.html'
    def get(self, request):
        return Response(status=status.HTTP_200_OK)
    
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else: return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @login_required
# def project_list(request, slug):

#     project = get_object_or_404(Project, slug=slug)
#     tasks = project.tasks.filter(assigned_to=request.user)
#     tasks_todo = tasks.filter(status="to_do")
#     tasks_in_progress = tasks.filter(status="in_progress")
#     tasks_done = tasks.filter(status="done")
    
   
#     return render(request, "project.html", {"project":project,
#                                             "tasks":tasks,
#                                             "tasks_todo":tasks_todo,
#                                             "tasks_in_progress":tasks_in_progress,
#                                             "tasks_done":tasks_done})


# def update_project(request, slug):
#     if request.method == 'POST':
#         print("Вьюха для обновления")
#         project = get_object_or_404(Project, slug=slug)
#         if project.author != request.user:
#             return render(request, "project.html", status=403)

#         new_description = request.POST.get("description", "")
#         if new_description:
#             project.description = new_description
#             project.save()
#             print("Описание обновлено")
#             return redirect(f"/project/{project.slug}")
    
# @login_required
# def delete_project(request, slug):
#     project = get_object_or_404(Project, slug=slug)
#     if project.author != request.user:
#         return JsonResponse({'error': 'Access denied'}, status=403)

#     if request.method == 'POST':
#         project.delete()
#         return redirect('home')


# @login_required
# def Create_project(request):
#     if request.method=="POST":
#         print(f"project_name - {request.POST["project_name"]}")
#         slug = slugify(request.POST["project_name"])
#         print(f"Slug - {slug}")
#         name=request.POST.get("project_name")
#         description = request.POST.get("project_description")
#         members = request.POST.get("members")
#         print(f"members {members}")
#
#         project = Project(
#             name = name,
#             description = description,
#             author=request.user,
#             slug=slug
#         )
#         project.save()
#         project.members.add(request.user)
#         if members:
#             project.members.add(*members)
#         request.user.projects.add(project)
#         task_count = int(request.POST.get('task_count', 0))
#         for i in range(1, task_count + 1):
#             task_title = request.POST.get(f'task_title_{i}')
#             task_description = request.POST.get(f'task_description_{i}')
#             if task_title:
#                 task = Task(
#                     name=task_title,
#                     description=task_description,
#                     project=project,
#                     assigned_to = request.user

#                 )
#                 task.save()

#         return redirect(f'/project/{slug}/')
#     return  render(request, 'project_form.html')
