from django.shortcuts import render, redirect
from Projects.models import Project
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from pytils.translit import slugify

from Tasks.models import Task

@login_required
def Create_project(request):
    if request.method=="POST":
        print(f"project_name - {request.POST["project_name"]}")
        slug = slugify(request.POST["project_name"])
        print(f"Slug - {slug}")
        name=request.POST.get("project_name")
        description = request.POST.get("project_description")
        members = request.POST.getlist("members")
        
        project = Project(
            name = name,
            description = description,
            author=request.user,
            slug=slug
        )
        project.save()
        project.members.add(request.user)
        project.members.add(*members)
        request.user.projects.add(project)
        task_count = int(request.POST.get('task_count', 0))
        for i in range(1, task_count + 1):
            task_title = request.POST.get(f'task_title_{i}')
            task_description = request.POST.get(f'task_description_{i}')
            if task_title:
                task = Task(
                    name=task_title,
                    description=task_description,
                    project=project
                )
                task.save()

        return redirect(f'/project/{slug}/')

        

        
   
    return  render(request, 'project_form.html')
