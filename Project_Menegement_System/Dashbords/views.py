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
    latest_tasks = Task.objects.filter(Q(status="in_progress") |Q( status="to_do") & Q(assigned_to=request.user)).order_by("-created_at")[:6]
  
    print(request.user)
    return render(request, "home.html", {"latest_projects":latest_projects, 
                                         "latest_tasks":latest_tasks, 
                                         "tasks_count":len(all_tasks),
                                         "projects_count": len(all_projects)})
