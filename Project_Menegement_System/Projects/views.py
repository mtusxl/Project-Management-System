from django.shortcuts import render, get_object_or_404
from pytils.translit import slugify
from django.contrib.auth.decorators import login_required
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
