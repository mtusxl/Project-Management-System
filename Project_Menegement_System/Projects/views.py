from django.shortcuts import render, get_object_or_404, redirect
from pytils.translit import slugify
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Project

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