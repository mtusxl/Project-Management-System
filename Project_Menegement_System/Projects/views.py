from django.shortcuts import render, get_object_or_404
from pytils.translit import slugify
from django.contrib.auth.decorators import login_required
from .models import Project

@login_required
def project_list(request, slug):

    project = get_object_or_404(Project, slug=slug)
    tasks = project.tasks.all()
    
   
    return render(request, "project.html", {"project":project,
                                            "tasks":tasks})
