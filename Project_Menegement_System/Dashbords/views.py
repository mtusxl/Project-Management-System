from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from Projects.models import Project
from Tasks.models import Task

@login_required
def home(request):
    latest_projects = Project.objects.filter(Q(author=request.user) | Q(members=request.user)).order_by('-created_at')[:2]
    all_projects = Project.objects.filter(Q(author=request.user) | Q(members=request.user)).all()
    all_tasks = Task.objects.filter(assigned_to=request.user).all()
    latest_tasks = Task.objects.filter(Q(assigned_to=request.user) & (Q(status="in_progress") | Q(status="to_do"))).order_by("-created_at")[:6]
    all_tasks_done = Task.objects.filter(Q(assigned_to=request.user) & (Q(status="Done") | Q(status="done")))
    projects = []
    for project in latest_projects:
        
        tasks_done = project.tasks.filter(Q(status="Done") | Q(status="done")).all()
        all_tasks_project = Task.objects.filter(project=project).all()

        progress = int((len(tasks_done)/len(all_tasks_project))*100) if len(all_tasks_project) > 0 else 0
        projects.append([project, progress])
  
        

        
  
    
    return render(request, "home.html", {"latest_projects": projects,
                                         "latest_tasks":latest_tasks, 
                                         "tasks_count":len(all_tasks),
                                         "projects_count": len(all_projects),
                                         "done_tasks":len(all_tasks_done)})
