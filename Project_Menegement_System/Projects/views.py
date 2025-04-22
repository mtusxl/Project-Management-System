from django.shortcuts import render, get_object_or_404, redirect
from pytils.translit import slugify
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Project
from Tasks.models import Task

@login_required
def project_list(request, slug):

    project = get_object_or_404(Project, slug=slug)
    tasks = project.tasks.filter(assigned_to=request.user)
    tasks_todo = tasks.filter(status="to_do")
    tasks_in_progress = tasks.filter(status="in_progress")
    tasks_done = tasks.filter(status="done")
    
   
    return render(request, "project.html", {"project":project,
                                            "tasks":tasks,
                                            "tasks_todo":tasks_todo,
                                            "tasks_in_progress":tasks_in_progress,
                                            "tasks_done":tasks_done})


def update_project(request, slug):
    if request.method == 'POST':
        print("Вьюха для обновления")
        project = get_object_or_404(Project, slug=slug)
        if project.author != request.user:
            return render(request, "project.html", status=403)

        new_description = request.POST.get("description", "")
        if new_description:
            project.description = new_description
            project.save()
            print("Описание обновлено")
            return redirect(f"/project/{project.slug}")
    
@login_required
def delete_project(request, slug):
    project = get_object_or_404(Project, slug=slug)
    if project.author != request.user:
        return JsonResponse({'error': 'Access denied'}, status=403)

    if request.method == 'POST':
        project.delete()
        return redirect('home')


@login_required
def Create_project(request):
    if request.method=="POST":
        print(f"project_name - {request.POST["project_name"]}")
        slug = slugify(request.POST["project_name"])
        print(f"Slug - {slug}")
        name=request.POST.get("project_name")
        description = request.POST.get("project_description")
        members = request.POST.get("members")
        print(f"members {members}")
        
        project = Project(
            name = name,
            description = description,
            author=request.user,
            slug=slug
        )
        project.save()
        project.members.add(request.user)
        if members:
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
                    project=project,
                    assigned_to = request.user

                )
                task.save()

        return redirect(f'/project/{slug}/')
    return  render(request, 'project_form.html')
